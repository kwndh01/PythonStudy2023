print('Score Average Calculator')
class_number = int(input('How many classes?'))

x = 0
for i in range(class_number):
    x = x + int(input('Enter your score:'))
if class_number == 0:
    class_number = 1

print('Your average score = ' + str(round(x / class_number,1)))
