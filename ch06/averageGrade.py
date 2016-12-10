grades = raw_input('please input points').split()
sum = 0
for grade in grades:
    sum += int(grade)
print 'the average grade is:',sum*1.0/len(grades)