import matplotlib.pyplot as plt 
x = [1,2,3,4]
y1 = [1,4,9,16]
y2 = [2,8,18,32]

fig, ax = plt.subplots()
ax.stackplot(x,y1,y2, labels =['Line 1',"Line 2"])
ax.legend()
plt.show()