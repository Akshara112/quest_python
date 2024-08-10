class person:
    def __init__(self,age,gender,pincode):
        self.age = age
        self.gender = gender
        self.pincode = pincode
    
class student(person):
    def __init__(self,age,gender,pincode,residence):
        self.residence = residence
        super().__init__(age,gender,pincode)
    

class employee(person):
    def __init__(self,age,gender,pincode):
        super().__init__(age,gender,pincode)

s1 = student(25,"male",12345,"h")
s1 = student(25,"male",12345,"h","True")
e1 = employee(25,"male",45678,)

















def __init__(self, age, gender, pincode, residence, sportsq):
        self.residence = residence
        self.sportsq = sportsq
        super().__init__(age,gender,pincode)
    print("sports quota")