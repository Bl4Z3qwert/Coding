import matplotlib.pyplot as plt
import numpy as np



xpoints=np.array([1,2,4,6,10])
ypoints=np.array([3,8,1,10,5])
plt.plot(xpoints, ypoints)
plt.plot(xpoints, ypoints)
plt.plot(xpoints, ypoints)
plt.plot(xpoints, ypoints)

plt.show()

ypoints=np.array([3,8,1,10,5])

plt.plot(xpoints, ypoints, marker='o', markersize=10, color='red', linestyle='dashed', linewidth=2, label='Line with Markers')
plt.plot(xpoints, ypoints, marker='o', markersize=10, color='red', linestyle='dashed', linewidth=2, label='Line with Markers')

plt.show()


x=np.array([80,85,90,95,100,105,110,115,120,125,13013,135,140])
y=np.array([220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, ])
plt.plot(x,y)
plt.xlabel('Sports data')
plt.ylabel('Average pulse')
plt.title('Line Graph')
plt.show()
xAxis=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
yAxis=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

xAxis =[i+0.5 for i, i in enumerate(xAxis)]
plt.bar(xAxis, yAxis)
plt.title('Bar Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xticks([i +0.5 for i, i in enumerate(xAxis)], xAxis)
plt.show()