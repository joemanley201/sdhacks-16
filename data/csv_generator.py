import random
firstNames = "John,Oliver,Melissa,Monica,Rachel,Sri,Binny,Stuart,Joe"
lastNames = "Shah,Singh,Chen,Chan,Wang,Smith,Greene,Watson,Lee"
countries = "India,China,USA,UK,Australia,Germany,France,Mexico,Italy,Greece,Spain,Japan"
universities = "Michigan,California - San Diego,California - Santa Cruz,California - Santa Barbara,Pennsylvania, Washington,California - Los Angeles,Texas - Austin,Wisconsin - Madison"
departments = "CSE,ECE,Bioinformatics,CE,Maths,Data Science"
degrees = "BS,MS,PhD"
#email, age

outputCSVFileName = "data.csv"
record_limit = 500

def getRandomValue(array):
    return array[random.randrange(0, len(array))]


outputCSVFile = open(outputCSVFileName, 'w')
outputCSVFile.write('name' + "," + 'email' + "," + 'age' + "," + 'country' + "," + 'university' + "," + 'department' + "," + 'degree')
outputCSVFile.write("\n")
for idx in xrange(record_limit):
    name = getRandomValue(firstNames.split(",")) + " " + getRandomValue(lastNames.split(","))
    email = name.replace(" ", "") + str(random.randrange(1, 10000)) + "@gmail.com"
    age = str(random.randrange(20,29))
    country = getRandomValue(countries.split(","))
    university = "University of " + getRandomValue(universities.split(","))
    department = getRandomValue(departments.split(","))
    degree = getRandomValue(degrees.split(","))

    outputCSVFile.write(name + "," + email + "," + age + "," + country+ "," + university + "," + department + "," + degree)

    if idx != record_limit - 1:
        outputCSVFile.write("\n")
outputCSVFile.close()

print outputCSVFileName, "is generated"