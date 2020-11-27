def tipCalculator():
  print("Welcome to the tip calculator.")
  totalBill = float(input("What was the total bill? $"))
  percentTip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
  totalTip = float(totalBill * (percentTip/100.0))
  numPeople = int(input("How many people to split the bill? "))
  billPerPerson = float((totalBill + totalTip)/numPeople)
  billPerPerson = round(billPerPerson, 2)
  print(f"Each person should pay: ${billPerPerson}")
  return billPerPerson

tipCalculator()