









print("-----------------")
print("DIGITAL MENU")
print("-----------------")
total = 0
total_items = 0
while True:
    print()
    print("------- MAIN MENU -------")
    print("1. CHINESE FOOD")
    print("2. ITALIAN FOOD")
    print("3. IRANIAN FOOD")
    print("4. APPETIZERS")
    print("5. DRINKS")
    print("0. CHECKOUT")
    print("-------------------------")
    category = input("CHOOSE A CATEGORY (0-5): ").strip()
    if category == "0":
        break
    elif category == "1":
        print("---------- CHINESE FOOD ----------")
        print("1. Kung Pao Chicken 450,000")
        print("2. Sweet & Sour Chicken 420,000")
        print("3. Chow Mein 350,000")
        print("4. Fried Rice 300,000")
        print("5. Mapo Tofu 320,000")
        print("6. Peking Duck 850,000")
        print("7. Spring Rolls 250,000")
        print("8. Beef & Broccoli 480,000")
        print("9. Wonton Soup 280,000")
        print("10. Dan Dan Noodles 370,000")
    elif category == "2":
        print("---------- ITALIAN FOOD ----------")
        print("1. Margherita Pizza 390,000")
        print("2. Pepperoni Pizza 450,000")
        print("3. Spaghetti Carbonara 410,000")
        print("4. Lasagna 430,000")
        print("5. Fettuccine Alfredo 420,000")
        print("6. Risotto 400,000")
        print("7. Ravioli 380,000")
        print("8. Gnocchi 350,000")
        print("9. Penne Arrabbiata 360,000")
        print("10. Chicken Parmigiana 470,000")
    elif category == "3":
        print("---------- IRANIAN FOOD ----------")
        print("1. Kabab Koobide 390,000")
        print("2. Joojeh Kabab 370,000")
        print("3. Kabab Barg 650,000")
        print("4. Ghormeh Sabzi 320,000")
        print("5. Gheimeh 310,000")
        print("6. Zereshk Polo 390,000")
        print("7. Baghali Polo 520,000")
        print("8. Fesenjan 440,000")
        print("9. Tahchin 350,000")
        print("10. Dizi 380,000")
    elif category == "4":
        print("---------- APPETIZERS ----------")
        print("1. Caesar Salad 260,000")
        print("2. Greek Salad 230,000")
        print("3. Garlic Bread 150,000")
        print("4. Mozzarella Sticks 220,000")
        print("5. French Fries 160,000")
        print("6. Onion Rings 170,000")
        print("7. Chicken Wings 290,000")
        print("8. Bruschetta 190,000")
        print("9. Mushroom Soup 180,000")
        print("10. Hummus 160,000")
    elif category == "5":
        print("------------ DRINKS ------------")
        print("1. Coca-Cola 65,000")
        print("2. Sprite 65,000")
        print("3. Mineral Water 30,000")
        print("4. Lemonade 110,000")
        print("5. Virgin Mojito 140,000")
        print("6. Orange Juice 130,000")
        print("7. Iced Tea 95,000")
        print("8. Chocolate Milkshake 180,000")
        print("9. Strawberry Smoothie 170,000")
        print("10. Espresso 90,000")
    else:
        print("INVALID CATEGORY!")
        continue
    while True:
        choice = input("CHOOSE YOUR ITEM (0-10): ").strip()
        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice <= 10:
                break
            else:
                print("INVALID ITEM NUMBER!")
                continue
        else:
            print("PLEASE ENTER NUMBERS ONLY!")
            continue
    code = category + "-" + str(choice)
    if code == "1-1":
        food = "Kung Pao Chicken"
        price = 450000
    elif code == "1-2":
        food = "Sweet & Sour Chicken"
        price = 420000
    elif code == "1-3":
        food = "Chow Mein"
        price = 350000
    elif code == "1-4":
        food = "Fried Rice"
        price = 300000
    elif code == "1-5":
        food = "Mapo Tofu"
        price = 320000
    elif code == "1-6":
        food = "Peking Duck"
        price = 850000
    elif code == "1-7":
        food = "Spring Rolls"
        price = 250000
    elif code == "1-8":
        food = "Beef & Broccoli"
        price = 480000
    elif code == "1-9":
        food = "Wonton Soup"
        price = 280000
    elif code == "1-10":
        food = "Dan Dan Noodles"
        price = 370000
    elif code == "2-1":
        food = "Margherita Pizza"
        price = 390000
    elif code == "2-2":
        food = "Pepperoni Pizza"
        price = 450000
    elif code == "2-3":
        food = "Spaghetti Carbonara"
        price = 410000
    elif code == "2-4":
        food = "Lasagna"
        price = 430000
    elif code == "2-5":
        food = "Fettuccine Alfredo"
        price = 420000
    elif code == "2-6":
        food = "Risotto"
        price = 400000
    elif code == "2-7":
        food = "Ravioli"
        price = 380000
    elif code == "2-8":
        food = "Gnocchi"
        price = 350000
    elif code == "2-9":
        food = "Penne Arrabbiata"
        price = 360000
    elif code == "2-10":
        food = "Chicken Parmigiana"
        price = 470000
    elif code == "3-1":
        food = "Kabab Koobide"
        price = 390000
    elif code == "3-2":
        food = "Joojeh Kabab"
        price = 370000
    elif code == "3-3":
        food = "Kabab Barg"
        price = 650000
    elif code == "3-4":
        food = "Ghormeh Sabzi"
        price = 320000
    elif code == "3-5":
        food = "Gheimeh"
        price = 310000
    elif code == "3-6":
        food = "Zereshk Polo"
        price = 390000
    elif code == "3-7":
        food = "Baghali Polo"
        price = 520000
    elif code == "3-8":
        food = "Fesenjan"
        price = 440000
    elif code == "3-9":
        food = "Tahchin"
        price = 350000
    elif code == "3-10":
        food = "Dizi"
        price = 380000
    elif code == "4-1":
        food = "Caesar Salad"
        price = 260000
    elif code == "4-2":
        food = "Greek Salad"
        price = 230000
    elif code == "4-3":
        food = "Garlic Bread"
        price = 150000
    elif code == "4-4":
        food = "Mozzarella Sticks"
        price = 220000
    elif code == "4-5":
        food = "French Fries"
        price = 160000
    elif code == "4-6":
        food = "Onion Rings"
        price = 170000
    elif code == "4-7":
        food = "Chicken Wings"
        price = 290000
    elif code == "4-8":
        food = "Bruschetta"
        price = 190000
    elif code == "4-9":
        food = "Mushroom Soup"
        price = 180000
    elif code == "4-10":
        food = "Hummus"
        price = 160000
    elif code == "5-1":
        food = "Coca-Cola"
        price = 65000
    elif code == "5-2":
        food = "Sprite"
        price = 65000
    elif code == "5-3":
        food = "Mineral Water"
        price = 30000
    elif code == "5-4":
        food = "Lemonade"
        price = 110000
    elif code == "5-5":
        food = "Virgin Mojito"
        price = 140000
    elif code == "5-6":
        food = "Orange Juice"
        price = 130000
    elif code == "5-7":
        food = "Iced Tea"
        price = 95000
    elif code == "5-8":
        food = "Chocolate Milkshake"
        price = 180000
    elif code == "5-9":
        food = "Strawberry Smoothie"
        price = 170000
    elif code == "5-10":
        food = "Espresso"
        price = 90000

while True:
    quantity = input("ENTER QUANTITY: ").strip()
    if quantity.isdigit():
        quantity = int(quantity)
        if 1 <= quantity <= 100:
            break
        else:
            print("INVALID QUANTITY!")
            continue
    else:
        print("PLEASE ENTER NUMBERS ONLY!")
        continue

subtotal = price * quantity
total = total + subtotal
total_items = total_items + quantity

print()
print("---------- ORDER ADDED ----------")
print("ITEM:", food)
print("UNIT PRICE:", price, "TOMANS")
print("QUANTITY:", quantity)
print("SUBTOTAL:", subtotal, "TOMANS")
print("---------------------------------")
print("CURRENT TOTAL:", total, "TOMANS")
print()
print("-------------")
print("FINAL BILL")
print("-------------")
if total_items == 0:
    print("NO ITEMS ORDERED!")
else:
    print("TOTAL ITEMS:", total_items)
print("TOTAL AMOUNT:", total, "TOMANS")
print("--------------------------------------")
print("ORDER COMPLETED SUCCESSFULLY!") 