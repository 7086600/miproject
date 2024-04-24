# create empty dictionary
medicalCosts = {}

# fill in dict by first data
medicalCosts["Marina"] = 6607.0
medicalCosts.update({"Vinay": 3225.0})
medicalCosts.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})
# update Vinay
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
#print(namesToAges)

# extract records

marina_age = namesToAges.get("Marina", None)
print("Marina's age is {}".format(marina_age))

# create medical records db

medical_records = {}
medical_records["Marina"] = {"Age": 27, 
                             "Sex": "Female", 
                             "BMI": 31.1, 
                             "Children": 2, 
                             "Smoker": "Non-smoker", 
                             "Insurance_cost": 6607.0}

medical_records.update({"Vinay": {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0},
                        "Connie": {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0},
                        "Isaac": {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0},
                        "Valentina": {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}})

# print(medical_records)

# read db record
print("Connie's insurance cost is {} dollars.".format(medical_records["Connie"]["Insurance_cost"]))

#remove db record

medical_records.pop("Vinay")
# print(medical_records)

# read all db recods and print out it

for key, value in medical_records.items():
    print("{Name} is a {Age} year old, {Sex}, {Smoker} with a BMI of {BMI} and insurance cost of {Insurance_cost}".format(
        Name = key, 
        Age = value["Age"],
        Sex = value["Sex"],
        Smoker = value["Smoker"],
        BMI = value["BMI"],
        Insurance_cost = value["Insurance_cost"]))