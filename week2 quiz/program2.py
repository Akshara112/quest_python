#code to demonstrate use of inheritance and polymorphism


class Eatable:
    def __init__(self, carbs, fat, protein, isPeelable, isBoneless ):
        self.carbs = carbs
        self.fat = fat
        self.protein = protein
        self.isPeelable = isPeelable
        self.isBoneless = isBoneless

    def choice(self):
        peelable =  self.isPeelable 
        boneless =  self.isBoneless
        

class Vegetarian(Eatable):
    def __init__(self, carbs, fat, protein, isPeelable, isBoneless ):
        super().__init__(carbs, fat, protein, isPeelable, isBoneless )

    def choice(self):
        return super().choice()
    

class NonVegetarian(Eatable):
    def __init__(self, carbs, fat, protein, isPeelable, isBoneless):
        super().__init__(carbs, fat, protein, isPeelable, isBoneless)

    def choice(self):
        return super().choice()

vegetarian_item = Vegetarian(1,1,5,True,False)
non_vegetarian_item = NonVegetarian(3,1,1,False,True)

print(vegetarian_item.choice())
print(non_vegetarian_item.choice())