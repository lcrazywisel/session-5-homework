









print("--------------")
print("CAR REPAIR")
print("--------------")
registered = False
logged_in = False
while True:
    print()
    print("---------- USER MENU ----------")
    print("1. REGISTER")
    print("2. LOGIN")
    print("0. EXIT")
    print("-------------------------------")
    option = input("CHOOSE AN OPTION (0-2): ").strip()
    if option == "1":
        while True:
            username = input("CREATE USERNAME: ").strip()
            if username.isalnum() and len(username) >= 4:
                break
            else:
                print("USERNAME MUST HAVE AT LEAST 4 CHARACTERS!")
                continue
        while True:
            password = input("CREATE PASSWORD: ").strip()
            if len(password) >= 8:
                break
            else:
                print("PASSWORD MUST HAVE AT LEAST 8 CHARACTERS!")
                continue
        registered = True
        print("REGISTRATION SUCCESSFUL!")
        print("PLEASE LOGIN TO YOUR ACCOUNT.")
    elif option == "2":
        if registered == False:
            print("PLEASE REGISTER FIRST!")
            continue
        while True:
            login_username = input("USERNAME: ").strip()
            login_password = input("PASSWORD: ").strip()

            if login_username == username and login_password == password:
                print("LOGIN SUCCESSFUL!")
                logged_in = True
                break
            else:
                print("INCORRECT USERNAME OR PASSWORD!")
                retry = input("TRY AGAIN? (YES/NO): ").strip().lower()
                if retry == "no":
                    break
        if logged_in == True:
            break
    elif option == "0":
        print("PROGRAM CLOSED!")
        break
    else:
        print("INVALID OPTION!")
        continue
