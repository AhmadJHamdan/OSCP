#!/usr/bin/python3
import socket
import sys

arguments = sys.argv

if arguments[1] == "-h":
    print("-u: search for user")
    print("-h: get help")
    print("-i: add ip address")
    print("-f: add file name")
    exit(0)

if len(sys.argv)!=5:
    print("[+]Usage: ./user-smtp-enum.py -i <IP> -u <user>")
    exit(0)

ip_address = arguments[arguments.index("-i")+1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect((ip_address,25))
banner = s.recv(1024)

def checkUser(socket_name, user_name):
    socket_name.send(f"vrfy {user_name}\r\n".encode())
    result = s.recv(1024).decode()
    print(f"User: {user_name}\nResult:\n{result}")
    
if "-u" in arguments:
    user = arguments[arguments.index("-u") + 1]
    checkUser(s,user)
elif "-f" in arguments:
    file_name = arguments[arguments.index("-f") + 1]
    with open(file_name) as f:
        for line in f:
            f_user = line.strip()
            checkUser(s,f_user)    
else:
    print("Wrong Entry!!")
    exit(0)
 
s.close()
print("The End ... Goodbye!")
