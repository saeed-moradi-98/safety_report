def safety_check(report):
    increasing = True
    
    levels = report.split(" ")
    if int(levels[0]) > int(levels[-1]):
        increasing = False
    else:
        increasing = True
    for i in range(len(levels) - 1):
        if int(levels[i + 1]) - int(levels[i]) == 0 or int(levels[i + 1]) - int(levels[i]) > 3 or int(levels[i]) - int(levels[i + 1]) > 3 or (int(levels[i + 1]) > int(levels[i]) and increasing == False) or (int(levels[i]) > int(levels[i + 1]) and increasing == True):
            return "Unsafe"
    return "Safe"

report = ""

while report != "exit":
    report = input("Please enter your report: ")
    if report == "exit":
        print("Program executed successfully!")
    else:
        print(safety_check(report))