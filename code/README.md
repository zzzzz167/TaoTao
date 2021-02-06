# code

该仓库为洮洮的QQ机器人仓库，由小指针进行发，您如果有疑惑与想法请提交issue，来告诉小指针，您也可以使用该源码进行二次创作，只要您在项目后标明该仓库地址。如果您觉得您可以请务必提交pr，由小指针进行适配后合并到该仓库，当然我们也会在其贡献者中填入您的名字。感谢您对该项目的支持。



### 目前开发出的功能

- 网易云热评
- 点歌
- 黄历
- 语音识别
- 微博热搜



### 使用方法

------

配置好mirai以及mirai-http-api，可以到[这里](https://github.com/mamoe/mirai)查看详情，以及进行部署，完毕后运行

安装python，pip安装[Graia](https://github.com/GraiaProject/Application)，Lunar库

将该文件夹下载下来，打开tao.ini在account中填入您的机器人QQ号，在tenxun_api中填入您的api密钥。

运行main.py即可



### 目录结构说明



```
code
│  ffmpeg.exe#音频转码器
│  huangli.py#黄历插件
│  log.py#一个抽象的日志输出
│  main.py#主程序
│  README.md
│  silk_v3_decoder.exe#音频解码器
│  silk_v3_encoder.exe#音频编码器
│  tao.ini#洮洮的运行配置
│  tenxun_voice.py#腾讯语音api
│  wangyiyun.py#网易云音乐插件
│  weibo.py#微博热评
│
├─.idea#pychram运行产生的文件
├─log#日志输出目录
│
├─picture#图片保存位置
│      test.jpg#测试图片
│
├─voice#音频目录
│  │  test.mp3#一段HELLO_WORLD的音频
│  │
│  └─rep接受到的音频
└─__pycache__#自写库在运行过程中产生的文件
```

### ToDo

------

- [ ] 随机涩图与涩图搜索（不会封号的那种）
- [ ] 代码的优化（现在的复用代码太多了）
- [ ] 自然语言处理（让洮洮能与人无障碍的交流）
- [ ] ~~生理期~~
- [ ] 更好的日志输出
- [ ] 地区天气
- [ ] 每日趣事与新闻
- [ ] 黄历插件的功能添加
- [ ] 自定义需要的群
- [ ] 一些小工具

### 鸣谢及相关项目

------

\> 这些项目也很棒, 去他们的项目页看看, 点个 `Star` 以鼓励他们的开发工作, 毕竟没有他们也没有 `洮洮这个机器人`.

特别感谢 [`mamoe`](https://github.com/mamoe) 给我们带来这些精彩的项目:

 \- [`mirai`](https://github.com/mamoe/mirai): 即 `mirai-core`, 一个高性能, 高可扩展性的 QQ 协议库

 \- [`mirai-console`](https://github.com/mamoe/mirai-console): 一个基于 `mirai` 开发的插件式可扩展开发平台

 \- [`mirai-api-http`](https://github.com/project-mirai/mirai-api-http): 为本项目提供与 `mirai` 交互方式的 `mirai-console` 插件

也感谢[`Elaina`](https://github.com/GreyElaina)为我们带来Graia 这个十分好使的python库

[luanar](http://6tail.cn/calendar/api.html#overview.html)是一个无依赖的支持阳历和阴历的日历工具库

微软小冰所提供的思路（[The Design and Implementation of XiaoIce, an Empathetic Social Chatbot](https://arxiv.org/abs/1812.08989?context=cs.CL)

以及一些api接口

