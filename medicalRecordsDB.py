# create empty dictionary
medicalCosts = {}

# fill in dict by first data
medicalCosts["Marina"] = 6607.0
medicalCosts.update({"Vinay": 3225.0})
medicalCosts.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})
medicalCosts["Vinay"] = 3325.0
print(medicalCosts)

# calculate the average medical cost

totalCost = 0
for cost in medicalCosts.values():
    totalCost += cost

averageCost = totalCost / len(medicalCosts)

print("Average Insurance Cost: {}".format(averageCost))

# create patients db

names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]
zippedAges = zip(names, ages)
# make dict by using a list comprehension
namesToAges = {key: value for key, value in zippedAges} # or simple: namesToAges = dict(zippedAges)
print(namesToAges)



