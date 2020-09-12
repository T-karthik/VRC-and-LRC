#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def vrceve():
    ##sender
    a = list(map(int, input("enter your binary string")))
    count = 0
    for i in a:
        if i == 1:
            count += 1
    if count % 2 == 0:
        a.append(0)
    else:
        a.append(1)
    print("At sender side:", a)
    ### receiver side
    b = list(map(int, input("enter your received binary string")))
    count1 = 0
    count2 = 0
    if len(a) == len(b):
        for i in b:
            if i == 1:
                count1 += 1
        if count1 % 2 == 0:
            b.append(0)
        else:
            b.append(1)
        print("before checking at receiver side", b)

        if b[len(b) - 1] == 1:
            print("error data received")
        else:
            # del b[len(b)-1]
            # del b[len(b)-2]
            # del a[len(a)-1]
            for i in range(len(b) - 2):
                if a[i] == b[i]:
                    # print("received string is correct",b[:len(b)-2])
                    count2 += 1
                # else:
                #   print("Received string is not correct")
        if count2 == len(b) - 2:
            print("received string is correct and exact data is", b[:len(b) - 2])
        else:
            print("received data is not correct")
    else:
        print("received string length is not equal to sent string length")


#vrceve()


def vrcodd():
    # sender side
    a = list(map(int, input("enter your binary string")))
    count = 0
    for i in a:
        if i == 1:
            count += 1
    if count % 2 == 0:
        a.append(1)
    else:
        a.append(0)
    print("At sender side:", a)
    ### receiver side
    b = list(map(int, input("enter your received binary string")))
    count1 = 0
    count2 = 0
    if len(a) == len(b):
        for i in b:
            if i == 1:
                count1 += 1
        if count1 % 2 == 0:
            b.append(1)
        else:
            b.append(0)
        print("before checking at receiver side", b)

        if b[len(b) - 1] == 1:
            print("error data received")
        else:
            # del b[len(b)-1]
            # del b[len(b)-2]
            # del a[len(a)-1]
            for i in range(len(b) - 2):
                if a[i] == b[i]:
                    # print("received string is correct",b[:len(b)-2])
                    count2 += 1
                # else:
                #   print("Received string is not correct")
        if count2 == len(b) - 2:
            print("received string is correct and exact data is", b[:len(b) - 2])
        else:
            print("received data is not correct")

    else:
        print("received string length is not equal to sent string length")


#vrcodd()

def lrceve():
    a=int(input("enter no of data to be sent"))
    b=int(input("enter length of each data to be sent"))
    x=[]
    for i in range(0,a):
        y = list(map(int, input("enter your binary string")))
        x.append(y)

    print(x)
    #count =0
    y = []
    for i in range(0,b):
        count=0
        for j in range(0,a):
            if x[j][i]==1:
                count+=1
        if count % 2 == 0:
            y.append(0)
        else:
            y.append(1)
    x.append(y)

    #receiver side
    p=[]
    for i in range(0,a+1):
        q = list(map(int, input("enter your received binary string")))
        p.append(q)
    #count = 0
    q = []
    for i in range(0, b):
        count=0
        for j in range(0, a):
            if x[j][i] == 1:
                count += 1
        if count % 2 == 0:
            q.append(0)
        else:
            q.append(1)
    p.append(q)
    print(p)
    print(x)
    print(x[a])
    print(p[a])

    if x[a] ==p[a]:
        print("data correctly received")
    else:
        print("wrong data received")



#lrceve()


def lrcodd():
    a = int(input("enter no of data to be sent"))
    b = int(input("enter length of each data to be sent"))
    x = []
    for i in range(0, a):
        y = list(map(int, input("enter your binary string")))
        x.append(y)

    print(x)
    #count = 0
    y=[]
    for i in range(0, b):
        count=0
        for j in range(0, a):
            if x[j][i] == 1:
                count += 1
        if count % 2 == 0:
            y.append(1)
        else:
            y.append(0)
    x.append(y)
    print(x)

    # receiver side

    p = []
    for i in range(0, a + 1):
        q = list(map(int, input("enter your received binary string")))
        p.append(q)
    #count = 0
    q=[]
    for i in range(0, b):
        count=0
        for j in range(0, a):
            if x[j][i] == 1:
                count += 1
        if count % 2 == 0:
            q.append(1)
        else:
            q.append(0)
    p.append(q)
    print(x)
    print(p)
    if x[a] == q:
        print("data correctly received")
    else:
        print("wrong data received")

while True:
    x=int(input("choose your options 1-vrc, 2-Lrc, 3-Exit"))
    y=int(input("choose 1 for  even parity and 2 for odd parity"))
    if x==1 and y==1:
        vrceve()
    elif x==1 and y==2:
        vrcodd()
    elif x==2 and y==1:
        lrceve()
    elif x==2 and y == 2:
        lrcodd()
    elif x==3:
        break
    else:
        print("choose your option correctly")


# In[ ]:




