import math
#investment - to calculate the amount of interest you will earn on your investment
#bond - to calculate the amount you will have to pay on a home loan

invest_or_bond= input(str("enter either investment or bond from the menu above to proceed:"))
if invest_or_bond=="investment":
    if True:
        p=float(input("how much are you depositing:"))
        r=float(input("enter interest rate:"))
        r=(r/100)
        t=float(input("how many years will the investment be:"))
        simp_comp=str(input("choose simple or compound:"))
        if simp_comp=="simple":
          "simple"==simp_comp
          simp_comp=p*(1+r*t)
          total=simp_comp
          print(f"total amount when simple interest is applied: {total}")
        elif simp_comp:
           simp_comp=p*math.pow((1+r),t)
           total=simp_comp
           print(f"total amount when compound interest is applied: {total}")

elif invest_or_bond == "bond":
   if True:
      p=float(input("what is present value of house:"))
      i=float(input("enter interest rate:"))

      i= ((i/100)/12)
      n=float(input("how many months do you plan to repay:"))
      monthly=((i*p)/(1-(1+i)**(-n)))
      print(f"monthly repayment value is: {monthly}")
else:
   print("please enter valid input")