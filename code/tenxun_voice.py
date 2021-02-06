import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.asr.v20190614 import asr_client, models
import log
import base64
import configparser

config = configparser.ConfigParser()
config.read("tao.ini")

def send(mid,now_time):
    try:
        file = open("voice/rep/{}-{}-end.wav".format(mid,now_time),"rb").read()
        data = base64.b64encode(file).decode('utf-8')
        cred = credential.Credential(config['tenxun_api']['secretId'], config['tenxun_api']['secretKey'])
        httpProfile = HttpProfile()
        httpProfile.endpoint = "asr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = asr_client.AsrClient(cred, "", clientProfile)

        req = models.CreateRecTaskRequest()
        params = {
            "EngineModelType": "16k_zh",
            "ChannelNum": 1,
            "ResTextFormat": 0,
            "SourceType": 1,
            "Data": data
        }
        req.from_json_string(json.dumps(params))

        resp = json.loads(client.CreateRecTask(req).to_json_string())
        return resp['Data']['TaskId']

    except TencentCloudSDKException as err:
        print(err)
        send(mid,now_time)

def get(Taskid):
    try:
        cred = credential.Credential(config['tenxun_api']['secretId'], config['tenxun_api']['secretKey'])
        httpProfile = HttpProfile()
        httpProfile.endpoint = "asr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = asr_client.AsrClient(cred, "", clientProfile)

        req = models.DescribeTaskStatusRequest()
        params = {
            "TaskId": Taskid
        }
        req.from_json_string(json.dumps(params))

        resp = json.loads(client.DescribeTaskStatus(req).to_json_string())
        if(resp['Data']['StatusStr'] == "success"):
            if (resp['Data']['Result']):
                #print(resp['Data']['Result'])
                return resp['Data']['Result']
            else:
                return "什么都没有听到呢"
        else:
            return get(Taskid)
    except TencentCloudSDKException as err:
        get(Taskid)

