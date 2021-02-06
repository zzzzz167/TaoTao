#--*-- coding:utf-8 --*--
import requests
import json
import time

host = 'https://api.uomg.com/api/comments.163?format=json'
host_s= 'http://musicapi.leanapp.cn/search?keywords={}'

def post():#post请求
    post_respose = requests.post(url=host)
    post_rest = post_respose.text
    #print(post_rest)
    return post_rest

def get(host_s):
    respose = requests.get(host_s)
    get_rest = respose.text
    return get_rest

def reping():
    rest_all = json.loads(post())
    if(rest_all['code'] == 1 ):
        rest = "{}\n来自@{}\n在[{}]\n歌曲下的评论".format(rest_all['data']['content'],rest_all['data']['nickname'],rest_all['data']['name'])
        #print(rest)
        return rest
    else:
        reping()

def diange(name):
    rest_all_se = json.loads(get("http://musicapi.leanapp.cn/search?keywords={}".format(name)))
    datas_se = rest_all_se['result']['songs']
    first_data = datas_se[0]
    sid = first_data['id']

    rest_all = json.loads(get('http://musicapi.leanapp.cn/song/detail?ids={}'.format(sid)))
    datas = rest_all['songs']
    name = datas[0]['name']
    ar_nmae = datas[0]['ar'][0]['name']
    pic_url = datas[0]['al']['picUrl']

    xml_data = '''<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
    <msg serviceID="146" templateID="1" action="web" brief="[分享] {} - 网易云音乐" sourceMsgId="0" url="https://y.music.163.com/m/song?id={}" flag="0" adverSign="0" multiMsgFlag="0">
    <item layout="2" advertiser_id="0" aid="0">
    <picture cover="{}" w="0" h="0" />
    <title>{}</title>
    <summary>{}</summary>
    </item>
    <source name="网易云音乐" icon="https://url.cn/55gqiDG" url="http://url.cn/5pl4kkd" action="app" a_actionData="com.netease.cloudmusic" i_actionData="tencent100495085://" appid="100495085" />
    </msg>'''.format(name,sid,pic_url,name,ar_nmae)

    return xml_data
