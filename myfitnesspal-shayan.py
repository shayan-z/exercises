energy = 509
protein = 1.8
fat = 8
carbohydrates = 10.6
numberofcookie = input("how many cookies did you have? ")

totalofenergy = energy * int(numberofcookie)
totalofprotein = protein * int(numberofcookie)
totaloffat = fat * int(numberofcookie)
totalofcarbohydrates = carbohydrates * int(numberofcookie)

if int(numberofcookie) > 2:
    print("The cookies is making you fat! Be carefull you had: \n"
      + str(int(totalofenergy)) + " energy, "
      + str(int(totalofprotein)) + " protein, "
      + str(int(totaloffat)) + " fat, "
      + str(int(carbohydrates)) + " carbohydrates. \nYou need to stop eating that much cookies!!! "
     )
else:
   print("You like cookies dont you! " 
      + str(int(totalofenergy)) + " energy, " 
      + str(int(totalofprotein)) + " protein, "
      + str(int(totaloffat)) + " fat, " 
      + str(int(carbohydrates)) + " fat. You can have one more"
     )
