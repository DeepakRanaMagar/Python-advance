import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [1,4,9,16]
plt.scatter(x, y, s =100)
plt.hlines(10, 0, 5, color = 'red')
plt.title("Scatter plot with horizontal lines")


plt.show()