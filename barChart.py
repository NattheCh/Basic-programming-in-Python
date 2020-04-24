import matplotlib.pyplot as matlib2

x1 = [2,4,6,8]
y1 = [10,15,10,5]

x2 = [3,5,7,9]
y2 = [5,10,15,20]

matlib2.bar(x1,y1, label='2020', color='orange')
matlib2.bar(x2, y2, label='2019', color='yellow')

matlib2.ylabel('Quantity for y')
matlib2.xlabel('Days for x')
matlib2.title('Bar in Python\nFirst bar chart')
matlib2.legend()
matlib2.show()