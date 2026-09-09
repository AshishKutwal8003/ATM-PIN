pin=8003

userpin=int(input("Enter your pin :"))

if userpin==pin:

    print("pin verify✅✅✅")
    print("Welcome to Ashish Bank")

    print("""
    1.Deposit
    2.withdraw
    3.Balance chake
    4.Exit
    """)

    Balance=10000

    choice=int(input("Enter your choice :"))

    if choice==1:
        Deposit=float(input("Enter your Deposit Amount "))

        if Deposit>0:
            Balance+=Deposit
            print("Rs",Deposit,"has been deposit successfully,new Balance is Rs",Balance)
        else:
            print("Invalid Amount")

    elif choice==2:
        withdraw=float(input("Enter your withdraw amount"))

        if withdraw>=0:

            if withdraw<=Balance:
                Balance-=withdraw
                print("Rs",withdraw,"has been withdraw successfully,new Balance is Rs",Balance)
            else:
                print("Insufficent Balance")
        else:
            print("Invalid Amount")

    elif choice==3:
        print("chake your Balance",Balance)

    elif choice==4:
        print("THANKS FOR VISIT Ashish Bank \nhave a nice day \nyou will more make money \nliggaly or inliggaly \nas will as \nyou wish.8003💲💲💲💲")

    else:
        ("Invalid choice")

else:
    print("Incorrect Pin❌❌❌")

    
