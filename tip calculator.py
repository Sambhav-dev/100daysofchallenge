#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("hello and welcome to my tip")
bill=float(input("what is your total bill ?"))
tip=int(input("how much tip you want to give? 12%, 15%, 20% "))
people=("how many people you want to split the bii ?")
total_bill=tip/100*bill+bill
number=int(input("how many people you want to split the bill? "))
bill_split=total_bill/number
final_bill=round(bill_split, 2)
message=f"each person should pay {final_bill}"
print(message)
input("enter any key to exit")