import datetime

def f_astock(f_name, f_qty, f_price):
    f_details['qty'] = f_qty
    f_details['price'] = f_price
    stock[f_name] = f_details

    file = open("log_file.txt", "a")
    file.write(f"\n{f_name} => Quantity : {f_qty} , Price : {f_price}   ({datetime.datetime.now()})\n*****************************************************************************************************")
    file.close()

def f_ustock(f_name, f_qty, f_price):
    f_details['qty'] = f_qty
    f_details['price'] = f_price
    stock[f_name] = f_details
    file = open("log_file.txt", "a")
    file.write(f"\n{f_name} => Quantity : {f_qty} , Price : {f_price}   ({datetime.datetime.now()})     [UPDATED]\n*****************************************************************************************************")
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
                f_name = input("Enter Fruit Name :")
                f_qty = int(input("Enter qty(in kg) :"))
                f_price = int(input("Enter Price :"))
                f_astock(f_name, f_qty, f_price)
                choi = input("Do you want to perform any more operations. press y for yes n for no :")
                if choi == 'n':
                    break
                elif choi == "y":
                    continue
                else:
                    print("!!!INVALID INPUT!!!")

            elif choice == '2':
                print(stock)
                choi = input("Do you want to perform any more operations. press y for yes n for no :")
                if choi == 'n':
                    break
                elif choi == "y":
                    continue
                else:
                    print("!!!INVALID INPUT!!!")

            elif choice == '3':
                upd = input("Enter Fruit Name :")
                if upd in stock:
                    f_qty = int(input("Enter qty(in kg) :"))
                    f_price = int(input("Enter Price :"))
                    f_ustock(upd, f_qty, f_price)
                    choi = input("Do you want to perform any more operations. press y for yes n for no :")
                    if choi == 'n':
                        break
                    elif choi == "y":
                        continue
                    else:
                        print("!!!INVALID INPUT!!!")
                else:
                    print("not in database")
                    choi = input("Do you want to perform any more operations. press y for yes n for no :")
                    if choi == 'n':
                        break
                    elif choi == "y":
                        continue
                    else:
                        print("!!!INVALID INPUT!!!")
            else:
                print("!!!INVALID INPUT!!!")


    elif role == '2':
        print("Hello!")
    elif role == '3':
        break
    else:
        print("!!! Invalid Input !!!")
        continue