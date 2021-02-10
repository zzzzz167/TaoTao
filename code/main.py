from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session
from graia.application.message.chain import MessageChain
import asyncio

from graia.broadcast.interrupt import InterruptControl
from graia.application.message.elements.internal import Plain,At,Voice,Image,Xml
from graia.application.friend import Friend
from graia.application.group import Group, Member

import configparser
import wangyiyun
import weibo
import log
import time
import os
import tenxun_voice
import huangli
import Tao

config = configparser.ConfigParser() # ini类实例化
loop = asyncio.get_event_loop()

config.read("tao.ini")
bcc = Broadcast(loop=loop)


app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="{}:{}".format(config['connect_mirai']['host'],config['connect_mirai']['port']),  # 填入 httpapi 服务运行的地址
        authKey=config['connect_mirai']['authKey'],  # 填入 authKey
        account=config.getint('connect_mirai','account'),  # 机器人的 qq 号
        websocket=config.getboolean('connect_mirai','websocket')  # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
    ),
    logger=log.CustomLogger() #继承日志输出的抽象调用方法
)
inc =InterruptControl(bcc)

async def netease_cloud_music_hot(some,*member):
    send_message = MessageChain.create([Plain(wangyiyun.reping())])
    if member[0] == ():
        await app.sendFriendMessage(some, send_message)
    else:
        at = MessageChain.create([At(member[0][0].id)])
        await app.sendGroupMessage(some,MessageChain.join(at,send_message))

async def netease_cloud_music_get(some,rmsg,*member):
    m = rmsg.split(' ')
    if len(m) == 2:
        send_message = MessageChain.create([Xml(wangyiyun.diange(m[1]))])
    else:
        MessageChain.create([Plain("您输入的参数有误请使用 点歌 [歌曲名] 来进行点歌")])
    if member[0] == ():
        await app.sendFriendMessage(some, send_message)
    else:
        await app.sendGroupMessage(some,send_message)
async def hot_weibo(some,rmsg,*member):
    m = rmsg.split(' ')
    if len(m) == 2:
        serial = int(m[1]) - 1
        reso_data = weibo.reso()[1]
        if serial >= len(reso_data):
            send_message = MessageChain.create([Plain("查找数值不正确,数值应为1~{}".format(len(reso_data)))])
        else:
            send_message = MessageChain.create([
                Plain("序号:{}\n"
                      "标题:{}\n"
                      "链接:{}"
                      .format(
                    reso_data[serial]['id'] + 1,
                    reso_data[serial]['name'],
                    reso_data[serial]['url']))])
    elif len(m) == 1:
        send_message = MessageChain.create([Plain('\n{}\n输入 微博热搜 [序号] 来获取访问链接'.format(weibo.reso()[0]))])
    else:
        send_message = MessageChain.create([Plain("你输入的参数有误")])
    if member[0] == ():
        await app.sendFriendMessage(some, send_message)
    else:
        at = MessageChain.create([At(member[0][0].id)])
        await app.sendGroupMessage(some,MessageChain.join(at,send_message))

async def Lunar(some,*member):
    send_message = MessageChain.create([Plain(huangli.get())])
    if member[0] == ():
        await app.sendFriendMessage(some,send_message)
    else:
        at = MessageChain.create([At(member[0][0].id)])
        await app.sendGroupMessage(some,MessageChain.join(at,send_message))

async def chat(msg,some,*member):
    send_message = MessageChain.create([Plain(Tao.skype_chat(msg))])
    if member[0] != ():
        await app.sendGroupMessage(some,send_message)

async def judge(msg, some, *member):
    if msg.startswith("网易云热评") or msg.startswith("网抑云热评"):
        await netease_cloud_music_hot(some,member)
    elif msg.startswith("黄历"):
        await Lunar(some,member)
    elif msg.startswith("微博热搜"):
        await hot_weibo(some,msg,member)
    elif msg.startswith("点歌"):
        await netease_cloud_music_get(some,msg,member)
    else:
        await chat(msg,some,member)

async def voice_get(message,member,group,app):   #异步处理silk音频文件
    now_time = time.time()
    with open('voice/rep/{}-{}-get.silk'.format(member.id,now_time), 'wb') as v:
        v.write(await Image.http_to_bytes(message.get(Voice)[0]))
    while (1):
        if os.path.exists('voice/rep/{}-{}-get.silk'.format(member.id,now_time)):
            break
    log.CustomLogger.info(Group,"rep voice")
    #音频转码
    os.system(r'.\silk_v3_decoder.exe voice/rep/{}-{}-get.silk voice/rep/{}-{}-middle.pcm'.format(member.id,now_time,member.id,now_time))
    os.system(r'ffmpeg.exe -f s16le -ar 24000 -ac 1 -i voice/rep/{}-{}-middle.pcm voice/rep/{}-{}-end.wav'.format(member.id,now_time,member.id,now_time))
    #语音转文字
    Td=tenxun_voice.send(member.id,now_time)
    log.CustomLogger.info(group,"Td:"+str(Td))
    Mg=str(tenxun_voice.get(Td))
    log.CustomLogger.info(group, "Message:" + Mg)
    #消息判断
    await judge(Mg,group,member)

#处理好友信息
@bcc.receiver("FriendMessage")
async def friend_message_listener(
        app: GraiaMiraiApplication,
        friend: Friend,
        message: MessageChain,
):
    msg = message.asDisplay()
    if msg.startswith("#"):
        await judge(msg[1:], friend)

#处理群组消息
@bcc.receiver("GroupMessage")
async  def group_message_listener(
        message:MessageChain,
        app:GraiaMiraiApplication,
        group:Group,member:Member,
):
    msg = message.asDisplay()
    if msg.startswith("#"):
        await judge(msg[1:],group,member)
    if message.has(Voice):
        log.CustomLogger.debug(group,message.get(Voice))
        await voice_get(message,member,group,app)


app.launch_blocking()