# User Input
age = int(input("Enter age: "))
gender = input("Enter gender: \nM. Male\nF. Female\nO. Other\nEnter any number: ")
occupation = input("Enter your occupation: \nS. Student\nW. Working\nEnter any number: ")
discount_pin = [12345, 67890, 23456]
residence_pin = int(input("Enter your pin: "))
residence = input("Enter your choice: \nH. Hosteler\nL. Localite\nEnter any number: ")

class Customer:
    def __init__(self, age, gender, occupation, residence_pin, residence):
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.residence_pin = residence_pin
        self.residence = residence
    
    def discounts(self):
        
        if self.gender.lower() == "m":
            if self.age >= 60:
                print("15 percent discount for all products, Thank you for shopping")
            else:
                print("Earned 100 coupon on Titan/Fastrack, Thank you for shopping")
                if self.occupation.lower() == "s" and self.residence_pin in discount_pin:
                    print("500 discount applied for books")
                if self.residence.lower() == "h":
                    print("Earned discount for groceries, Thank you for shopping")
        
        elif self.gender.lower() == "f":
            if self.age >= 45:
                print("15 percent discount for all products, Thank you for shopping")
            else:
                print("Earned 100 coupon on Nykaa/Fastrack, Thank you for shopping")
                if self.occupation.lower() == "s" and self.residence_pin in discount_pin:
                    print("500 discount applied for books")
                if self.residence.lower() == "h":
                    print("Earned discount for groceries, Thank you for shopping")
        
        else:
            print("Thank you for shopping")


customer = Customer(age, gender, occupation, residence_pin, residence)

customer.discounts()
