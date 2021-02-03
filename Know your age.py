print("Welcome to (Know Your Age) Application ")
#Data of Today
print("Frist, Write the Date Today")
now_day = int(input(" Today : "))
now_month = int(input(" The Month : "))
now_year = int(input(" Year : "))
print("Second, Write the Date of birth")
n=1
while n==1 :
   #birth Data
    birth_day = int(input(" Day : "))
    birth_month = int(input(" Month : "))
    birth_year = int(input(" Year : "))
    
    if birth_year > now_year :
        print("You are not born yet !")
    else:
        #1 from 3 >> now_month < birth_month
        if now_month < birth_month :
            age_year = now_year - birth_year - 1
            age_month = (now_month - 1) + (12 - birth_month)
            age_day = (30 - birth_day) + now_day
            if age_day >= 30 :
                age_month = age_month + 1
                age_day = age_day - 30
                print("YOUR AGE \n", age_year, "Years", age_month, "Months", age_day, "Days")
            else:
                print("YOUR AGE \n", age_year, "Years", age_month, "Months", age_day, "Days")
        #2 from 3  now_month > birth_month   
        elif now_month > birth_month :
            age_year = now_year - birth_year
            age_month = now_month - birth_month - 1
            age_day = (30 - birth_day) + now_day
            if age_day >= 30 :
                age_month = age_month + 1
                age_day = age_day - 30
                print("YOUR AGE \n", age_year, "Years", age_month, "Months", age_day, "Days")
            else:
                print("YOUR AGE \n", age_year, "Years", age_month, "Months", age_day, "Days")
       #3 from 3 now month = birth month
        else:
            if now_day < birth_day :
                age_year = now_year - birth_year - 1
                age_month = (now_month - 1) + (12 - birth_month)
                age_day = (30 - birth_day) + now_day
                print("YOUR AGE \n", age_year, "Years", age_month, "Months", age_day, "Days")
            elif now_day == birth_day :
                age_year = now_year - birth_year
                age_month = 0
                age_day = 0
                print("YOUR AGE \n", age_year, "Years", age_month, "Months", age_day, "Days \nToDay is Your Birthday")
            else:
                age_year = now_year - birth_year
                age_month = 0
                age_day = now_day - birth_day
                print("YOUR AGE \n", age_year, "Years", age_month, "Months", age_day, "Days")
    n=int(input("\n Enter 1 to more or 0 to exit : "))
    if n==1 :print("\n Welcome, Write the Date of birth")
    else:print("GOOD BYE")