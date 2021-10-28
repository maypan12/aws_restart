print("hello world, This is python")

print("Python has three numeric types: int, float, and complex")

print("PPAP")

firststring = " I have a pen"
secondstring = " I have an apple"

print(firststring +  secondstring)

thirdstring = " I have a pen"
fourthstring = " I have pineapple"

print(thirdstring +  fourthstring)

name1 = "pen-pineapple"
name2 = " apple-pen"

print(name1 + name2 )

myValue=1
print(myValue)

print (type(myValue))

print(str(myValue) + " is of the data type " + str(type(myValue)))


myString = "This is a string."
print(myString)

print(type(myString))

print(myString + " is of the data type " + str(type(myString)))


firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)


myFruitList = ["apple", "banana", "cherry"]

print(myFruitList)

print(type(myFruitList))

print(myFruitList[0])

print(myFruitList[1])

print(myFruitList[2])

myFruitList[2] = "orange"

print(myFruitList)

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))


print(myFinalAnswerTuple[0])

print(myFinalAnswerTuple[1])

print(myFinalAnswerTuple[2])

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)

print(myFavoriteFruitDictionary["Akua"])

print(myFavoriteFruitDictionary["Saanvi"])

print(myFavoriteFruitDictionary["Paulo"])

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))

