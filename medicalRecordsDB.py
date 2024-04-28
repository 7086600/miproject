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

marinaAge = namesToAges.get("Marina", None)
print("Marina's age is {}".format(marinaAge))

# create medical records db

medicalRecords = {}
medicalRecords["Marina"] = {"Age": 27, 
                             "Sex": "Female", 
                             "BMI": 31.1, 
                             "Children": 2, 
                             "Smoker": "Non-smoker", 
                             "insuranceCost": 6607.0}

medicalRecords.update({"Vinay": {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "insuranceCost": 3225.0},
                        "Connie": {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "insuranceCost": 8886.0},
                        "Isaac": {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "insuranceCost": 16444.0},
                        "Valentina": {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "insuranceCost": 6420.0}})

# print(medicalRecords)

# read db record
print("Connie's insurance cost is {} dollars.".format(medicalRecords["Connie"]["insuranceCost"]))

#remove db record

medicalRecords.pop("Vinay")
# print(medicalRecords)

# function for read all db recods and print out it

def printMedicalRecords():
    for key, value in medicalRecords.items():
        print("{Name} is a {Age} year old, {Sex}, {Smoker} with a BMI of {BMI} and insurance cost of {insuranceCost}".format(
            Name = key, 
            Age = value["Age"],
            Sex = value["Sex"],
            Smoker = value["Smoker"],
            BMI = value["BMI"],
            insuranceCost = value["insuranceCost"]))

# printMedicalRecords()

# function for update medical records db

def updateMedicalRecords(name, age, sex, bmi, children, smoker, insCost):
    medicalRecords.update({name : {
                                    "Age": age, 
                                    "Sex": sex,
                                    "BMI": bmi,
                                    "Children": children,
                                    "Smoker": smoker,
                                    "insuranceCost": insCost
                                    }})

updateMedicalRecords("ZoRRo", 33, "Male", 25.7, 0, "NO!", 15777.78)

printMedicalRecords()