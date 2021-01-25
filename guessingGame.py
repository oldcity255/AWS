userInputs = []
numGreater90 = []
score = 0
while score >= 0:
    score = int(input("Put a number, to exit enter a negative numbers: "))
    if score >= 90:
        userInputs.append(score)
        numGreater90.append(score)
    elif score >= 0:
        userInputs.append(score)
    else:
        print("number is out of range")
print(userInputs)
print(numGreater90)
print("Bigger than 90: ", len(numGreater90))
print("Avarege: ", sum(userInputs)/len(userInputs))


print("Merhaba from git session in vs code")

print("test for compare and pull request")

print("adding line after git checkout to main")


