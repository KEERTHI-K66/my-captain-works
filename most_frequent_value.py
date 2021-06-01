def frequency(string):
    dic={}
    for val in string:
        dic.setdefault(val,0)
        dic[val]+=1
    dic={k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}
    for k, v in reversed(dic.items()):
        print(k,"=", v,end=' ')

string=input("Please enter a string")
frequency(string)
