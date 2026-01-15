import time

CountDown = int(input("Enter a Number to Start CountDown: "))
print("CountDown Starts Now!")

for i in range(CountDown,0,-1):
    print(CountDown)
    CountDown -= 1
    time.sleep(1)

print("\n Happy New Year")