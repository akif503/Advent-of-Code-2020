with open("input.txt","r") as inputFile:
    data = [int(x) for x in inputFile.read().split("\n") if x != ""]


for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i] + data[j] == 2020:
            with open("out1.txt","w") as out1:
                out1.write(f"{data[i]*data[j]}\n")
        for k in range(j+1,len(data)):
            if data[i] + data[j] + data[k] == 2020:
                with open("out2.txt","w") as out2:
                    out2.write(f"{data[i]*data[j]*data[k]}\n")


