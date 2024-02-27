def age():
    global currentYear
    global birthYear
    birthYear = 2020
    currentAge = currentYear - birthYear
    print(f'Youre age is {currentAge}')


currentYear = int('Current Year: ')
birthYear = int('Birth Year: ')

age()
print(birthYear)