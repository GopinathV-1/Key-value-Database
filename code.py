import json
import time
temp={}
x=input('Do you want to import master database and perform operation on it yes/no:')
if x=='yes':
    print('Loading master database in temp....')
    with open('master.json','r') as masteropen:
        data_load = json.load(masteropen)
    temp=data_load
    print('Loaded master database')
    print(temp)
d = temp 
def read(k):
    if k not in d:
        print("Error: This key is not present")
    else:
        b = d[k]
        if b[1]!=0:
            if time.time() < b[1]:
                stri = str(k)+":"+str(b[0])
                return stri
            else:
                print("ErrorL time to live of",k,"has expired")               
def create(key,value):
    temp[key]=value
def delete(key):
    temp[key]=0
print("Enter 1 for create , 2 for read , 3 for delete , e to exit , 5 to show data 1")
while(True):
    x=int(input())
    if(x==4):
        break
    if(x==1):
        key = input('Enter key for input')
        value=int(input('Enter its corresponding value'))
        create(key,value)
    if(x==2):
        key=input('Enter key to read')
        print(read(str(key)))
    if(x==3):
        key = input('Enter key')
        delete(key)
        print('key deleted')
    if(x==5):
        print(d)
    if x not in [1,2,3,4,5]:
        break
import json
temp=d
with open('temp.json','w') as fp:
    json.dump(temp,fp)
print('your database after operations are:')
print(temp)
x=int(input('is the first ever operation yes/no'))
if(x=='yes'):
    with open('master.join','w') as fp:
        json.dump(tepm,fp)
    print("thank you")
    exit()
x=input('Do you want to save this is the master dataset yes/no:')
if(x=='yes'):
    data={}
    import json
    with open('master.json','r') as fp:
        data = json.load(fp)
    master = dict(data)
    master.update(temp)
    with open('master.join','w') as fp:
        json.dump(master,fp)
print('All task done, Thanks')
