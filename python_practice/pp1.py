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

class Customer:
    def __init__(self , age, gender, occupation, residence_pin, residence):
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.residence_pin = residence_pin
        self.residence = residence
    def discounts(self):
        pass


def customer_group(age, gender, occupation, residence_pin, residence):
    if gender.lower() == "m":
        return MaleCustomer(age, gender, occupation, residence_pin, residence)
    elif gender.lower() == "f":
        return FemaleCustomer(age, gender, occupation, residence_pin, residence)
    else:
        return OtherCustomer(age, gender, occupation, residence_pin, residence)
    


class MaleCustomer(Customer):
    def discounts(self):
        if gender.lower() == "m":
            if age >= 60:
                print("15 percent discount for all product, Thank you for shopping")
            else:
                print("Earned 100 coupon on titan/fastrack, Thank you for shopping")
                if occupation.lower() == "s" and residence_pin in discount_pin: 
                    print("500 discount applied for books")    
                if residence.lower() == "h":
                    print("Earned discount for groceries, Thank you for shopping")


class FemaleCustomer(Customer):
    def discounts(self):
        if gender.lower() == "f":
            if age >= 45:
                print("15 percent discount for all product, Thank you for shopping")
            else:
                print("Earned 100 coupon on Nyka/fastrack, Thank you for shopping")
                if occupation.lower() == "s" and residence_pin in discount_pin: 
                    print("500 discount applied for books")    
                if residence.lower() == "h":
                    print("Earned discount for groceries, Thank you for shopping")


class OtherCustomer(Customer):
    def discounts(self):
        print("Thank you for shopping")



Customer = customer_group(age, gender, occupation, residence_pin, residence)
Customer.discounts()
