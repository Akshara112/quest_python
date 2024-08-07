'''* Name
* Age
 
15% discount for all product for senior citizen
 
* Gender
male senior citizen (60 and above)
female senior citizen (45 and above)
 
100 rupees nyka, fastrack, if female (<45)
100 coupon on titan, fastrack, if male (<60)
----
 
*Occupation: Working, Student (PIN code should be local)
 
College: 500 coupon on books
Working: NA
 
----
*Residence: Hosteller, Localite (Hostel name should be valid)
 
Hosteller: Groceries
Localite: NA

 '''
#" Earned 100 coupon on titan, fastrack, thank you for shopping
#Earned discount for groceries, thank you for shopping"
#Hosteler Male student  < 60



age = int(input("Enter age: "))
gender = input("Enter gender: \nM. Male\nF. Female\nO. Other\nEnter any number.")
occupation = input("Enter your occupation: \nS. Student\nW. Working\nEnter any number.")
discount_pin = [ 12345, 67890, 23456]
residence_pin = int(input("Enter your pin: "))
residence =  input("Enter your choice: \nH. Hosteler\nL. Localite\nEnter any number.")


if gender.lower() == "m":
    if age >= 60:
        print("15percent discount for all product, thank you for shopping")
    else:
        print("Earned 100 coupon on titan, fastrack, thank you for shopping")
        if occupation.lower() == "s"and residence_pin in discount_pin: 
            print("500 discount applied for books")    
        if residence.lower() == "h":
            print("Earned discount for groceries, thank you for shopping")
elif gender.lower() == "f":
    if age >= 45:
        print("15percent discount for all product, thank you for shopping")
    else:
        print("Earned 100 coupon on Nyka, fastrack, thank you for shopping")
        if occupation.lower() == "s"and residence_pin in discount_pin: 
            print("500 discount applied for books")    
        if residence.lower() == "h":
            print("Earned discount for groceries, thank you for shopping")

else:
    print("Thank you for shopping")


