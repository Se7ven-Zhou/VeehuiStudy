# coding:utf-8

import requests
import HuShi.Config.JiraConfig

class KeyIssue:

    def __init__(self):

        self.url = HuShi.Config.JiraConfig.url
        self.headers = HuShi.Config.JiraConfig.headers

    def commit(self,api,params,response,check,n,sql = None):
        if n == 0:
            summary = "【BUG】[" + api + "]该接口状态码错误"
            description = "【参数】\n" + str(params) + "\n" + "【返回结果】\n" + str(response) + "\n" + "【正确状态】\n" + str(check)
        else:
            summary = "【BUG】[" + api + "]该接口返回数据错误"
            description = "【参数】\n" + str(params) + "\n" + "【返回结果】\n" + str(response) + "\n" + "【正确数据】\n" + str(check) +"\n【参考SQL】\n"+ str(sql)

        params = {"pid": "10005",
                       "issuetype": 10004,
                       "atl_token": "BQGC-6ARB-IN3M-2T50_cea041428c5f8cf318993c1f475bf2d6c28ee790_lin",
                       "formToken": "fc5df7e565d1da57a4250186cb3d422e6bcf96fe",
                       "summary": summary,
                       "description": description,
                       "priority": 3,
                       "environment": "",
                       "dnd-dropzone": "",
                       "issuelinks	issuelinks": "",
                       "issuelinks-linktype": "blocks",
                       "assignee": "zhouj",
                       "customfield_10101": "",
                       "fieldsToRetain": "project",
                       "fieldsToRetain": "issuetype",
                       "fieldsToRetain": "components",
                       "fieldsToRetain": "fixVersions",
                       "fieldsToRetain": "priority",
                       "fieldsToRetain": "labels",
                       "fieldsToRetain": "environment",
                       "fieldsToRetain": "versions",
                       "fieldsToRetain": "issuelinks",
                       "fieldsToRetain": "assignee",
                       "fieldsToRetain": "customfield_10102",
                       "fieldsToRetain": "customfield_10101}"
                       }
        requests.post(self.url,params,headers=self.headers)

if __name__ == "__main__":
    a="api"
    b='{"aa":"aa"}'
    c= '{"code":1}'
    d= '{"key":1}'
    KeyIssue().Commit(a,b,c,d,0)