person = ['name',['saving',100.00]]
hubby = person[:]
wifey = list(person)
hubby[0] = 'joe'
wifey[0] = 'jane'
hubby[1][1] = 50.00
print wifey[1] [1]