def one():
    print("Question One\n")

    n = int(input("How many numbers do you have? "))
    imperial = []
    metric = []
    for i in range(n):
        temp = float(input("Enter height in feet >> "))
        imperial.append(temp)

    print("\nimperial = ", imperial)

    for i in range(n):
        metric.append(imperial[i] * 30.48)

    print("  metric = ", metric)