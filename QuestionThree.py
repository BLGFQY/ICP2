def three():
    print("Question Three\n")

    infile = open("input.txt", 'r')
    line = infile.readline()
    words = []
    count = []

    while line != "":
        for xStr in line.split(" "):
            xStr = xStr.replace("\n", "")
            if xStr not in words:
                words.append(xStr)
                count.append(1)
            else:
                index = words.index(xStr)
                count[index] += 1

        line = infile.readline()

    infile.close()
    outfile = open("input.txt", 'a+')

    for i in range(len(words)):
        temp = words[i]
        temp += ": "
        temp += str(count[i])
        print(temp)
        temp += "\n"
        outfile.write(temp)
    outfile.close()
