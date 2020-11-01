from requests import post,get
from requests.auth import HTTPDigestAuth
import json
import argparse

arg_parser = argparse.ArgumentParser(description="UNISEC CLI <VAPIX>")


arg_parser.add_argument("protocol")
arg_parser.add_argument("ip")
arg_parser.add_argument("username")
arg_parser.add_argument("password")
arg_parser.add_argument("doorid")

arguments = arg_parser.parse_args()

headers = {
    "Content-Type": "application/json"
}

def learnPacs(protocol:str,ip:str,username:str,password:str)-> object: 
    """Lista todos os AxisID

    @params protocol:str                 https ou http\n
    @params ip:str                       172.16.2.102\n
    @params username:str                 root\n
    @params password:str                 ********453\n
    
    """
    payload = {
     "pacs:GetAccessPointInfoList":  {}  
    }
    response = post(protocol + "://" + username + ":" + password + "@"+ ip + "/vapix/pacs",data=json.dumps(payload),headers= headers, auth=HTTPDigestAuth(username, password))
    return response.json()

def opeDoor(protocol:str,ip:str,username:str,password:str,doorId:str): 
    """Abre porta AxisID

    @params protocol:str                 https ou http\n
    @params ip:str                       172.16.2.102\n
    @params username:str                 root\n
    @params password:str                 ********453\n
    @params doorId:str                   Axis-000000000:00000000.00000000 
    """
    payload = {
     "tdc:AccessDoor":  {
         "Token":doorId
        }  
    }
    response = post(protocol + "://" + username + ":" + password + "@"+ ip + "/vapix/doorcontrol",data=json.dumps(payload),headers= headers,auth=HTTPDigestAuth(username, password))
    print(response.text)




opeDoor(arguments.protocol,arguments.ip,arguments.username,arguments.password,arguments.doorid)