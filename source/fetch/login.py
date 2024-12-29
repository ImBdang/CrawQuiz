import requests as re
import json
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

class Login:
    def __init__(self, tk, mk) -> None:
        self.url = "https://apps.ictu.edu.vn:9087/ionline/api/login"
        self.head = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Host': 'apps.ictu.edu.vn:9087',
            'Origin': 'https://lms.ictu.edu.vn',
            'Referer': 'https://lms.ictu.edu.vn/',
            'Sec-CH-UA': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            'Sec-CH-UA-Mobile': '?0',
            'Sec-CH-UA-Platform': '"Linux"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'X-App-Id': '7040BD38-0D02-4CBE-8B0E-F4115C348003'
        }

        self.data=  {
            "username": tk,
            "password": mk
        }

    def login(self):
        res = re.post(url=self.url, headers=self.head, data=json.dumps(self.data))
        if res.status_code == 200:
            res = res.json()
            token = res.get("access_token")
            with open(f"{current_dir}/../../data/token.txt", "w") as f:
                f.write(str(token))
                print("Login complete\n")
        else:
            print(f"Login failed, " + str(res.status_code))
            exit()
    
    def getVer(self, config):
        urlVer = "https://apps.ictu.edu.vn:9087/ionline/api/configs/"
        paramsVer = {
            "limit": 1,
            "select": "value,title",
            "condition[0][key]": "config_key",
            "condition[0][value]": "__APP_VERSION",
            "condition[0][compare]": "="
        }
        headersVer = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
            "Authorization": config["token"],
            "Connection": "keep-alive",
            "Host": "apps.ictu.edu.vn:9087",
            # "If-None-Match": 'W/"9b-ZCpcVAKZs1i3ddPYDY7gN0Tz9MM"',
            "Origin": "https://lms.ictu.edu.vn",
            "Referer": "https://lms.ictu.edu.vn/",
            'Sec-CH-UA': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            "Sec-CH-UA-Mobile": "?0",
            'Sec-CH-UA-Platform': '"Linux"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            "X-APP-ID": "7040BD38-0D02-4CBE-8B0E-F4115C348003"
        }

        res = re.get(url=urlVer, headers=headersVer, params=paramsVer)
        
        if res.status_code == 200:
            res = res.json()
            version = res["data"][0]["title"]
            with open(f"{current_dir}/../../data/ver.txt", "w") as f:
                f.write(str(version))
                print(f"Version is {version}\n")
        else:
            print(f"Version failed, " + str(res.status_code))
            exit()
        
    def getInfo(self, config, hocky):
        headInfo = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
            "Authorization": config["token"],
            "Connection": "keep-alive",
            "Host": "apps.ictu.edu.vn:9087",
            #"If-None-Match": 'W/"260-LiQZXbJfrCdLfMuAk+ezDX0uiPo"',
            "Origin": "https://lms.ictu.edu.vn",
            "Referer": "https://lms.ictu.edu.vn/",
            'Sec-CH-UA': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            "Sec-CH-UA-Mobile": "?0",
            'Sec-CH-UA-Platform': '"Linux"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            "X-APP-ID": "7040BD38-0D02-4CBE-8B0E-F4115C348003"
        }

        urlInfo = "https://apps.ictu.edu.vn:9087/ionline/api/class-students/"
        urlMng = "https://apps.ictu.edu.vn:9087/ionline/api/class/"

        paramsInfo = {
            "limit": 1000,
            "paged": 1,
            "select": "namhoc,hocky,class_id",
            "condition[0][key]": "student_id",
            "condition[0][value]": config["Student_id"],
            "condition[0][compare]": "="
        }
        paramsMng = {
            "with": "managers"
        }

        response = re.get(url=urlInfo, headers=headInfo, params=paramsInfo)
        if (response.status_code == 200):
            print("Lay thong tin mon hoc thanh cong\n\n")
            response = response.json()
            a = []
            c = []
            for i in response["data"]:
                if (i["hocky"] == hocky):
                    a.append(i["class_id"])
            b = []
            for i in a:
                nurlMng = urlMng + str(i)
                res = re.get(url=nurlMng, params=paramsMng, headers=headInfo)
                if (res.status_code == 200):
                    res = res.json()
                    b.append(res["data"]["name"])
                    c.append(res["data"]["course_id"])
                else:
                    print(f"Loi xay ra tai class id = {i}")
                    exit()
            return a,b,c

        else:
            print("Co loi khi lay thong tin lop hoc\n\n")
            exit()

        

    

