#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import sys
import requests
import random
import json
import time
requests.packages.urllib3.disable_warnings()

UA="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36"
user_cookie={
"mpfwsx":"BAIDUID=B39B68B741F2079143F808539FDCCF3F:FG=1; FP_UID=4e8d3ec5a9356a67ba1c951bb769a27b; BDUSS=1JjVjRvbmlGU0N-ai0tT0IzVUQ1bzA0S2N4d3pvRWRoTTJFSXFzQ0NzU1NJYWxhQVFBQUFBJCQAAAAAAAAAAAEAAABcEL8nbXBmd3N4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJKUgVqSlIFaR",
"mengpanfei":"BDUSS=pgElm1Xf5gIBxZZDPwI4Yw==; OPENBDUSS=AAAAEAAAALL3MFJLitAN1WRaTuJzLPoQjSVQmnALAUsRns5VflcWEPdjBvjtiO5ruGIayHC1INQDuA0YMnhcRo6hANAEXDRR8Pm8WeUPQJL7cY5W-EsyLkHAwYrhWVdzVbx1mrOZ-oDTaMz1FESlUq3fLnYQu5jTEGL3ogVLPZHObfAonZZgAQ; STOKEN=bd7912d94742c40af1e24867250760c5bb3c3decb8247a7760cdf88aff8f4e52; Hm_lvt_2a9b55018981a1911dd3914ca3f9bcf6=1589687943,1589687972,1589693967,1589694788; Hm_lpvt_2a9b55018981a1911dd3914ca3f9bcf6=1589711422",
"leleyi":'BAIDUID=F588BFA169DCB675202758236DC1EF67:FG=1; FP_UID=d3f4458488a0486582dba99131f4bd01; BDUSS=0JCalJ5OW5sSUFObXBqWlFibFF5RW95TTQ3ZHNNYzg1MVlHSjFkWnhZQ25Jc3hhQVFBQUFBJCQAAAAAAAAAAAEAAAD7u37OAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKeVpFqnlaRaS',
"yophy":"BAIDUID=4EE5E3EBE7DCE13EEF62D288102031AC:FG=1; FP_UID=3fdf683dad85310b8189c693f8819a2a; BDUSS=2J-WTFvcUhWNkFEUVpsNmloaXFiZklKM1Nld21rSkNpQnBCTXB-ZnV2bE5QYzlhQVFBQUFBJCQAAAAAAAAAAAEAAACqJOU~0-rOtLn9yKXM7NLRx-cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE2wp1pNsKdaV",
"mengxiao":"BAIDUID=C72CE2E02361A73C0A088A2BE3B38D17:FG=1; FP_UID=dba13a02e9faabb692be1a53ee3cc581; BDUSS=FEeGxsTXFmZDhGc0xnbGVGMTl6aFNGRGo2eFlSOEpZQkVKMHp5b1E4ZjdsNnBhQVFBQUFBJCQAAAAAAAAAAAEAAACmB1ycAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPsKg1r7CoNaaT",
"denghui":"BAIDUID=71477616300E1BFB994F6CC6B9BAFE2F:FG=1; BDUSS=TQ3b1l5TGxjR0ZlWGpmUzhmVFkwdEQzT0lPb3FNRTBBcXQ4TmRnM1pyRFVXNmxhQVFBQUFBJCQAAAAAAAAAAAEAAAAg-zolzP3LtbXGxd3U2rG8xdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANTOgVrUzoFaM; BIDUPSID=3E3EBC1C38AB7F72B2845FAC1283E94B; FP_UID=c74f3f097548643b9bfa2e4b8dc71e62; PSTM=1506072888",
"lvluo":"BAIDUID=6E777D3AD9AD4F2E7AF04796EA342235:FG=1; BDUSS=FxUWdqZk5sWTllMUVISnpVeU5wMFMzbEowOFYtOWZoQ1dnQnA3VmtRRnRLTWhhQVFBQUFBJCQAAAAAAAAAAAEAAAA6OkHPs6y8ttDCz8rCzMLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG2boFptm6BaWT; BIDUPSID=6E777D3AD9AD4F2E7AF04796EA342235; FP_UID=9389b1ca8dadc2158e4dc69b1bf9923a; H_PS_PSSID=1456_21119_17001_22157; PSTM=1520474726",
"yophy2":"BAIDUID=2C8ADEB40527D0C7EDEB1267F8EDBF8F:FG=1; FP_UID=d25e98c51739d874874e3987475b4232; BDUSS=d3TW1wMjVQQWZGSTJNRmlDeDZSYzV0fnAxcEdkSTM0eVZhLUhVNWxhdUd-Y3BhQUFBQUFBJCQAAAAAAAAAAAEAAAC~g07PAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIZwo1qGcKNaTl",
}


