import wizcoin


purse = wizcoin.WizCoin(2, 5, 99) # Целые числа передаются __init__()
print(purse)
print("G:", purse.galleons, "S:", purse.sickles, "K:", purse.knuts)
print("Total value:", purse.value())
print("Weight:", purse.weightInGrams(), "grams")
print()