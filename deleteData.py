#coding:utf-8

import requests
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class Tools:

    def DeleteData(self, _account_list, _url):

        for account in _account_list:
            new_url = _url + account
            print new_url
            response = requests.get(new_url)
            print(response.text)
    
    def string_to_list(self, _tag):
        
        result = _tag.split(',')
        print result
        return result

if __name__ == '__main__':

    if  len(sys.argv) <= 1:
        print "please input user id, multiple users separated by commas"
        sys.exit()

    account = sys.argv[1]
        
    _Tools = Tools()
    account_list =_Tools.string_to_list(account)
    url = "http://10.111.203.203:8888/student/progress/clear?uid="
    _Tools.DeleteData(account_list, url)