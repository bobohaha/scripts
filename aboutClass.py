# coding:utf-8
import os
import sys
import json
import time
import requests
import datetime
import hashlib
reload(sys)  
sys.setdefaultencoding('utf8')  

class Tools:

    def run(self, _phone, _password):
        print "Login: "
        user_info = self.get_user_info(_phone, _password)
        print "About Class: "
        self.aboult_class_sh(user_info)

    def aboult_class_sh(self, _data):
        timeStart = self.get_current_Zore_times()
        timeEnd = timeStart + 84600
        timeNow = self.get_current_times()
        while timeStart <= timeEnd:
            timeStart += 1800
            if timeStart > timeNow:
                format_time = self.get_timestamp_format_times(timeStart)
                print "can about class, time is: " + format_time
                _data['stamp'] = timeStart
                dataJson = self.get_dick_to_json(_data)
                tag = "\' "
                commandDataFormat = tag + str(dataJson) + tag
                result = os.popen('sh ./run.sh ' + commandDataFormat).read()
                result_json = json.loads(result)
                if result_json['ret'] != 1:
                    print result_json['msg']
                    if '无可用课时' in result_json['msg']:
                        break

            else:
                print "class time is end, next: "
                continue
        pass
    
    def get_user_info(self, _phone, _password):
    
        response = self.login(_phone, _password)
        uid = self.get_uid(response)
        token = self.get_token(response)
        user_info = {
            "h_ts": 0,
            "h_m": uid,
            "token": token,
            "kid": 306537937891354
        }
    
        return user_info

    def get_current_Zore_times(self):
        today = datetime.date.today()
        zore_times = int(time.mktime(today.timetuple()))
        return zore_times
        
    def get_current_times(self):
        return int(time.time())
    
    def get_timestamp_format_times(self, _timestamp):
        timeArray = time.localtime(_timestamp)
        format_time = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
        return format_time

    def get_dick_to_json(self, _dick_data):
        json_data = json.dumps(_dick_data, separators=(',', ":"))
        return json_data
    
    def get_token(self, _response):
        token = _response["data"]["token"]
        return token
    
    def get_uid(self, _response):
        uid = _response["data"]["member_info"]["id"]
        return uid
    
    def login(self, _phone, _password):
        url = "https://m.ipalfish.com/klian/account/login"
        pw = self.get_pw(_password)
        request_param = {
            "phone": _phone,
            "pw": pw,
            "area": "86",
            "cate": 1
        }
        
        response = requests.post(url, data=json.dumps(request_param))
        if response.status_code == 200:
            response_json = response.json()
            if response_json['ret'] != 1:
                print response_json['msg']
                sys.exit()
            print "Login success"
        return response_json
   
    def get_pw(self, pw):
        pw = str(pw)
        m = hashlib.md5()
        b = pw.encode(encoding='utf-8')
        m.update(b)
        pw_md5 = m.hexdigest()
        return pw_md5[:16]
        
if __name__ == '__main__':
    
    phone = sys.argv[1]
    password = sys.argv[2]
    _AboutClass = Tools()
    _AboutClass.run(phone, password)
    # _AboutClass.login(phone, password)