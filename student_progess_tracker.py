
# STUDENT PROGRESS TRACKER SYSTEM
while True:     # Do-While for infinity
    # PART 1: WELCOME SCREEN
    print("-----------------------------------------")
    print("      STUDENT PROGRESS TRACKER SYSTEM      ")
    print("-----------------------------------------")
    name = input("Enter Student Name : ")
    sclass = input("Enter Class : ")
    roll = input("Enter Roll Number : ")
    # PART 2: ENTER SUBJECT MARKS
    subject_count = int(input("\nHow many subjects do you want to enter? : "))
    total = 0
    marks_list = []

    for i in range(subject_count):
        mark = int(input(f"Enter marks for Subject {i+1}: "))
        marks_list.append(mark)
        total += mark

    average = total / subject_count
    # PART 3: GRADE CALCULATION
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 35:
        grade = "D"
    else:
        grade = "Fail"
    # PART 4: PASS / FAIL LOGIC
    if any(m < 35 for m in marks_list):
        result = "FAIL"
    else:
        result = "PASS"

    # PART 5: DISPLAY REPORT
    print("\n-----------------------------------------")
    print("          STUDENT PROGRESS REPORT         ")
    print("-----------------------------------------")
    print(f"Name        : {name}")
    print(f"Class       : {sclass}")
    print(f"Roll No     : {roll}")
    print(f"Total Marks : {total}")
    print(f"Average     : {average:.2f}")
    print(f"Grade       : {grade}")
    print(f"Result      : {result}")
    print("-----------------------------------------\n")
    # PART 6: MENU SYSTEM (Do-While Style)
    print("What do you want to do next?")
    print("1. Enter marks again")
    print("2. View report again")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 2:
        # Display report again without re-entering data
        print("\n-----------------------------------------")
        print("          STUDENT PROGRESS REPORT         ")
        print("-----------------------------------------")
        print(f"Name        : {name}")
        print(f"Class       : {sclass}")
        print(f"Roll No     : {roll}")
        print(f"Total Marks : {total}")
        print(f"Average     : {average:.2f}")
        print(f"Grade       : {grade}")
        print(f"Result      : {result}")
        print("-----------------------------------------\n")

    elif choice == 3:
        print("\nThank you for using the system!")
        break
