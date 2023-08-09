weight=float(input("enter your weight"))
answer=input("do you want to change into pound or kg? ")
if(answer == "pound"):
  weight=weight*2.20462
  print(weight)
else:
  weight*=0.453592
  print(weight)