import os
import json

def runMerge(chekcpoint, config):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_data = ""
    merge_data = ""

    root_dir = f"{current_dir}/../../data/Questions.txt"
    merge_dir = f"{current_dir}/../../data/question.txt"

    if chekcpoint == False:
        with open(root_dir, "w", encoding='utf-8') as f:
            f.write("")
        with open(merge_dir, "r",  encoding='utf-8') as f:
            root_data = f.read()
    else:
        with open(root_dir, "r",  encoding='utf-8') as f:
            root_data = f.read()
    
    
    with open(merge_dir, "r",  encoding='utf-8') as f:
        merge_data = f.read()


    root_data = json.loads(root_data)
    merge_data = json.loads(merge_data)

    Rdict = dict()
    Mdict = dict()

    data = root_data["data"][0]["test"]

    for i in data:
        Rdict[i["id"]] = i

    data = merge_data["data"][0]["test"]

    for i in data:
        Mdict[i["id"]] = i

    Rdict.update(Mdict)
    test = []
    sluong = 0
    for k,i in Rdict.items():
        if ((len(i["answer_option"]) >0) and config["av"] != 1):
            test.append(i)
            sluong = sluong + 1
        elif (config["av"] == 1):
            test.append(i)
            sluong = sluong + 1

    root_data["data"][0]["test"] = test
    root_data = json.dumps(root_data)

    with open(root_dir, "w",  encoding='utf-8') as f:
        f.write(root_data)

    print(f"So luong cau hoi hien tai la: {sluong}")
    
