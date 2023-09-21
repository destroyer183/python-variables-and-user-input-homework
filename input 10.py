money = int(input("How much money are you investing? "))
rate = int(input("What is the interest rate? "))
time = int(input("How many years? "))

interest = money * rate * time

interest /= 100

interest = round(interest, 2)

print("You would earn " + str(interest))