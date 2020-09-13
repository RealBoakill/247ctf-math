#!/bin/python3

import re
import sys
import socket
import time

### Variables ###

host = sys.argv[1]
port = int(sys.argv[2])
pattern = re.compile("(\\d+)")

### End of Variables ###


### Functions ###

def connect(hn,p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hn,p))
    res = ""
    
    while True:
        data = s.recv(1024)
        if (not data):
            break
        res += data.decode()
        print(f"{res}")                                                                                                                                                                            
                                                                                                                                                                                                   
    for i in range(500):                                                                                                                                                                           
        nums = pattern.findall(res)                                                                                                                                                                
        print(f"Matched pattern of {pattern}: {nums}")                                                                                                                                             
        first = nums.pop()                                                                                                                                                                         
        second = nums.pop()                                                                                                                                                                        
        answer = first+second
        print(f"{i} answer: {answer}\n")

        s.send(answer.encode())
        data = s.recv(1024)
        res = data.decode()

        i = i+1

    print("Connection closed.")
    s.close()

### End of Functions ###

connect(host,port)