def get_httpheader(username="mengpanfei",refer='https://pet-chain.baidu.com/'):
    if username=="random": 
        username=random.choice(list(user_cookie.keys()))
    if username=="UA": username="mengpanfei"
    Cookie=user_cookie.get(username)
    headers={'Cookie':Cookie,'Referer':refer,'User-Agent':UA,'accept':'application/json',
             'Pragma':'no-cache','Cache-Control':'no-cache','content-type':'application/json'}
    return headers


#带重试版本
def get_url_data_bak(url,param,headers,MaxTry=2):
    r=None
    while MaxTry>0:
        try:
            r=requests.post(url,data=param,headers=headers,verify=False)
            if r.json()['errorNo'] in ('00',"30001","30008"): #30001狗状态改变不能操作，30008下架太频繁不能操作
                break
        except Exception as ex:
            print(ex)
            pass
        MaxTry-=1
        time.sleep(0.54)
    return r


##不带重试，防止出错没人管而无限重试
def get_url_data(url,param,headers,MaxTry=2):
    r=requests.post(url,data=param,headers=headers,verify=False)
    return r


## 获取狗窝里的狗
def get_my_dogs(username="mengpanfei"):
    dogs=[]
    url="https://pet-chain.duxiaoman.com/data/user/pet/list"
    headers=get_httpheader(username)
    pageNo=1
    totalCount=10
    while True:
        if pageNo * 10 > totalCount: break
        param={"pageNo":pageNo,"pageSize":10,"rareDegree":"null","generation":"null","requestId":int(time.time() * 1000),"appId":1,"tpl":"","timeStamp":"null","nounce":"null","token":"null","phoneType":"android"}
        r=requests.post(url,data=json.dumps(param),headers=headers,verify=False)
#         print( r.json()["errorNo"])
        if r.json()["errorNo"] != "00": # 20013 太频繁;
            print(r.json())
            sys.exit(2)
        jr=r.json()["data"]
        totalCount=jr["totalCount"]
        pageNo+=1
        for dog in jr["dataList"]:
            dogs.append([dog["id"].zfill(8),dog["petId"],dog["rareDegree"],dog["generation"],dog["shelfStatus"],dog["chainStatus"],dog["amount"], funny_type(dog["id"])])
        time.sleep(2)
    return dogs


