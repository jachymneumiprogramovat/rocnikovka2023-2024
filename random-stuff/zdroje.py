import json

zdroje = json.load(open("rocnikovka.json"))
zdroje = zdroje["items"]

outstr=""
for zdroj in zdroje:
    outstr+=zdroj["title"]+" ZE ZDROJE TYPU:"+zdroj["itemType"]+"\n"
    try:
        outstr+="   "+zdroj["abstractNote"]+"\n"
    except:
        pass
    outstr+="\n"

output=open("zdroje.txt","w")
output.write(outstr)
