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
    if ("网易云热评" in Mg):
        await  app.sendGroupMessage(group, MessageChain.create([
            At(member.id), Plain(wangyiyun.reping())
        ]))
    else:
        await app.sendGroupMessage(group,MessageChain.create([
            Plain(Mg)
        ]))

#处理好友信息
@bcc.receiver("FriendMessage")
async def friend_message_listener(
        app: GraiaMiraiApplication,
        friend: Friend,
        message: MessageChain,
):
    if message.asDisplay().startswith("网易云热评") or message.asDisplay().startswith("网抑云热评"): #网易云热评
        await app.sendFriendMessage(friend, MessageChain.create([
            Plain(wangyiyun.reping())
        ]))
    elif message.asDisplay().startswith("微博热搜"):
        m = message.asDisplay().split(' ')
        if len(m) == 2:
            serial = int(m[1])-1
            log.CustomLogger.info(friend,"微博序号：{}]".format(serial))
            reso_data = weibo.reso()[1]
            if serial >= len(reso_data):
                await app.sendFriendMessage(friend,MessageChain.create([
                    Plain("查找数值不正确,数值应为1~{}".format(len(reso_data)))
                ]))
            else:
                await app.sendFriendMessage(friend,MessageChain.create([
                    Plain("\n序号:{}\n标题:{}\n链接:{}".format(reso_data[serial]['id']+1,reso_data[serial]['name'],reso_data[serial]['url']))
                ]))
        elif len(m)== 1:
            await app.sendFriendMessage(friend,MessageChain.create([
                Plain('\n{}\n输入 微博热搜 [序号] 来获取访问链接'.format(weibo.reso()[0]))
            ]))
        else:
            await app.sendFriendMessage(friend,MessageChain.create(
                Plain("你输入的参数有误"))
            )
    elif message.asDisplay().startswith("黄历"):
        await app.sendFriendMessage(friend, MessageChain.create([
            Plain('\n{}'.format(huangli.get()))
        ]))
    elif message.asDisplay().startswith("pic_test"):
        await app.sendFriendMessage(friend, MessageChain.create([
            Image.fromLocalFile("picture/test.jpg")
        ]))
    elif message.has(Image):
        log.CustomLogger.debug(friend,message.get(Image))
        with open('test.jpg','wb') as f:
            f.write(await Image.http_to_bytes(message.get(Image)[0]))

#处理群组消息
@bcc.receiver("GroupMessage")
async  def group_message_listener(
        message:MessageChain,
        app:GraiaMiraiApplication,
        group:Group,member:Member,
):
    if message.asDisplay().startswith("网易云热评") or message.asDisplay().startswith("网抑云热评"):  # 网易云热评
        await  app.sendGroupMessage(group,MessageChain.create([
            At(member.id),Plain(wangyiyun.reping())
        ]))
    elif message.asDisplay().startswith("点歌"):
        m = message.asDisplay().split(' ')
        if len(m) == 2:
            await app.sendGroupMessage(group,MessageChain.create([
               Xml(wangyiyun.diange(m[1]))
            ]))
        else:
            await app.sendGroupMessage(group,MessageChain.create([
                Plain("您输入的参数有误请使用 点歌 [歌曲名] 来进行点歌")
            ]))
    elif message.asDisplay().startswith("微博热搜"):
        m = message.asDisplay().split(' ')
        if len(m) == 2:
            serial = int(m[1])-1
            log.CustomLogger.info(group,"微博序号：{}]".format(serial))
            reso_data = weibo.reso()[1]
            if serial >= len(reso_data):
                await app.sendGroupMessage(group,MessageChain.create([
                    At(member.id), Plain("查找数值不正确,数值应为1~{}".format(len(reso_data)))
                ]))
            else:
                await app.sendGroupMessage(group,MessageChain.create([
                    At(member.id),Plain("\n序号:{}\n标题:{}\n链接:{}".format(reso_data[serial]['id']+1,reso_data[serial]['name'],reso_data[serial]['url']))
                ]))
        elif len(m)== 1:
            await app.sendGroupMessage(group,MessageChain.create([
                At(member.id),Plain('\n{}\n输入 微博热搜 [序号] 来获取访问链接'.format(weibo.reso()[0]))
            ]))
        else:
            await app.sendGroupMessage(group,MessageChain.create(
                At(member.id,Plain("你输入的参数有误"))
            ))
    elif message.asDisplay().startswith("黄历"):
        await app.sendGroupMessage(group, MessageChain.create([
            At(member.id), Plain('\n{}'.format(huangli.get()))
        ]))
    elif message.asDisplay().startswith("voice_test"):
        try:
            await  app.sendGroupMessage(group,MessageChain.create([
                Voice.fromLocalFile(group.id,'voice/test.mp3')
            ]))
        except:
           log.CustomLogger.error(group,"voice test has error")

    if message.has(Voice):
        log.CustomLogger.debug(group,message.get(Voice))
        await voice_get(message,member,group,app)




app.launch_blocking()