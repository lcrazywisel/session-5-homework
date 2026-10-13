








print("----------------")
print("HOSPITAL FORM")
print("----------------")
#FIRST_NAME
while True:
    first_name = input("ENTER YOUR FIRST NAME:").strip()
    if first_name.isalpha():
        first_name = first_name.capitalize()
        break
    else:
        print("INVALID FIRST NAME!")
        continue
#LAST_NAME
while True:
    last_name = input("ENTER YOUR LAST NAME:").strip()
    if last_name.isalpha():
        last_name = last_name.capitalize()
        break
    else:
        print("INVALID LAST NAME!")
        continue
#AGE
while True:
    age = input("ENTER YOUR AGE:")
    if age.isdigit():
        age = int(age)
        if 0 <= age <= 120:
            if 0 <= age < 18:
                department = "PEDIATRICS DEPARTMENT"
            elif 18 <= age <= 120:
                department = "ADULTS DEPARTMENT"
                break
        else:
            print("INVALID AGE!")
            continue
    else:
        print("ENTER YOUR AGE WITH NUMBERS!")
        continue
#CODE_MELLI
while True:
    code_melli = input("ENTER YOUR CODE MELLI:").strip()
    if code_melli.isdigit() and len(code_melli) == 10:
        break
    else:
        print("INVALID CODE MELLI!")
        continue
#PHONE_NUMBER
while True:
    phone = input("ENTER YOUR PHONE NUMBER:").strip()
    if phone.isdigit() and len(phone) == 11 and phone.startswith("09"):
        break
    else:
        print("INVALID PHONE NUMBER!")
        continue
#GENDER
while True:
    gender = input("Gender(female/male/others):").strip().lower()
    if gender == "female" or "male" or "others":
        gender = gender.capitalize()
        break
    else:
        print("INVALID GENDER!")
        continue
#ADDRESS
while True:
    address = input("ENTER YOUR ADDRESS:").strip()
    address_check = address.replace(" ", "")
    if address_check.isalnum():
        address = address.title()
        break
    else:
        print("INVALID ADDRESS!")
        continue
#DISEASE
while True:
    disease = input("ENTER YOUR DISEASE:").strip()
    disease_check = disease.replace(" ", "")
    if disease_check.isalpha():
        disease = disease.title()
        break
    else:
        print("INVALID DISEASE!")
        continue
#MEDICAL_HISTORY
while True:
    history = input("MEDICAL HISTORY(YES/NO):").strip().lower()
    if history == "yes": 
        while True:
            pre_disease = input("ENTER YOUR PREVIOUS DISEASE:").strip()
            check = pre_disease.replace(" ", "")
            if check.isalpha():
                pre_disease = pre_disease.title()
                break
            else:
                print("INVALID DISEASE NAME!")
                continue
        break
    elif history == "no":
        pre_disease = "NONE."
        break
    else:
        print("PLEASE ENTER YES OR NO!")
        continue
#DOCTOR_NAME
while True:
    doctor = input("ENTER YOUR DOCTOR'S NAME:").strip()
    doctor_check = doctor.replace(" ", "")
    if doctor_check.isalpha():
        doctor = doctor.title()
        break
    else:
        print("INVALID DOCTOR NAME!")
        continue

print("----------------")
print("HOSPITAL FORM")
print("----------------")
print("FIRST NAME:", first_name)
print("LAST NAME:", last_name)
print("AGE:", age)
print("DEPARTMENT:", department)
print("CODE MELLI:", code_melli)
print("PHONE NUMBER:", phone)
print("GENDER:", gender)
print("ADDRESS:", address)
print("DISEASE:", disease)
print("MEDICAL HISTORY:", history)
print("PREVIOUS DISEASE:", pre_disease)
print("DOCTOR NAME:", doctor)











        


