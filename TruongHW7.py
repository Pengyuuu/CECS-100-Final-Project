'''
    Name: Eric Truong
    ID: 018149311
    Instructor: Minhthong Nguyen
    Date: December 5, 2018
'''

def spending():
    rent = '1000'
    gas = '40'
    food = '150'
    clothing = '60'
    payCar = '250'
    misc = '87'

    pie = open('spending', 'w')

    pie.write(rent + '\n')
    pie.write(gas + '\n')
    pie.write(food + '\n')
    pie.write(clothing + '\n')
    pie.write(payCar + '\n')
    pie.write(misc + '\n')

    pie.close()

spending()
