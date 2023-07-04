print("hello and welcome to my bmi calculator")
height=float(input("what is height? "))
weight=float(input("what is your weight? "))
bmi=weight/height**2
final_bmi=round(bmi)
if bmi<18.5:
  print(f"Your BMI is {final_bmi}, you are underweight")
elif 18.5<bmi<25:
  print(f"Your BMI is {final_bmi}, you have a normal weight")
elif 25<bmi<30:
  print(f"Your BMI is {final_bmi}, you are slightly overweight")
elif 30<bmi<35:
  print(f"Your BMI is {final_bmi}, you are obese")
elif bmi>35:
  print(f"Your BMI is {final_bmi}, you are clinically obese")
input("enter any key to exit")