gameList = ["Resident Evil 4", "Resident Evil 5", "Resident Evil 6", "Resident Evil 7", "Resident Evil 8", "Resident Evil 9", "Resident Evil 10"]

# list length (function (len) returns the length of the list)
print(len(gameList))

# Recover a item from the list by index
print(gameList.index("Resident Evil 7"))

# Add a item to the final of the list
gameList.append("Resident Evil 11")
print(len(gameList))

# order the list
gameList.sort()
print(gameList)

# Copy a list to another list
gameList2 = gameList.copy()
print(gameList2)
gameList2.remove("Resident Evil 11")
print(gameList2)

# Remove a item from the list by index
gameList.pop(0)
print(gameList)

# Remove a item from the list by value
gameList.remove("Resident Evil 11")

# Clear the list
gameList.clear()
print(gameList)

# Delete the list
del gameList2
