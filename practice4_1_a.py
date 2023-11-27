from time import sleep

def countdown(n):
    if n > 0:
        if n < 10:
            if n % 2 == 0:
                print("Launch Imminent!")
            else:
                print(n)
        else:
            print(n)


        sleep(1)
        countdown(n-1)
    else:
        print("Launch!")

print(countdown(10))