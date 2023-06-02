import requests
import sys
from collections import defaultdict

from log_catcher import TornLogCatcher
from basic_ui import Ui_Form
import threading
from gdoc_basic import GoogleSheetAgent

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, Qt
import PyQt5

class Spy_Catcher(TornLogCatcher):
    TS_FACTION_DICT = {
        "CCRC" : 27902,
        "PTA" : 9356,
        "PN" : 20465,
        "SH" : 36134,
        "NOV" : 16335,
        "BSU" : 11796
    }

    def __init__(self, key):
        super().__init__(key)
        self.ts_session = requests.Session()
        self.gdoc_agent = GoogleSheetAgent("ctr4l_cred.json")

    def get_torn_stats_data(self, faction_name):
        if faction_name not in Spy_Catcher.TS_FACTION_DICT:
            Spy_Catcher.TS_FACTION_DICT["temp"] = faction_name
            faction_name = "temp"

        url = "https://www.tornstats.com/api/v2/{}/spy/faction/{}".format(self.api_key, Spy_Catcher.TS_FACTION_DICT[faction_name])
        res = self._general_request(url, True, True, self.ts_session)
        return res
    
    def get_yata_stats_data(self):
        url = "https://yata.yt/api/v1/faction/members/?key={}".format(self.api_key)
        res = self._general_request(url, True, True, self.ts_session)
        return res

    def save_member_data(self, faction_name, ts_json_, yata_json_):
        record_users = defaultdict(list)
        
        # torn stats
        try:
            for tid in ts_json_['faction']["members"]:
                data = ts_json_['faction']["members"][tid]
                if data.get("spy", None):
                    record_users[tid] = [data["name"],
                                        tid,
                                        data["spy"]["strength"],
                                        data["spy"]["defense"],
                                        data["spy"]["speed"],
                                        data["spy"]["dexterity"],
                                        data["spy"]["total"]
                                        ]
                else:
                    record_users[tid] = [data["name"], tid]
        except KeyError as e:
            print(e)
            print("Your Key might not be registered in Torn Stats, Skip now...")        
        
        # yata stats
        try:
            for tid in yata_json_["members"]:
                if len(record_users[tid]) > 2:
                    continue

                data = yata_json_["members"][tid]
                if data["stats_share"] == 0:
                    record_users[tid] = [data["name"], tid]
                else:
                    record_users[tid] = [data["name"], 
                                        tid, 
                                        data["stats_strength"],
                                        data["stats_defense"],
                                        data["stats_speed"],
                                        data["stats_dexterity"],
                                        data["stats_total"]
                                        ]
        except KeyError as e:
            print("Error encountering when parsing yata stats, Skip now...")

        # merge
        all_stats = []
        for tid in record_users:
            if len(record_users[tid]) > 2:
                all_stats.append(record_users[tid])
            else:
                all_stats.append(record_users[tid] + [0,0,0,0,0])
        
        all_stats.sort(key=lambda x:x[6], reverse=True)

        # write
        with open(faction_name + "_SPY.csv", "w") as f:
            f.write("Name,ID,Str,Def,Spd,Dex,Total\n")
            for item in all_stats:
                f.write("{},{},{},{},{},{},{}\n".format(item[0],item[1],item[2],item[3],item[4],item[5],item[6]))

        res, doc_url = self.gdoc_agent.update(write_array=[["Name","ID","Str","Def","Spd","Dex","Total"]] + all_stats, sheet_name=faction_name)
        return doc_url + " " + res

class MainWindow(QWidget, QObject):
    finished = pyqtSignal(str)
    terminated = pyqtSignal(str)

    def set_align_center(self):
        self.ui.faction_name.setEditable(True)
        self.ui.faction_name.lineEdit().setAlignment(Qt.AlignCenter)
        self.ui.faction_name.lineEdit().setReadOnly(True)

        self.ui.key.setAlignment(Qt.AlignCenter)
        self.ui.faction_id_opt.setAlignment(Qt.AlignCenter)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.set_align_center()

        self.ui.pushButton.clicked.connect(self.start)
        self.finished.connect(self.notify)
        self.terminated.connect(self.report_error)
    
    def start(self):
        thread = threading.Thread(target=self.spy)
        thread.start()

    def notify(self, file_name):
        finish_ = QMessageBox()
        finish_.setText("{} successfully generated!".format(file_name))
        finish_.exec_()

    def report_error(self, err):
        finish_ = QMessageBox()
        finish_.setText("error happens, msg is {}".format(err))
        finish_.exec_()

    def spy(self):
        #  eS1eojybR4IyZzU4
        try:
            key = self.ui.key.text()
            faction_name = self.ui.faction_name.currentText()
            if faction_name == "Others":
                faction_name = self.ui.faction_id_opt.text()

            spy = Spy_Catcher(key)
            ts_json = spy.get_torn_stats_data(faction_name)
            yata_json = {}
            # 如果Key拥有者的帮派和输入不一致，则不抓取yata数据
            user_faction_id = spy.get_user_data_json("", "profile")["faction"]["faction_id"]
            if user_faction_id == spy.TS_FACTION_DICT.get(faction_name, "") or user_faction_id == faction_name:
                yata_json = spy.get_yata_stats_data()
            
            doc_url = spy.save_member_data(faction_name, ts_json, yata_json)
        except Exception as e:
            self.terminated.emit(repr(e))
            return

        self.finished.emit(doc_url)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()