class NegativeNumberError(Exception):
    def __init__(self, number, message="переданное число отрицательное"):
        self.number = number
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.number}"
    

def check_positive_number(number :float):
    if number > 0: 
        print("число является положительным")
    elif number == 0:
        print("число = 0")    
    else: 
        raise NegativeNumberError(number)   

print(check_positive_number(10))
print(check_positive_number(0))
print(check_positive_number(-10.1))