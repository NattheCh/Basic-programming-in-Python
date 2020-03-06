import os.path

booksTitles = []
if os.path.isfile('file.txt'):
    textFile = open('file.txt', 'r+')
    print('The books which are currently added to the library:')
    print(textFile.read())
else:
    textFile = open('file.txt', 'w')
while True:
    print('Name of the book is (To end do not enter anything.):')
    title = input()
    if title == '':
        break
    booksTitles = booksTitles + [title]
print('The books added to my home library: ')
for title in booksTitles:
    print(title)
for title in booksTitles:
    textFile.write(str(title) + '\n')
textFile.close()
