#NMTM is "Number of minutes talked in a month"
def TotalPrice(NMTM):
    TAB = [] 
    # Plan A: 200DH for unlimited minutes
    price_A = 200

    # Plan B: 100DH for 2 hours, and 0.5DH per additional minute
    if NMTM > 120:
        price_B = 100 + (NMTM - 120) * 0.5
    else:
        price_B = 100

    # Plan C: 50DH for 1 hour, and 1DH per additional minute
    if NMTM > 60:
        price_C = 50 + (NMTM - 60) * 1
    else:
        price_C = 50

    # Plan D: 20DH for 30 minutes, and 1.5DH per additional minute
    if NMTM > 30:
        price_D = 20 + (NMTM - 30) * 1.5
    else:
        price_D = 20

    # Plan E: 2DH per minute with no monthly fee
    price_E = NMTM * 2

    TAB.append(price_A)
    TAB.append(price_B)
    TAB.append(price_C)
    TAB.append(price_D)
    TAB.append(price_E)

    return TAB

NMTM = 0

while True:
    print("Menu:")
    print("1- Enter the communication duration")
    print("2- Display the monthly cost for each plan")
    print("3- Display the most cost-effective plan")
    print("4- Quit the program")

    choice = input("Choose an option (1/2/3/4): ")

    if choice == "1":
        NMTM = int(input("Enter the communication duration in minutes: "))

    elif choice == "2":
        prices = TotalPrice(NMTM)
        print("Monthly cost per plan:")
        for i in range(len(prices)):
            print(f"{i + 1}- Plan {i + 1}: {prices[i]} DH")

    elif choice == "3":
        prices = TotalPrice(NMTM)
        min_price = min(prices)
        best_offer = prices.index(min_price) + 1 
        print(f"The most cost-effective plan is Plan {best_offer} with a cost of {min_price} DH.")

    elif choice == "4":
        print("Program terminated.")
        break
    else:
        print("Invalid option. Please choose a valid option (1/2/3/4).")
