booksTitles = []
while True:
    print('Name of the book is ' + str(len(booksTitles) + 1) +
          ' (To end do not enter anything.):')
    title = input()
    if title == '':
        break
    booksTitles = booksTitles + [title]
print('The books I have in my home bibliothek: ')
for title in booksTitles:
    print(' ' + title)