## 狗号的靓号类型
def funny_type(_id):
    id=_id.zfill(8)
    
    #生日号
    if id[:4]>="1900" and id[:4]<="2050":
        #大月
        if id[4:6] in ("01","03","05","07","08","10","12",) \
            and id[6:]>="01" and id[6:]<="31" : 
            return "birth_%s_%s"%(id[:4],365*20)
        #小月
        if id[4:6] in ("04","06","09","11",) \
            and id[6:]>="01" and id[6:]<="30" : 
            return "birth_%s_%s"%(id[:4],365*20)
        #2月
        if id[4:6]=="02" \
            and id[6:]>="01" and id[6:]<="28" :
            return "birth_%s_%s"%(id[:4],365*20) #平
            if int(id[:4])%4==0 and int(id[:4])%100!=0 \
                and id[6:]=="29":
                return "birth_%s_%s"%(id[:4],10) #润
            if id=="20000229": #年份能被400整除
                return "birth_%s_%s"%(id[:4],1) #润
            
    ############ start 纯号和飞机，重合的可能性很大。 注意收到的特殊号
    if id.endswith("00544") or id.endswith("44944") :
        return "haha_%s_%s"%(id[-5:],1000) #12300544
    #复制  
    if id[:4]==id[4:]: 
        if id[0:2]==id[2:4]:
            return "copy_%s_%s"%(id[:2],100) #12121212 #糖葫芦
        return "copy_%s_%s"%(id[:4],10000*3) #12341234
    #对称
    if id[:4]==id[4:][::-1]: return "huiwen_%s_%s"%(id[:4],10000*3) #12344321
    #4对  不放这里，会被2、4截断。。。
    if id[0]==id[1] and id[2]==id[3] and id[4]==id[5] and id[6]==id[7]:
        return "tail2222_%s%s%s%s_%s"%(id[-8],id[-6],id[-4],id[-2],1000*2) #11224444

    #纯号
    idc=list(id);idc.sort()
    idc_count={}
    for c in id:
        idc_count[c]=idc_count.get(c,0)+1
    if len(idc_count)==1:
        return "single_%s_%s"%(idc[0],10) #
    elif len(idc_count)==2:
        if "0" in id:
            return "single0_%s_%s"%(idc[-1],2560) #03000000
        return "double_%s%s_%s"%(idc[0],idc[-1],2560*3) #21221212
    #飞机 火箭
    lian41=lian42=lian31=lian32=-1
    for c in range(10):
        if str(c)*4 in id:
            if lian41==-1: lian41=c; 
            else: lian42=c
        elif str(c)*3 in id:
            if lian31==-1: lian31=c; 
            else: lian32=c
    # print lian41,lian42,lian31,lian32
    if lian42>=0:
        return "roket_%s%s_%s"%(lian41,lian42,100) # 11112222  #实际上会被纯2截去
    if lian32>=0:
        if id[0]==id[1] and id[0]==id[2]:
            if id[-1]==id[-2] and id[-1]==id[-3]:
                if id[3]==id[4]:
                    return "fly121_%s%s_%s"%(id[0],id[-1],1000*2) # 11122444
                return "fly101_%s%s_%s"%(id[0],id[-1],10000*20) # 11123444
            if id[3]==id[4] and id[3]==id[5]:
                if abs(int(id[0])-int(id[3]))==1:
                    return "fly112_%s%s_%s"%(id[0],id[3],1000) # 11122237
                if id[6]==id[7]:
                    return "fly112_%s%s_%s"%(id[0],id[3],1000*2) # 11144433
                return "fly110_%s%s_%s"%(id[0],id[3],10000*10) # 11122234
        if id[-1]==id[-2] and id[-1]==id[-3]:
            if id[-4]==id[-5] and id[-4]==id[-6]:
                if abs(int(id[3])-int(id[6]))==1:
                    return "fly211_%s%s_%s"%(id[3],id[6],1000) # 14222333
                if id[0]==id[1]:
                    return "fly211_%s%s_%s"%(id[3],id[6],1000*2) # 11666444
                return "fly011_%s%s_%s"%(id[3],id[6],10000*1) # 12666444
        return "fly_%s%s_%s"%(lian31,lian32,10000*10) # 12223444
    if lian41>=0 and lian31>=0:
        return "fly2_%s%s_%s"%(lian31,lian41,1000*2) # 12223333
    ############# end 纯号和飞机
    
    #狮子号
    if id[-1]==id[-2] and id[-1]==id[-3] and id[-1]==id[-4]:
        if id[-1]==id[-5]:
            if id[-1]==id[-6]:
                if id[-1]==id[-7]:
                    return "tail7_%s_%s"%(id[-1],100) # 12222222
                return "tail6_%s_%s"%(id[-1],1000) # 12333333
            if id[0]==id[1]:
                if id[0]==id[2]:
                    return "tail35_%s%s_%s"%(id[0],id[-1],100) # 12333333
                return "tail205_%s%s_%s"%(id[0],id[-1],1000) # 11233333
            return "tail5_%s_%s"%(id[-1],10000) # 10344444
        if id[-5]==id[-6]:
            if id[0]==id[1]:
                return "tail224_%s%s%s_%s"%(id[-8],id[-6],id[-4],1000) #11334444
            return "tail24_%s_%s"%(id[-4],10000) #12334444
        else:
            if id[0]==id[1]:
                if id[0]==id[2]:
                    return "tail304_%s%s_%s"%(id[0],id[-1],1000) # 11123333
                return "tail204_%s%s_%s"%(id[0],id[-1],10000*2) # 11234444
            return "tail4_%s_%s"%(id[-4],100000) #10345555
    
    #豹子、葫芦
    if id[-1]==id[-2] and id[-2]==id[-3]:
        if id[-4]==id[-5]:
            if id[-5]==id[-6]:
                return "tail33_%s%s_%s"%(id[-4],id[-1],10000) #12333444
            elif id[-7]==id[-6]:
                return "tail223_%s%s%s_%s"%(id[-6],id[-4],id[-1],10000*10) #12233444
            else:
                if id[0]==id[1]:
                    return "tail2023_%s%s%s_%s"%(id[0],id[-4],id[-1],10000*8) #11233444
                return "tail23_%s%s_%s"%(id[-4],id[-1],100000*4) #12344555
        else:
            if id[0]==id[1]:
                if id[2]==id[3]:
                    return "tail2203_%s%s%s_%s"%(id[0],id[2],id[-1],10000*10) #11223444
                return "tail203_%s%s_%s"%(id[0],id[-1],100000*8) #11234555
            d={}
            for i in range(4):d[id[i]]=1
            if len(d)==2:
                return "tailx03_%s_%s"%(id[-1],50000*1.5) #11213444  12123444
            return "tail3_%s_%s"%(id[-1],1000000*3) #10345666
        
    #连对号
    if id[-1]==id[-2] and id[-3]==id[-4]:
        if id[-5]==id[-6]:
            if int(id[-1])+1==int(id[-3]) and int(id[-1])+2==int(id[-5]):
                return "stair_%s%s%s_%s"%(id[-5],id[-3],id[-1],1000) #96443322
            if int(id[-1])-1==int(id[-3]) and int(id[-1])-2==int(id[-5]):
                return "stair_%s%s%s_%s"%(id[-5],id[-3],id[-1],1000) #96223344
            if id[-7]==id[-8]:
                return "tail2222_%s%s%s%s_%s"%(id[-8],id[-6],id[-4],id[-2],1000*2) #11223344
            elif id[-7]==id[-6]:
                return "tail322_%s%s%s_%s"%(id[-6],id[-4],id[-2],10000*5) #12223344
            else:
                if id[-4]==id[-6]:
                    return "tail42_%s%s_%s"%(id[-4],id[-2],10000*5) #12333344
                return "tail222_%s%s%s_%s"%(id[-6],id[-4],id[-2],100000*2) #12334455
        else:
            if id[-5]==id[-4]:
                if id[0]==id[1]:
                    return "tail2032_%s%s%s_%s"%(id[0],id[-4],id[-2],100000*10) #11233344
                return "tail32_%s%s_%s"%(id[-4],id[-2],100000*5) #10344455
            if id[0]==id[1] and id[0]==id[2]:
                return "tail3022_%s%s%s_%s"%(id[0],id[-4],id[-2],10000*10) #11123344
            else:
                if id[0]==id[1]:
                    if id[0]==id[2]:
                        return "tail3022_%s%s%s_%s"%(id[0],id[-4],id[-2],10000*3) #11123344
                    return "tail2022_%s%s%s_%s"%(id[0],id[-4],id[-2],100000*5) #11234455
                return "tail22_%s%s_%s"%(id[-4],id[-2],1000000*10) #10345566

    #前豹子号
    for i in range(8):
        if id[0]!=id[1+i]:
            break
    if i>=3:
        if id[-1]==id[-2]:
            return "head%s02_%s%s_%s"%(i+1,id[0],id[-1],pow(10,8-i)*1) #11123044 头打折
        return "head%s_%s_%s"%(i+1,id[0],pow(10,8-i)*5) #11123045 头打折
        
    #521 1314
    if ("521" in id or "520" in id) and "1314" in id and "5213" not in id:
        return "luck_5211314_%s"%(100)
    #13146547
    if id.startswith("1314") or id.endswith("1314"): return "luck_1314_%s"%(100000*5)
    #1688
    if id.startswith("1688") or id.endswith("1688"): return "luck_1688_%s"%(100000*5)
    #1588
    if id.endswith("1588"): return "luck_1588_%s"%(100000*5)
    #5188
    if id.endswith("5188"): return "luck_5188_%s"%(100000*5)
        
    #前连对
    if id[0]==id[1] and id[2]==id[3]:
        if id[4]==id[5]: 
            if int(id[0])+1==int(id[2]) and int(id[0])+2==int(id[4]):
                return "stair_%s%s%s_%s"%(id[0],id[2],id[4],10000) #22334496
            if int(id[0])-1==int(id[2]) and int(id[0])-2==int(id[4]):
                return "stair_%s%s%s_%s"%(id[0],id[2],id[4],10000) #44332296
            if id[6]==id[5]: 
                return "head223_%s%s%s_%s"%(id[0],id[2],id[4],10000*10) #11223334
            return "head222_%s%s%s_%s"%(id[0],id[2],id[4],100000) #11223345
        # return "head22_%s%s"%(id[0],id[2]) #没啥用，还会误伤 11443210
        
    #尾顺
    upstepcnt=downstepcnt=1
    for i in range(-1,-8,-1):
        if int(id[i])-1==int(id[i-1]):upstepcnt+=1
        else: break
    if upstepcnt>=4: 
        if id[0]==id[1]:
            return "tailup20%s_%s%s_%s"%(upstepcnt,id[0],id[-1],pow(10,8-upstepcnt+1)*5) #11023456
        return "tailup%s_%s_%s"%(upstepcnt,id[-1],pow(10,8-upstepcnt+1)*2) #01023456
    for i in range(-1,-6,-1):
        if int(id[i])+1==int(id[i-1]):downstepcnt+=1
        else:break
    if downstepcnt>=4: 
        if id[0]==id[1]:
            return "taildown20%s_%s%s_%s"%(downstepcnt,id[0],id[-1],pow(10,8-downstepcnt+1)*1.5) #11065432
        return "taildown%s_%s_%s"%(downstepcnt,id[-1],pow(10,8-downstepcnt+1)*2) #01065432
        
    #头顺
    upstepcnt0=downstepcnt0=1
    for i in range(8):
        if int(id[i])+1==int(id[i+1]):upstepcnt0+=1
        else: break 
    if upstepcnt0>=4: 
        if id[-1]==id[-2]:
            return "headup%s02_%s%s_%s"%(upstepcnt0,id[0],id[-1],pow(10,8-upstepcnt0+1)*3) #12345922
        return "headup%s_%s_%s"%(upstepcnt0,id[0],pow(10,8-upstepcnt0+1)*5) #12345867
    for i in range(8):
        if int(id[i])-1==int(id[i+1]):downstepcnt0+=1
        else:break
    if downstepcnt0>=4: 
        if id[-1]==id[-2]:
            return "headdown%s02_%s%s_%s"%(downstepcnt0,id[0],id[-1],pow(10,8-upstepcnt0+1)*1.5) #65432922
        return "headdown%s_%s_%s"%(downstepcnt0,id[0],pow(10,8-upstepcnt0+1)*2) #65432972

    #5205
    if id.startswith("520") or id.endswith("520"): return "luck_520_%s"%(500000)
    #521
    if id.startswith("521") or id.endswith("521"): return "luck_521_%s"%(500000)
        
    #中间n连
    for lianN in range(6,3,-1):
        for c in range(10):
            cc=str(c)*lianN
            if cc in id:
                return "mid%s_%s_%s"%(lianN,c,pow(10,8-lianN+1)*1.2) #mid 打折
        
    #纯的补丁
    if len(idc_count)==3:
        if "0" in id:
            minc='0'
            for i in range(len(idc)):
                if idc[i]>minc:
                    minc=idc[i]; break
            return "double0_%s%s_%s"%(minc,idc[-1],656100) #11021012
    
    # 尾三带一
    d={}
    for c in id[-4:]:
        d[c]=d.get(c,0)+1
    if len(d)==2:
        c1=c3=None
        for k,v in d.items():
            if v==1: c1=k
            if v==3: c3=k
        if c1:# 屏蔽 1212的类型
            return "t31_%s%s_%s"%(c3,c1,1000000*10) #
        
    return "0_0_0" #other


