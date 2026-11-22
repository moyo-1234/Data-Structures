


class Sports:
    def __init__(self, shoes, BoN):
        self.shoes = shoes
        self.BallorNot = BoN
    def display(self):
        print(self.shoes)
        print(self.BallorNot)

basketball = Sports("trainers", "Ball")
basketball.display()        
