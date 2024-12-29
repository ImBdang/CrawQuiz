import requests as re
import json
import os

class GetQuestions:
    def __init__(self, config) -> None:
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.config = config
        self.url = "https://apps.ictu.edu.vn:9087/ionline/api/class-plan-activity-student-tests/"
        self.head = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9',
            'Authorization': config["token"],
            'Connection': 'keep-alive',
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
        self.params = {}

    def getQuestions(self, i, datavalue):
        self.params= {
            "select": "id,class_plan_activity_id,av,class_id,time,questions,course_id",
            "with": "test",
            "condition[0][key]": "id",
            "condition[0][value]": datavalue,
            "condition[0][compare]": "="
        }
        response = re.get(url=self.url, headers=self.head, params=self.params)

        if response.status_code == 200:
            response = response.text
            with open(f"{self.current_dir}/../../data/question.txt", "w",  encoding='utf-8') as f:
                f.write(response)
            return 1
        else:
            print(f"Request failed with status code {response.status_code}, trong file getquestions.py")
            print("Response content:", response.text,"\n\n")
            return -1
