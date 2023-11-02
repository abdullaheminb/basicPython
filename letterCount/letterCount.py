with open("strawberry.txt") as f:
    sentences = f.read()
sentences=sentences.upper().replace(",","").replace(".","")
for line in sentences.splitlines():
    lineList = []
    for sentence in line.split():
        lineList.append(sentence)
    for i in range(len(lineList)-2):
        if len(lineList[i]) == len(lineList[i+1]):
            if len(lineList[i+1]) == len(lineList[i+2]):
                print(lineList[i:i+3])