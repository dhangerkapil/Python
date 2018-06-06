	# The list of candies to print
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit",
             "Swedish Fish", "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

candyCart = []

# Print all of the candies and index
for candy in candyList:
    print("[" + str(candyList.index(candy)) + "] " + candy)

# loop
for x in range(0, 5):
    selected = input("Which candy would you like to bring home? ")

 
    candyCart.append(candyList[int(selected)])
#Candy list
print("I brought Candy..")
for candy in candyCart:
    print(candy)