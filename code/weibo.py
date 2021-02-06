#--*-- coding:utf-8 --*--
import requests
import json

host = 'https://api.hmister.cn/weibo/'

def get():
    respose = requests.get(host)
    get_rest = respose.text
    return get_rest

def reso():
    end_data =[]
    rest_all = json.loads(get())
    if(rest_all['code'] == 200):
        datas = rest_all['data'][0:10]
        #print(datas)
        for data in datas:
            end_data.append("{}.{}".format(data['id']+1,data['name']))
        #print('\n'.join(end_data))
        return '\n'.join(end_data),rest_all['data']

    else:
        reso()