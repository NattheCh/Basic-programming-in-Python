import matplotlib.pyplot as matlib

x1 = [1,2,3,4]
y1 = [10,20,30,20]

x2 = [1,2,3,4]
y2 = [5,10,15,15]

matlib.figure(figsize=(10,6))
matlib.plot(x1, y1, color="orange", linewidth=3.0, linestyle="-", label="2020")
matlib.plot(x2, y2, color="yellow", linewidth=3.0, linestyle="dashdot", label="2019")
matlib.ylabel("Quantity for y")
matlib.xlabel("Days for x")
matlib.title("Graph in Python\nFirst deliveries")
matlib.legend()
matlib.show()

