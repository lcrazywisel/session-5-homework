









print("-------------------")
print("UNIVERSITY FORM")
print("-------------------")
#FIRST_NAME
while True:
    first_name = input("ENTER YOUR FIRST NAME: ").strip()
    if first_name.isalpha():
        first_name = first_name.capitalize()
        break
    else:
        print("INVALID FIRST NAME!")
        continue
#LAST_NAME
while True:
    last_name = input("ENTER YOUR LAST NAME: ").strip()
    if last_name.isalpha():
        last_name = last_name.capitalize()
        break
    else:
        print("INVALID LAST NAME!")
        continue
#CODE_MELLI
while True:
    code_melli = input("ENTER YOUR CODE MELLI: ").strip()
    if code_melli.isdigit() and len(code_melli) == 10:
        break
    else:
        print("ENTER YOUR CODE MELLI WITH NUMBERS (10 DIGITS)!")
        continue
#CODE_DANESHJOOYIE
while True:
    code_daneshjooyie = input("ENTER YOUR CODE DANESHJOOYIE: ").strip()
    if code_daneshjooyie.isdigit() and len(code_daneshjooyie) == 9:
        break
    else:
        print("INVALID STUDENT ID! MUST BE 9 DIGITS.")
        continue
#EDUCATION_LEVEL
while True:
    degree = input("EDUCATION LEVEL (BACHELOR/MASTER/PHD): ").strip().lower()
    if degree == "bachelor":
        degree = "Bachelor"
        break
    elif degree == "master":
        degree = "Master"
        break
    elif degree == "phd":
        degree = "PhD"
        break
    else:
        print("INVALID EDUCATION LEVEL!")
        continue
#MAJOR
while True:
    major = input("ENTER YOUR MAJOR: ").strip()
    if major.replace(" ", "").isalpha():
        major = major.title()
        break
    else:
        print("INVALID MAJOR!")
        continue
#SEMESTER
while True:
    semester = input("ENTER YOUR SEMESTER: ").strip()
    if semester.isdigit():
        semester = int(semester)
        if degree == "Bachelor" and 1 <= semester <= 8:
            break
        elif degree == "Master" and 1 <= semester <= 4:
            break
        elif degree == "PhD" and 1 <= semester <= 8:
            break
        else:
            print("INVALID SEMESTER FOR YOUR DEGREE!")
            continue
    else:
        print("PLEASE ENTER SEMESTER WITH NUMBERS!")
        continue

print()
print("------------------")
print("UNIVERSITY FORM")
print("------------------")
print("FIRST NAME:", first_name)
print("LAST NAME:", last_name)
print("CODE MELLI:", code_melli)
print("CODE DANESHJOOYIE:", code_daneshjooyie)
print("EDUCATION LEVEL:", degree)
print("MAJOR:", major)
print("SEMESTER:", semester)