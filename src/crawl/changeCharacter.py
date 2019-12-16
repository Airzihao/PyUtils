

pandaStr = ['p','a','n','d','a']
iter = 0
with open("./pandatext1.txt",'r',encoding='utf-8') as input:
    with open("./logo1.txt",'w+',encoding='utf8') as output:
        for line in input:
            line = list(line)
            for i in range(0,len(line)):
                if(line[i]!=' ' and line[i]!='\n'):
                    line[i] = pandaStr[iter%5]
                    # line[i] = str('t')
                    iter+=1
            # line = str(line)
            # print(line)
            line = ",".join(line)
            line = line.replace(",","")
            if(line.isspace() == False ):

                print(line[0])
                output.write(line)

