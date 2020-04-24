import matplotlib.pyplot as matlib3

slices = [11,9,3,2]
deliveries = ['express shipping', 'standard shipping', 'delivery to store', 'delivery to post office']
cols = ['blue', 'green', 'yellow', 'orange']

matlib3.pie(slices, labels= deliveries,
            colors= cols,
            startangle=50,
            shadow=True,
            explode=(0.2, 0, 0, 0),
            autopct='%1.2f%%')

matlib3.title('First pie chart in Python\nDeliveries')
matlib3.show()