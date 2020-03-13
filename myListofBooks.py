import os.path

booksTitles = []
if os.path.isfile('file.txt'):
    booksTitles = open('file.txt').read().splitlines()
    for title in booksTitles:
        print(title)
textFile = open('file.txt', 'w+')
while True:
    print('\nName of the book is (To end do not enter anything.):')
    title = input()
    if title == '':
        break
    booksTitles = booksTitles + [title]
booksTitles = sorted(booksTitles)
for title in booksTitles:
    textFile.write(str(title) + '\n')
textFile.close()
