> API

# 2.API

提交人：SCP-173[2549133]  
提交日期：2023-04-09  
原文地址：https://wiki.torn.com/wiki/API

## 细节：
___
“API”是Torn提供的一种新工具，您可以使用它来构建自己的Torn应用程序/扩展。此页面上的信息直接从 [API网站](https://www.torn.com/api.html) 复制而来（包括来自Torn的几个人添加的信息），因此在使用API之前，请务必仔细阅读它。

要开始使用API，请转到 [此处](https://www.torn.com/api.html) ，然后单击“Try It!”按钮。之后您可以在顶部填写您的API密钥，此密钥可以在 [此页面](https://www.torn.com/preferences.php) 的“API keys”选项中找到。然后选择例如用户部分，填写您的ID和您选择的选项。

如果您不知道选项并且它们未显示在“尝试”部分中，则始终可以转到 [api.torn.com/user/?selections=lookup&key=apikeyhere](api.torn.com/user/?selections=lookup&key=apikeyhere) 以查看可能的选项。

## 简介：
___
首先，API是什么意思？它代表应用程序编程接口。可以在 **此处（原文链接缺失）** 找到完整定义，但更重要的是它能做什么，您可以在本页面的详细信息部分找到。

Torn API的目标是为玩家提供完全支持和只读的方法，以从Torn获取有关其玩家，派系或公司的有用信息。这可以单独使用，以检索有关您帐户的信息，或者您可以构建一个网站，整个社区都可以使用该网站来利用通过API公开的数据进行有趣的事情。

## 潜力：
___
无论您是在制作浏览器扩展以帮助派系进行战时活动，还是制作移动应用程序以提供即时通知，或者制作用于跟踪数据以进行绘图的网站——只要使用这 16 个字符的 API 密钥，您的可能性是无限的。我们鼓励您富有创造力，构建功能和工具，扩展 Torn 的游戏性和乐趣。

## 使用规则：
___
这个系统的开发是为了让您仅需要向用户请求一个API密钥。只要拥有密钥，就可以获取用户的所有信息，没有必要询问姓名或用户ID。**绝不能**要求任何用户提供Torn的密码。

您必须保护和保密密钥以及从中获得的数据，除非得到密钥所有者的许可。接受其他用户的密钥，他们对您寄予了信任，请勿滥用此信任。我们将立即永久禁止违规应用程序访问API。

我们恭请您在构建使用我们的API系统的网站或应用程序时遵循Torn的无广告政策，以确保最佳的用户体验，但可以例外。如果您想要进行广告宣传、接受自愿的实际货币捐款或向用户收费，请 [联系我们](mailto:api@torn.com) 。

请确保您的脚本经过优化，仅检索特定请求所需的信息。它们应该尽可能少地检索信息；这将提高加载时间并减少对Torn服务器的压力。

## 不公平的优势:
___
我们明白，为Torn制作一个API系统可能会让一些用户获得不公平的优势。我们希望该系统能够扩展和增强游戏玩法，而不是为用户提供更容易与他人竞争的优势。我们在开发过程中已经考虑到了这一点，但我们将聆听反馈，并进行任何必要的适当更改。

## 日志记录:
___
请注意，我们记录所有请求的详细信息和输入，并进行例行检查。如果发生滥用，我们将立即永久禁止IP地址、密钥和用户访问系统。

## 自动限制和阻止:
___
每个用户密钥每分钟最多可以发出100个单独的请求，这应该足够实现几乎任何事情。使用无效密钥进行多次请求可能会导致暂时的IP禁止 - 您必须在出现错误时通过删除已禁用或无效的密钥来解决这个问题。

这些限制可能会在不事先通知的情况下发生变化，以确保 Torn 服务器保持稳定。

## 访问级别:
___
用户可以为不同的脚本或工具创建不同的密钥。用户可以拥有10个密钥，每个密钥都具有不同级别的访问权限，并且每个密钥都可以在用户想要的时候单独删除。每个访问级别都对可以使用密钥检索的数据有限制。

每个密钥有4个访问级别，即“仅公共信息”、“最小访问权限”、“有限访问权限”、“完全访问权限”，可以在 [API文档](https://www.torn.com/api.html#%7C) 中找到可以由密钥访问的信息。

## 错误代码:
___
0 => **未知错误**：未处理的错误，不应该发生。

1 => **密钥为空**：当前请求中的私钥为空。

2 => **错误的密钥**：私钥错误或格式不正确。

3 => **错误的类型**：请求了不正确的基本类型。

4 => **错误的字段**：请求了不正确的选择字段。

5 => **请求过多**：由于请求过多（最多每分钟100次），当前私钥被禁用一小段时间。

6 => **错误的ID**：ID值错误。

7 => **错误的ID-实体关系**：请求的选择是私有的（例如，另一个用户/派系的个人数据）。

8 => **IP封禁**：由于滥用，当前IP被禁用一小段时间。

9 => **API禁用**：API系统目前已禁用。

10 => **密钥所有者在联邦监狱中**：由于所有者在联邦监狱中，当前密钥无法使用。

11 => **密钥更改错误**：您每60秒只能更改一次API密钥。

12 => **密钥读取错误**：从数据库读取密钥时出错。

13 => **由于所有者不活跃，该密钥已暂时禁用**：在7天后，不活跃的玩家密钥可能无法进行API调用。

14 => **达到每日读取限制**：该用户今天从我们的云服务中提取的记录太多。

15 => **临时错误**：专门用于测试目的的错误代码，没有专门的含义。

16 => **该密钥的访问级别不足**：正在调用一个选择，但此密钥没有权限访问。

## 示例：
___
这里将提供几种编程语言的简短代码示例，以展示如何使用API。

* JavaScript:
```
  fetch("https://api.torn.com/user/?selections=skills&key=APIKEY") // 通过API获取数据
  .then((response) => response.json()) // 将获取到的数据转换成JSON格式
  .then((jsonResponse) => console.log(jsonResponse)); // 打印JSON内容
```

* Python:
```
  import requests
  r = requests.get("apiurl") # 查询"apiurl"并返回从Torn获取的响应
  data = r.json()            # 将该响应转换为一个字典变量
  print(data)                # 打印变量
```

* PHP:
```
  <?php
    $jsonurl = "http://api.torn.com/user/[MyID]?selections=networth&key=[MyKey]";
    $json = file_get_contents($jsonurl); //获取API相应
    $decodedString = json_decode($json, true); //将API相应解析为JSON
    $nwtotal = $decodedString["networth"]; //从JSON数组中提取"netwworth"
    echo "Stock Market: ".$nwtotal["stockmarket"]."</br>"; // 输出股票净值
    echo "Networth Total: ".$nwtotal["total"]."</br>"; // 输出总净值
?>
```

## 安全可靠的应用程序:
___
以下是一些已知的安全可靠的应用程序，它们需要您的 API：
* [Torn Stats](https://www.tornstats.com/) ，由 [IceBlueFire](https://www.torn.com/profiles.php?XID=776) 制作
* [DoctorN](https://chrome.google.com/webstore/detail/doctorn-for-torn/kfdghhdnlfeencnfpbpddbceglaamobk) ，由 [Mauk](https://www.torn.com/profiles.php?XID=1494436) 制作
* [TornTools](https://www.torn.com/forums.php#/p=threads&f=67&t=16243863) ，由 [Mephiles](https://www.torn.com/profiles.php?XID=2087524) 制作
* [YATA](https://yata.yt/) ，由 [Kivou](https://www.torn.com/profiles.php?XID=2000607) 制作
* [Torn PDA](https://www.torn.com/forums.php#/p=threads&f=67&t=16163503&b=0&a=0) ，由 [Manuito](https://www.torn.com/profiles.php?XID=2225097) 制作
