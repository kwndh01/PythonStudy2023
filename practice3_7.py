print('Score Average Calculator')
class_number = input('How many classes?')
while True:
    if class_number.isdigit():
        class_number = int(class_number)
        if class_number >= 0:
            print('The number of classes = ' + str(class_number))
            break
        else:
            class_number = input('Enter a positive number:')
    else:
        class_number = input('Enter a positive number:')

x = 0
Failed = 0
for i in range(class_number):
    new = input('Enter your score:')
    while True:
        if new.isdigit():
            new = int(new)
            if 0 > new or new > 100:
                new = input('Enter your score between 0 and 100:')
            else:
                print('Your score = ' + str(new))
                if new < 60:
                    Failed = Failed + 1
                    break
                else:
                    x = x + new
                    break
        else:
            new = input('Enter your score between 0 and 100:')

if class_number == 0:
    class_number = 1

print('Your average score = ' + str(round(x / (class_number - Failed),1)))
print('Failed = ' + str(Failed))