if logged_in == True:
    print()
    print("-------------------------")
    print("CAR OWNER INFORMATION")
    print("-------------------------")
    while True:
        first_name = input("FIRST NAME: ").strip()
        if first_name.isalpha():
            first_name = first_name.capitalize()
            break
        else:
            print("INVALID FIRST NAME!")
            continue
    while True:
        last_name = input("LAST NAME: ").strip()
        if last_name.isalpha():
            last_name = last_name.capitalize()
            break
        else:
            print("INVALID LAST NAME!")
            continue
    while True:
        phone = input("PHONE NUMBER: ").strip()
        if phone.isdigit() and len(phone) == 11 and phone.startswith("09"):
            break
        else:
            print("INVALID PHONE NUMBER!")
            continue
    while True:
        job = input("YOUR JOB: ").strip()
        if job.replace(" ", "").isalpha():
            job = job.title()
            break
        else:
            print("INVALID JOB!")
            continue
    while True:
        address = input("YOUR ADDRESS: ").strip()
        if len(address) >= 5:
            address = address.title()
            break
        else:
            print("INVALID ADDRESS!")
            continue
    print()
    print("-------------------")
    print("CAR INFORMATION")
    print("-------------------")
    while True:
        brand = input("CAR BRAND: ").strip()
        if brand.replace(" ", "").isalpha():
            brand = brand.title()
            break
        else:
            print("INVALID CAR BRAND!")
            continue
    while True:
        model = input("CAR MODEL: ").strip()
        if model.replace(" ", "").isalnum():
            model = model.title()
            break
        else:
            print("INVALID CAR MODEL!")
            continue
    while True:
        year = input("MANUFACTURING YEAR (AD): ").strip()
        if year.isdigit():
            year = int(year)
            if 1980 <= year <= 2027:
                break
            else:
                print("INVALID MANUFACTURING YEAR!")
                continue
        else:
            print("PLEASE ENTER NUMBERS ONLY!")
            continue
    while True:
        color = input("CAR COLOR: ").strip()
        if color.isalpha():
            color = color.capitalize()
            break
        else:
            print("INVALID COLOR!")
            continue
    while True:
        plate = input("LICENSE PLATE: ").strip()
        if len(plate) >= 5:
            break
        else:
            print("INVALID LICENSE PLATE!")
            continue
    while True:
        mileage = input("CAR MILEAGE (KM): ").strip()
        if mileage.isdigit():
            mileage = int(mileage)
            if 0 <= mileage <= 2000000:
                break
            else:
                print("INVALID MILEAGE!")
                continue
        else:
            print("PLEASE ENTER NUMBERS ONLY!")
            continue
    while True:
        problem = input("DESCRIBE THE CAR PROBLEM: ").strip()
        if len(problem) >= 5:
            break
        else:
            print("PLEASE DESCRIBE THE PROBLEM!")
            continue

    total = 0
    service_count = 0
    receipt = ""
    while True:
        print()
        print("---------------")
        print("SERVICE MENU")
        print("---------------")
        print("1. Engine Oil Change       750000")
        print("2. Air Filter Change       250000")
        print("3. Brake Pad Replacement   1400000")
        print("4. Car Diagnostics         450000")
        print("5. Engine Tune-Up          1200000")
        print("6. Spark Plug Change       650000")
        print("7. Transmission Service    2500000")
        print("8. Suspension Repair       2200000")
        print("9. Battery Replacement     3200000")
        print("10. AC Service             950000")
        print("11. Wheel Alignment        600000")
        print("12. Timing Belt Change     3500000")
        print("13. Radiator Service       850000")
        print("14. Exhaust Repair         1500000")
        print("15. Full Car Inspection    1800000")
        print("0. CHECKOUT")
        print("--------------------------------------")
        print("ALL PRICES ARE IN TOMANS.")
        while True:
            choice = input("CHOOSE A SERVICE (0-15): ").strip()
            if choice.isdigit():
                choice = int(choice)
                if 0 <= choice <= 15:
                    break
                else:
                    print("INVALID SERVICE NUMBER!")
                    continue
            else:
                print("PLEASE ENTER NUMBERS ONLY!")
                continue
        if choice == 0:
            break
        if choice == 1:
            service_name = "Engine Oil Change"
            price = 750000
        elif choice == 2:
            service_name = "Air Filter Change"
            price = 250000
        elif choice == 3:
            service_name = "Brake Pad Replacement"
            price = 1400000
        elif choice == 4:
            service_name = "Car Diagnostics"
            price = 450000
        elif choice == 5:
            service_name = "Engine Tune-Up"
            price = 1200000
        elif choice == 6:
            service_name = "Spark Plug Change"
            price = 650000
        elif choice == 7:
            service_name = "Transmission Service"
            price = 2500000
        elif choice == 8:
            service_name = "Suspension Repair"
            price = 2200000
        elif choice == 9:
            service_name = "Battery Replacement"
            price = 3200000
        elif choice == 10:
            service_name = "AC Service"
            price = 950000
        elif choice == 11:
            service_name = "Wheel Alignment"
            price = 600000
        elif choice == 12:
            service_name = "Timing Belt Change"
            price = 3500000
        elif choice == 13:
            service_name = "Radiator Service"
            price = 850000
        elif choice == 14:
            service_name = "Exhaust Repair"
            price = 1500000
        elif choice == 15:
            service_name = "Full Car Inspection"
            price = 1800000
        total = total + price
        service_count = service_count + 1
        receipt = receipt + str(service_count) + ". "
        receipt = receipt + service_name + " - "
        receipt = receipt + str(price) + " TOMANS\n"
        print()
        print("SERVICE ADDED SUCCESSFULLY!")
        print("SERVICE:", service_name)
        print("PRICE:", price, "TOMANS")
        print("CURRENT TOTAL:", total, "TOMANS")

    print()
    print("-----------------")
    print("FINAL INVOICE")
    print("-----------------")
    print("----------- CAR OWNER -----------")
    print("FIRST NAME:", first_name)
    print("LAST NAME:", last_name)
    print("PHONE:", phone)
    print("JOB:", job)
    print("ADDRESS:", address)
    print()
    print("-------- CAR INFORMATION --------")
    print("BRAND:", brand)
    print("MODEL:", model)
    print("YEAR:", year)
    print("COLOR:", color)
    print("LICENSE PLATE:", plate)
    print("MILEAGE:", mileage, "KM")
    print("CAR PROBLEM:", problem)
    print()
    print("-------- SELECTED SERVICES ------")
    if service_count == 0:
        print("NO SERVICES SELECTED!")
    else:
        print(receipt)
    print("---------------------------------")
    print("TOTAL SERVICES:", service_count)
    print("TOTAL AMOUNT:", total, "TOMANS")
    print("---------------------------------")