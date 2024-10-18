#this is tip calculator

print("Welecome to tip calculator!!\n")

#taking input and storing in the bill variable
bill=float(input("what was the total bill\n"))

#now calculate tip on the bill by the percentage
tip=float(input("How much tip would you like to give in percentage?\n"))
per=tip/100
total_bill=bill*per
total=total_bill+bill
#taking how much person are there to divide bill

person=int(input("Enter the number of person to divide bill\n"))
quantry=total/person

#Gving output

print(f"your sepreate bill will be{round(quantry,3)}\n")