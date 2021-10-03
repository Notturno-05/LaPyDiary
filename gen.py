#!/bin/python3
import glob
import datetime
import functools
def cmp_months(a, b):
    a=lastB(a)
    b=lastB(b)
    lookup={"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"Dicember":12}
    ca=int(lookup[a])
    cb=int(lookup[b])
    if ca > cb:
        return 1
    elif ca == cb:
        return 0
    else:
        return -1
def lastB(path):
    e=path.split("/")
    return e[len(e)-1]
list=""
years = sorted(glob.glob("diarydata/*"))
for ypath in years:
    year = int(lastB(ypath))
    list +="\n\\newpage\n\yearH{"+str(year)+"}\n"
    for mpath in sorted(glob.glob(ypath+"/*"),key=functools.cmp_to_key(cmp_months)):
        month = lastB(mpath)
        list +="\n\monthH{"+str(month)+"}\n"
        for dpath in sorted(glob.glob(mpath+"/*")):
            day = int(lastB(dpath).split(".")[0])
            r = datetime.datetime.strptime(str(day)+" "+str(month)+" "+str(year),"%d %B %Y")
            fileContent = open(dpath).read().split("\n")
            if "TITLE|" in fileContent[0]:
                title = fileContent[0].split("|")[1].strip()
                s = 1
            else:
                title = ""
                s = 0
            list+="\n\dayH{"+r.strftime("%A")+"}{"+str(day)+"}{"+str(title)+"}\n"
            for i in range(s,len(fileContent)):
                list+=fileContent[i]
modelTex=open("model.tex","r").read()
open("final.tex","w").write(modelTex.replace("REPLACETHIS",list))
