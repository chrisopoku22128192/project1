def main():
    names = [] #the names will be stored here
    print("Enter names (type 'end' to stop):")
 #this guides the user to enter the names and to end a list of names and move to the next list when 'end' is typed

    
    while True:
        name = input()
        if name == 'end':
            break
        names.append(name)
#this checks the list of names and breaks into the next list when the user types 'end' at the ending of a list of names
    
    group1 = []
    group2 = []
    group3 = []
    group4 = []
    group5 = []
    group6 = []
#this stores the list of names in groups from 1 - 6
    
    for i in range(len(names)):
        if i < 6:
            group1.append(names[i])
        elif i < 12:
            group2.append(names[i])
        elif i < 18:
            group3.append(names[i])
        elif i < 24:
            group4.append(names[i])
        elif i < 30:
            group5.append(names[i])
        else:
            group6.append(names[i])

    print("1.", group1)
    print("2.", group2)
    print("3.", group3)
    print("4.", group4)
    print("5.", group5)
    print("6.", group6)
# did it "1.", group1 and the rest so that the output will be organized

if __name__ == "__main__":
    main()

