









print("-----------")
print("GYM FORM")
print("-----------")
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
#AGE
while True:
    age = input("ENTER YOUR AGE: ").strip()
    if age.isdigit():
        age = int(age)
        if 12 <= age <= 100:
            break
        else:
            print("INVALID AGE! AGE MUST BE BETWEEN 12 AND 100.")
            continue
    else:
        print("ENTER YOUR AGE WITH NUMBERS!")
        continue
#GENDER
while True:
    gender = input("GENDER (MALE/FEMALE/OTHER): ").strip().lower()
    if gender == "male" or gender == "female" or gender == "other":
        gender = gender.capitalize()
        break
    else:
        print("INVALID GENDER!")
        continue
#HEIGHT
while True:
    height = input("ENTER YOUR HEIGHT IN CM: ").strip()
    if height.replace(".", "", 1).isdigit():
        height = float(height)
        if 100 <= height <= 250:
            break
        else:
            print("INVALID HEIGHT!")
            continue
    else:
        print("ENTER YOUR HEIGHT WITH NUMBERS!")
        continue
#WEIGHT
while True:
    weight = input("ENTER YOUR WEIGHT IN KG: ").strip()
    if weight.replace(".", "", 1).isdigit():
        weight = float(weight)
        if 20 <= weight <= 300:
            break
        else:
            print("INVALID WEIGHT!")
            continue
    else:
        print("ENTER YOUR WEIGHT WITH NUMBERS!")
        continue
#DISEASE
while True:
    disease = input("DO YOU HAVE ANY DISEASE? (YES/NO): ").strip().lower()
    if disease == "yes":
        while True:
            disease_name = input("ENTER DISEASE NAME: ").strip()
            if disease_name.replace(" ", "").isalpha():
                disease_name = disease_name.title()
                break
            else:
                print("INVALID DISEASE NAME!")
                continue
        break
    elif disease == "no":
        disease_name = "None"
        break
    else:
        print("PLEASE ENTER YES OR NO!")
        continue
#MEDICATION
while True:
    medication = input("DO YOU TAKE ANY MEDICATION? (YES/NO): ").strip().lower()
    if medication == "yes":
        while True:
            medication_name = input("ENTER MEDICATION NAME: ").strip()
            if medication_name.replace(" ", "").isalpha():
                medication_name = medication_name.title()
                break
            else:
                print("INVALID MEDICATION NAME!")
                continue
        break
    elif medication == "no":
        medication_name = "None"
        break
    else:
        print("PLEASE ENTER YES OR NO!")
        continue
#SPORTS_HISTORY
while True:
    sports_history = input("DO YOU HAVE SPORTS EXPERIENCE? (YES/NO): ").strip().lower()
    if sports_history == "yes":
        while True:
            sport = input("PREVIOUS SPORT: ").strip()
            if sport.replace(" ", "").isalpha():
                sport = sport.title()
                break
            else:
                print("INVALID SPORT NAME!")
                continue
        while True:
            years = input("YEARS OF EXPERIENCE: ").strip()
            if years.isdigit():
                years = int(years)
                if 0 <= years <= age:
                    break
                else:
                    print("INVALID YEARS OF EXPERIENCE!")
                    continue
            else:
                print("ENTER WITH NUMBERS!")
                continue
        break
    elif sports_history == "no":
        sport = "None"
        years = 0
        break
    else:
        print("PLEASE ENTER YES OR NO!")
        continue
#BODY_INJURY
while True:
    injury = input("DO YOU HAVE ANY BODY INJURY? (YES/NO): ").strip().lower()
    if injury == "yes":
        while True:
            injury_name = input("ENTER INJURY DETAILS: ").strip()
            if injury_name.replace(" ", ""):
                injury_name = injury_name.title()
                break
            else:
                print("INVALID INJURY DETAILS!")
                continue
        break
    elif injury == "no":
        injury_name = "None"
        break
    else:
        print("PLEASE ENTER YES OR NO!")
        continue
print()
print("-----------------------")
print(" GYM MEMBER PROFILE ")
print("-----------------------")
print("FIRST NAME:", first_name)
print("LAST NAME:", last_name)
print("AGE:", age)
print("GENDER:", gender)
print("HEIGHT:", height, "CM")
print("WEIGHT:", weight, "KG")
print("DISEASE:", disease_name)
print("MEDICATION:", medication_name)
print("SPORTS HISTORY:", sports_history)
print("PREVIOUS SPORT:", sport)
print("YEARS OF EXPERIENCE:", years)
print("BODY INJURY:", injury_name)
     
