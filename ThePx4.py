#file = open("c:\\Users\\nmalhotra\\Downloads\\Liberal_Plan.txt", "r", encoding="utf8")
file = open("c:\\Users\\nmalhotra\\Downloads\\cp.txt", "r", encoding="utf8")

promises = ""
pcount=0
pval = 0
read = False
for line in file:
    if(line[0:2] == "• "):
        promises+="\n"
        read = True
        pcount+=1

    if read:
        if("$" in line and ("million" in line or "billion" in line)):
            val = float(line[slice(line.find("$")+1,line.find(" ",line.find("$")))])
            if("million" in line):
                val*=1000000
            if("billion" in line):
                val*=1000000000
            pval+=val
        promises+=line

    if ("." in line) and read:
        read = False

# f = open("c:\\Users\\nmalhotra\\Downloads\\Liberal.txt", "w")
f = open("c:\\Users\\nmalhotra\\Downloads\\Conservative.txt", "w")
f.write("Number of promises: " + str(pcount) + "\n")
f.write("Cost: " + str(pval) + "\n")
f.write(promises)
f.close()
