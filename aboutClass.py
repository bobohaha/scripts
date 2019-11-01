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
        print "get user info:"
        user_info = self.get_user_info(_phone, _password)
        print "about class:"
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
                print commandDataFormat
                os.system('sh ./run.sh ' + commandDataFormat)
                break

            else:
                print "class time is end"
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
        print zore_times
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
        token = _response.json()["data"]["token"]
        print token
        return token
    
    def get_uid(self, _response):
        uid = _response.json()["data"]["member_info"]["id"]
        print uid
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
        return response
   
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