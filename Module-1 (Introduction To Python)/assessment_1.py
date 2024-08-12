import datetime

def f_astock(f_name, f_qty, f_price):
    f_details['qty'] = f_qty
    f_details['price'] = f_price
    stock[f_name] = f_details
    print("\n ACTION IS SUCCESSFUL \n")

    file = open("log_file.txt", "a")
    file.write(f"\n{f_name} => Quantity : {f_qty} , Price : {f_price}   ({datetime.datetime.now()})\n*****************************************************************************************************")
    file.close()

def f_ustock(f_name, f_qty, f_price):
    f_details['qty'] = f_qty
    f_details['price'] = f_price
    stock[f_name] = f_details
    print("\n ACTION IS SUCCESSFUL \n")

    file = open("log_file.txt", "a")
    file.write(f"\n{f_name} => Quantity : {f_qty} , Price : {f_price}   ({datetime.datetime.now()})     [UPDATED]\n*****************************************************************************************************")
    file.close()

def c_buy(b_name, b_qty, price, name):
    file = open("log_file.txt", "a")
    file.write(f"\n{b_name} => Quantity : {b_qty} , Bill : {price},  Customer : {name}   ({datetime.datetime.now()})     [PURCHASED]\n*****************************************************************************************************")
    file.close()
    upd(f_name,f_qty, f_price)

def upd(name, qty, price):
    file = open("log_file.txt", "a")
    file.write(f"\n{f_name} => Quantity : {f_qty - b_qty} , Price : {f_price}   ({datetime.datetime.now()})     [STOCK]\n*****************************************************************************************************")
    file.close()

# dictionary to store details

stock = dict()
f_details = dict()

while True:

    print("\n\t\t\t Welcome To Fruit Market\t\t\t\n")
    print("\t\t\t 1) Manager\t\t\t")
    print("\t\t\t 2) Customer \t\t\t")
    print("\t\t\t 3) Exit\t\t\t\n\n")

    role = input("Select your role :")

    if role == '1':
        while True:
            print("\n\t\t\tFruit Market Manager\n")
            print("\t\t\t 1) Add Fruit Stock")
            print("\t\t\t 2) View Fruit Stock")
            print("\t\t\t 3) Update Fruit Stock\n\n")

            choice = input("Enter Your Choice :")


            if choice == '1':
                f_name = input("Enter Fruit Name :").upper()
                f_qty = int(input("Enter qty(in kg) :"))
                f_price = int(input("Enter Price :"))
                f_astock(f_name, f_qty, f_price)
                choice2 = input("Do you want to perform any more operations. press y for yes n for no :")
                if choice2 == 'n':
                    break
                elif choice2 == "y":
                    continue
                else:
                    print("!!!INVALID INPUT!!!")

            elif choice == '2':
                print(stock)
                choice2 = input("Do you want to perform any more operations. press y for yes n for no :")
                if choice2 == 'n':
                    break
                elif choice2 == "y":
                    continue
                else:
                    print("!!!INVALID INPUT!!!")

            elif choice == '3':
                upd = input("Enter Fruit Name :").upper()
                if upd in stock:
                    f_qty = int(input("Enter qty(in kg) :"))
                    f_price = int(input("Enter Price :"))
                    f_ustock(upd, f_qty, f_price)
                    choice2 = input("Do you want to perform any more operations. press y for yes n for no :")
                    if choice2 == 'n':
                        break
                    elif choice2 == "y":
                        continue
                    else:
                        print("!!!INVALID INPUT!!!")
                else:
                    print("not in database")
                    choice2 = input("Do you want to perform any more operations. press y for yes n for no :")
                    if choice2 == 'n':
                        break
                    elif choice2 == "y":
                        continue
                    else:
                        print("!!!INVALID INPUT!!!")
            else:
                print("!!!INVALID INPUT!!!")


    elif role == '2':

        while True:

            print("\n\t\t\tCustomer\n")
            print("\t\t\t 1) View Fruit Market")
            print("\t\t\t 2) Exit\t\t\t\n\n")

            choice3 = input("Enter Your Choice :")

            if choice3 == '1':
                print("\n\t\t\tFruit Market")
                for i in stock.keys():
                    print(f"\n\t\t\t{i} : {stock[i]}")

                print("\n1) Buy Fruits")
                print("2) Exit\n")
                choice4 = input("Enter Your Choice :")

                if choice4 == '1':
                    b_name = input("Enter Fruit Name :").upper()
                    if b_name in stock:
                        b_qty = int(input("Enter qty(in kg) :"))
                        if b_qty <= stock[b_name]["qty"]:
                            stock[b_name]["qty"] -= b_qty
                            price = b_qty*stock[b_name]["price"]

                            print("\n\t\t\tYour Bill\t\t\t\n")
                            name = input("Enter Your Name :")

                            print(f"{b_name} : {b_qty} (qty)  => Rs. {price}")
                            c_buy(b_name, b_qty, price, name)

                            print("\t\t\tThank You For Shopping\t\t\t\n")
                            choice5 = input("Do you want to perform any more operations. press y for yes n for no :")
                            if choice5 == 'n':
                                break
                            elif choice5 == "y":
                                continue
                            else:
                                print("!!!INVALID INPUT!!!")

                        else:
                            print("\nAmount Of Quantity Is Not Available In Market")

                    else:
                        print("not in market\n")


                elif choice4 == '2':
                    break
                else:
                    print("!!! Invalid Input !!!")
                    continue

            elif choice3 == '2':
                break
            else:
                print("!!! Invalid Input !!!")
                continue

    elif role == '3':
        break

    else:
        print("!!! Invalid Input !!!")
        continue