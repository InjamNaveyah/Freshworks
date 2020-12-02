import threading 
from threading import*
import time

dic={} #'dic' is the dictionary in which we store data

#for create operation 
def create(key,value,timeout=0):
    if key in dic:
        print("This key already exists,Try new one") 
    else:
        if(key.isalpha()):
            if len(dic)<(1024*1020*1024) and value<=(16*1024*1024): #for file size < 1GB & JsonObject < 16KB 
                if timeout==0:
                    la=[value,timeout]
                else:
                    la=[value,time.time()+timeout]
                if len(key)<=32: #for input key capped at 32chars
                    dic[key]=l
            else:
                print("Memory limit is exceeded")
        else:
            print("Invalid key_name")

#for read operation
            
def read(key):
    if key not in dic:
        print("Key does not exist in database") 
    else:
        s=dic[key]
        if s[1]!=0:
            if time.time()<s[1]: 
                stri=str(key)+":"+str(s[0]) 
                return stri
            else:
                print("key has expired") 
        else:
            stri=str(key)+":"+str(s[0])
            return stri

#for delete operation

def delete(key):
    if key not in dic:
        print("key does not exist in database.") 
    else:
        s=dic[key]
        if s[1]!=0:
            if time.time()<s[1]: 
                del dic[key]
                print("key is successfully deleted")
            else:
                print("key has expired")
        else:
            del dic[key]
            print("key is successfully deleted")


#for modify operation 

def modify(key,value):
    s=dic[key]
    if s[1]!=0:
        if time.time()<s[1]:
            if key not in dic:
                print("key does not exist in database") 
            else:
                la=[]
                la.append(value)
                la.append(s[1])
                dic[key]=l
        else:
            print("key has expired") 
    else:
        if key not in dic:
            print("key does not exist in database")
        else:
            la=[]
            la.append(value)
            la.append(b[1])
            dic[key]=l