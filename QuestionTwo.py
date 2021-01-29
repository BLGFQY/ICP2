def two():
    print("Question Two\n")

    x = int(input("Input an integer >> "))
    count = 0
    while x != 0:
        if (x % 2 == 1):
            x-=1
        else:
            x/=2
        count+=1

    print("Iterations = ", count)