#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      KatieHarte
#
# Created:     26/04/2016
# Copyright:   (c) KatieHarte 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

"""I watched a video recently of a guy trying to explain the monty hall problem,
but he explained it wrong. He put three playing cards on a table, one was an
ace, and shuffled them. He had a person pick which one was the ace. Then
*without looking at the other two cards* he flipped over one of the other two,
showed that it was not an ace, and asked if the guy wanted to change cards.
Does this change the problem if the host selects an empty door without knowing
whether or not it was empty beforehand?"""

for i in range(0, 1000):
    import random
    f = open("montyhall.txt", "a")

    doors = {'a' : 'win', 'b' : 'lose', 'c' : 'lose', 'x' : 'none'}
    possibleDoors = ['a', 'b', 'c']

    firstChoice = random.randint(1,3)

    if firstChoice == 1:
        firstChoice = 'a'
    elif firstChoice == 2:
        firstChoice = 'b'
    elif firstChoice == 3:
        firstChoice = 'c'
    else:
        print("I think something has gone wrong here")

    hostChoice = random.randint(1,2)

    if firstChoice == 'a':
        if hostChoice == 1:
            hostChoice = 'b'
        if hostChoice == 2:
            hostChoice = 'c'
    if firstChoice == 'b':
        if hostChoice == 1:
            hostChoice = 'a'
        if hostChoice == 2:
            hostChoice = 'c'
    if firstChoice == 'c':
        if hostChoice == 1:
            hostChoice = 'a'
        if hostChoice == 2:
            hostChoice = 'b'

    #print("Host's choice: ", hostChoice, doors[hostChoice])

    secondChoice = 'x'

    if doors[hostChoice] == 'lose':
        for x in possibleDoors:
            #print(x)
            if x != hostChoice and x != firstChoice:
                #print(x)
                secondChoice = x

    #print("First choice: ", firstChoice, doors[firstChoice])
    #print("Second choice:", secondChoice, doors[secondChoice])

    f.write(secondChoice + '\n')

    f.close()

aCount = 0
bCount = 0
cCount = 0

f = open("montyhall.txt", 'r')
for line in f:
    #print(line)
    if line == 'a\n':
        aCount += 1
    if line == 'b\n':
        bCount += 1
    if line == 'c\n':
        cCount += 1
f.close()

winCount = aCount
loseCount = bCount + cCount

print("a: ", aCount)
print("b: ", bCount)
print("c: ", cCount)
print("wins: ", winCount)
print("losses: ", loseCount)

"""In conclusion, it looks like this version of the problem just creates a
50/50 chance that the prize will be behind a given door out of the remaining two
when the host happens to successfully choose a losing door, so it doesn't
matter if you stick or switch!"""