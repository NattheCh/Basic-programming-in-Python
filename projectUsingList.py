listOfThings = ['apple', 'coffee', 'cat', 'wine']

things = ''
for i in range(len(listOfThings) - 2):
    things += listOfThings[i] + ', '
things = things + listOfThings[-2] + ' and ' + listOfThings[-1]
print(things)


