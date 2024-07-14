a = "Thank you so much for your time."

dictCount = {}

for i in range(len(a)):
    c = a[i]
    if c in dictCount:
        dictCount[c] = dictCount[c] + 1
    else:
        dictCount[c] = 1

print(dictCount)




filePath = "..."
fileData = open(filePath)
# a = open()
fileContent = str(fileData.buffer())
# fileContent = "Clock    Period   Waveform ...."

fileLines = fileContent.split("\n")

startFlag = 0
dataLines = []

for line in fileLines:
    l = line.trim()
    if l == "Clock Period Waveform ...":
        startFlag = 1
    elif startFlag == 1:
        if l == "Generated Master Generated ...":
            startFlag = 0
            break
        else:
            dataLines.append(l)



# fileContent.trim() == "Clock Period Waveform"