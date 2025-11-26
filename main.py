# Expence Tracker

expencelist = [] 

print("======  WELCOME TO THE EXPENCE TRACKER  ======")

while True:
    print("====== MENU ======")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4.Exit")

    choice =int(input("Please Enter your choice :"))

    if(choice==1):
        date = input("On which date did you spend it : ")
        category = input("What type of expece is it? :")
        description = input("Enter More detail :")
        amount = float(input("Enter the Amount :"))
# 1.Adding Expences
        expence = {
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expencelist.append(expence)
        print("\n====  Expenses Added Successfully  ====")

#2.View All Expences

    elif(choice==2):
        if(len(expencelist)==0):
            print("==== Nothing expence are saved ====")
        else:
            print("==== This is your Expenses ====")

            count = 1 
            
            for eachspend in expencelist:
                print(f"Number of spending {count} -> {eachspend["date"]},{eachspend["category"]},{eachspend["description"]},{eachspend["amount"]}")
                count = count+1

 # 3. View total Spending
 #    
    elif(choice==3):
        total = 0
        for eachspend in expencelist :
            total = total + eachspend["amount"]

        print("\n ===== Total Spend = ",total)

    elif(choice==4):
        print("======= Thank you for Visiting =======")
        break
    else:
        print ("You entered Invalid Choice")
    
    
    