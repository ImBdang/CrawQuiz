import requests as re
import json
import os
from datetime import datetime


current_dir = os.path.dirname(os.path.abspath(__file__))

def note():
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    ver1 = ""
    ver1 = ver()
    note = current_time + ver1
    return note

def ver():
    with open(f"{current_dir}/../../data/ver.txt", "r") as f:
        version = f.read()    
    return version

class GetData:
    def __init__(self, id_sv, config) -> None:
        self.url = f"https://apps.ictu.edu.vn:9087/ionline/api/class-plan-activity-student-tests/sinhde/{id_sv}"
        self.gotData = 0
        self.head = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9',
            'Authorization': config["token"],
            'Connection': 'keep-alive',
            'Content-Length': '207',
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
            'X-App-Id': config["Xid"]
        }

        self.note = note()

        self.data = {
            "class_plan_activity_id": config["ClassAc_id"],
            "av": config["av"],
            "course_id": config["Course_id"],
            "class_id": config["Class_id"],
            "student_id": config["Student_id"],
            "passed": 0,
            "passing_point": 80,
            "env": "web",
            "week": config["week"],
            "with_correct_answers": 0,
            "time": config["time"],
            "note": self.note 
        }

    def layDe(self):

        response = re.post(url=self.url, headers=self.head, data=json.dumps(self.data))

        if response.status_code == 200:
            response = response.json()
            self.gotData = response.get("id")
        else:
            print(f"Request failed with status code {response.status_code}, trong file getdata.py")
            print("Response content:", response.text,"\n\n")
            self.gotData = -1
        return self.gotData
        