## 卖狗
def sell_dog(petId, amount, username="mengpanfei"):
#     petId="4095578422147784544"
#     amount="223"
    param={"petId":petId,"amount":str(amount),"requestId":int(time.time() * 1000),"appId":1,"tpl":"","timeStamp":"null","nounce":"null","token":"null","phoneType":"android"}
    url="https://pet-chain.duxiaoman.com/data/market/sale/shelf/create"
    headers=get_httpheader(username)
    r=requests.post(url,data=json.dumps(param),headers=headers,verify=False)
    return r.json()["errorMsg"]


#取消卖狗，狗狗下架
def cancel_sell_dog(petId, username="mengpanfei"):
#     petId="4095578422147784544"
#     amount="223"
    param={"petId":petId,"requestId":int(time.time() * 1000),"appId":1,"tpl":"","timeStamp":"null","nounce":"null","token":"null","phoneType":"android"}
    url="https://pet-chain.duxiaoman.com/data/market/unsalePet"
    headers=get_httpheader(username)
    r=requests.post(url,data=json.dumps(param),headers=headers,verify=False)
    return r.json()["errorMsg"]


# 卖掉狗窝里的狗
dogs=get_my_dogs("mengpanfei")
dogcount=0
for dog in dogs:
    if dog[2] >= 2 : continue # 级别
    if dog[7] in ("0_0_0") : continue # 靓号类型
    if not dog[7].startswith("tail3"): continue #先只卖尾豹子号
    if dog[0][-1] in ("6","8","9"): continue # 689尾号不卖
    if dogcount>300: break # 每次卖300。 太多了会被封号。
    cancel_sell_dog(dog[1])
    time.sleep(2)
    price="2666.{tn}{tn}".format(tn=dog[0][-1])
    sell_dog(dog[1],price)
    dogcount+=1
#     print(time.time(),dog[0],price,dog[1],dog[7])
    time.sleep(5)
print(time.time(),"\tdone")    
