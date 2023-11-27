from time import sleep

def countdown(n):
    while n > 0:
        if n < 10:
            if n % 2 == 0:
                print("Launch Imminent!")
            else:
                print(n)
        else:
            print(n)
        sleep(1)
        n = n-1
    print("Launch!")

print(countdown(20))