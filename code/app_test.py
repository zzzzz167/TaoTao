from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session
from graia.application.message.chain import MessageChain
import asyncio

from graia.application.message.elements.internal import Plain,App,Json,Xml
from graia.application.friend import Friend

import configparser

loop = asyncio.get_event_loop()
config = configparser.ConfigParser()

config.read("tao.ini")
bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="{}:{}".format(config['connect_mirai']['host'], config['connect_mirai']['port']),  # 填入 httpapi 服务运行的地址
        authKey=config['connect_mirai']['authKey'],  # 填入 authKey
        account=config.getint('connect_mirai', 'account'),  # 机器人的 qq 号
        websocket=config.getboolean('connect_mirai', 'websocket')  # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
    ),
)

xml_data = '''<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<msg serviceID="146" templateID="1" action="web" brief="[分享] 芒种 - 网易云音乐" sourceMsgId="0" url="https://y.music.163.com/m/song?id=1369798757" flag="0" adverSign="0" multiMsgFlag="0">
<item layout="2" advertiser_id="0" aid="0">
<picture cover="http://p1.music.126.net/KFWbxh1ZLyy9WR77Ca08tA==/109951164866828786.jpg" w="0" h="0" />
<title>芒种</title>
<summary>音阙诗听，赵方婧 - 二十四节气</summary>
</item>
<source name="网易云音乐" icon="https://url.cn/55gqiDG" url="http://url.cn/5pl4kkd" action="app" a_actionData="com.netease.cloudmusic" i_actionData="tencent100495085://" appid="100495085" />
</msg>'''


@bcc.receiver("FriendMessage")
async def friend_message_listener(app: GraiaMiraiApplication, friend: Friend):
    await app.sendFriendMessage(friend, MessageChain.create([
        Xml(xml_data)
    ]))

app.launch_blocking()