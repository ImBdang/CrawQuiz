import argparse
from source.config import make_config
from source.fetch.getdata import GetData
from source.fetch.getquestions import GetQuestions
from source.fetch.login import Login
from source.merge.merge import runMerge
import time
import os
import getpass
import subprocess


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id_sv", type=int, default=0) 
    parser.add_argument("--week", type=int, default=0)
    parser.add_argument("--course", type=int, default=1)
    parser.add_argument("--loop", type=int, default=5)
    parser.add_argument("--speed", default=5, type=int)
    parser.add_argument("--checkpoint", default=False, type=bool)
    parser.add_argument("--av", type=int, default=0)
    return parser

def run(config, args):
    getdata = GetData(args.id_sv, config)
    getques = GetQuestions(config)

    for i in range(0, config["loop"]):
        print("\n===========================================")
        dataDe = getdata.layDe()
        if dataDe == -1:
            print("Sinh de that bai")
            break
        else:
            print(f"Sinh de thanh cong, ma de la: {dataDe}")
            t = getques.getQuestions(i, dataDe)
            if t == -1:
                print("Lay cau hoi that bai")
                break
            else:
                runMerge(args.checkpoint, config)
                if (args.checkpoint == False):
                    args.checkpoint = True
                print(f"No.{i+1} get complete")
                print("===========================================\n\n\n")
                if i < (config["loop"]-1):
                    time.sleep(args.speed)
                
def menu(class_name):
    print("Danh sach cac mon hoc la: \n")
    index = 1
    for i in class_name:
        print(f"\t{index}. {i}\n")
        index += 1
    print(f"\t0. Exit\n\n")

def preProcess(course, parser, args, config, class_id, student_id, c):
    week = input("Nhap tuan muon lay: ")
    loop = input("Nhap so lan muon lay: ")
    config = make_config(args, class_id[c-1], student_id)
    args = parser.parse_args([
        "--id_sv", str(config["Student_id"]),
        "--loop", loop,
        "--week", week,
        "--course", str(course)
    ])
    # print("args")
    # for arg, value in vars(args).items():

    #     print(f"{arg}: {value}")
    config = make_config(args, class_id[c-1], student_id)
    # print("config items")
    # for key, value in config.items():
    #     print(f"{key}: {value}")

    run(config, args)
    while True:
        exitCode = input("Co muon tiep tuc lay khong ? [y/n]: ")
        exitCode = exitCode.lower()
        if (exitCode == "n"):
            break
        elif (exitCode == "y"):
            loop = input("Nhap so lan lay: ")
            args = parser.parse_args([
                "--id_sv", str(config["Student_id"]),
                "--loop", loop,
                "--course", str(course),
                "--week", week,
                "--checkpoint", "True"
            ])
            config = make_config(args, class_id[c-1], student_id)
            run(config, args)
 


if __name__ == "__main__":
    subprocess.Popen(
        ["python", "-m", "http.server", "8080"],
        stdout=subprocess.PIPE,  
        stderr=subprocess.PIPE 
    )
    hocky = 2
    parser = make_parser()
    args = parser.parse_args()
    tk = input("\nVui long dang nhap\n\nTai khoan: ")
    mk = getpass.getpass("Mat khau: ")
    log = Login(tk, mk)
    student_id = log.login()
    config = make_config(args, 0, student_id)
    log.getVer(config)
    class_id, class_name, course_id = log.getInfo(config, hocky)
    while True:
        menu(class_name)
        c = input("Chon mon hoc cua ban: ")
        c = int(c)
        if (c == 0):
            exit()
        elif (c > len(course_id)):
            print("Nhap khong hop le, vui long nhap lai")
        else:
            preProcess(course_id[c-1], parser, args, config, class_id, student_id, c)

    

    
    
 

