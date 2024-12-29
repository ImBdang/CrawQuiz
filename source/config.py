import os
from datetime import datetime
current_dir = os.path.dirname(os.path.abspath(__file__))

def make_config(args, class_id, student_id):
   
    config = dict()

    # for head
    with open(f"{current_dir}/../data/token.txt", "r") as f:
        config["token"] = f.read()
        config["token"] = "Bearer " + config["token"]
    with open(f"{current_dir}/../data/id.txt", "r") as f:
        config["Xid"] = f.read()


    #for data and pramas
    config["time"] = 0
    config["Course_id"] = args.course
    config["Class_id"] = class_id
    config["Student_id"] = student_id
    config["ClassAc_id"] = 0
    config["week"] = args.week
    config["av"] = args.av

    #config["note"] = "26/12/2024 17:13:00v3.1.15"

    #loop
    config["loop"] = args.loop

    return config


