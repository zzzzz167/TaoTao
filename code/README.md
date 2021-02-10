# code

该仓库为洮洮的QQ机器人仓库，由小指针进行发，您如果有疑惑与想法请提交issue，来告诉小指针，您也可以使用该源码进行二次创作，只要您在项目后标明该仓库地址。如果您觉得您可以请务必提交pr，由小指针进行适配后合并到该仓库，当然我们也会在其贡献者中填入您的名字。感谢您对该项目的支持。

在git本仓库时，因为训练模型大的原因，需使用git lfs进行

### 目前开发出的功能

- 网易云热评
- 点歌
- 黄历
- 语音识别
- 微博热搜
- 闲聊（目前使用的是小黄鸡语料



### 使用方法

------

配置好mirai以及mirai-http-api，可以到[这里](https://github.com/mamoe/mirai)查看详情，以及进行部署，完毕后运行

安装python，pip安装[Graia](https://github.com/GraiaProject/Application)，Lunar库

将该文件夹下载下来，打开tao.ini在account中填入您的机器人QQ号，在tenxun_api中填入您的api密钥。

运行main.py即可



### 目录结构说明



```
code
│  ffmpeg.exe
│  huangli.py#黄历插件
│  log.py#日志文件
│  main.py#主程序
│  README.md
│  silk_v3_decoder.exe#解码器
│  silk_v3_encoder.exe#编码器
│  tao.ini
│  Tao.py#闲聊插件
│  tenxun_voice.py#腾讯语音转文字
│  wangyiyun.py#网易云插件
│  weibo.py#微博插件
│
├─chatbot_quick_start
│  │  CONFIG.py#配置文件
│  │  DataProcessing.py
│  │  RestfulAPI.py#api接口
│  │  SequenceToSequence.py
│  │  Train.py#训练模型
│  │
│  ├─data
│  │      data.pkl
│  │      w2i.pkl
│  │      xiaohuangji50w_nofenci.conv#小黄鸡语料
│  │
│  ├─graph
│  │  └─nlp
│  │          events.out.tfevents.1612801284.AILLIOM-CPT
│  │
│  ├─model#已经训练好的模型
│  │      chatbot_model.ckpt.data-00000-of-00001
│  │      chatbot_model.ckpt.index
│  │      chatbot_model.ckpt.meta
│  │      checkpoint
│
├─log#日志文件
├─picture
│      test.jpg#测试照片
│
├─voice
│  │  test.mp3#一段hello_world的音频
│  │
│  └─rep#接收到的音频文件
```

### ToDo

------

- [ ] 随机涩图与涩图搜索（不会封号的那种）
- [x] 代码的优化（现在的复用代码太多了）
- [x] 自然语言处理（让洮洮能与人无障碍的交流）
- [ ] ~~生理期~~
- [x] 更好的日志输出
- [ ] 地区天气
- [ ] 每日趣事与新闻
- [ ] 黄历插件的功能添加
- [ ] 自定义需要的群
- [ ] 一些小工具
- [ ] 属于自己的词料

### 闲聊

------

请按照以下环境进行配置

conda虚拟环境,python版本=3.6，所需的库已经放在chatbot_quick_start的pip.txt与conda.txt中可直接使用

在配置完成后运行RestfulAPI.py

在浏览器中输入：http://127.0.0.1:8000/api/chatbot?infos=【你想说的话】

稍等一会，如果出现回答则为成功配置

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

感谢ximingxing提供的闲聊[chatbot](https://github.com/ximingxing/chatbot)

以及一些api接口

