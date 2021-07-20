# Python Program to illustrate Linear Plotting
'''
import matplotlib.pyplot as plt
 month contains the x-axis values  and India & BD  are the y-axis values for plotting
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
India = [100.6, 158.61, 305.54, 394.96, 724.79]
BD = [10.5, 25.21, 58.65, 119.27, 274.87]
 plotting of x-axis(year) and y-axis(COVID Infections) with different colored labels of two countries.
plt.plot(month, India, color ='orange', marker='o', label ='India')
plt.plot(month, BD, color ='g', marker='s', label ='Bangladesh')
 naming of x-axis and y-axis
plt.xlabel('Months-2021')
plt.ylabel('COVID-19 infection rate')
plt.grid()
 naming the title of the plot
plt.title('COVID-19 infections in 2021 of India and Bangladesh')
plt.legend()
plt.show()
'''


# Python Program to illustrate Linear Plotting
import matplotlib.pyplot as plt
# month contains the x-axis values  and India & BD  are the y-axis values for plotting
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
India = [100.6, 158.61, 305.54, 394.96, 724.79]
BD = [10.5, 25.21, 58.65, 119.27, 274.87]

# plotting of x-axis(year) and  y-axis(COVID Infections) with different colored labels of two countries.

plt.plot(month, India, color ='orange', marker ='o', markersize = 12, label ='India')
plt.plot(month, BD, color ='g', linestyle ='dashed', linewidth = 2, marker='s', label ='Bangladesh')
# giving the grid lines
plt.grid(True)
# naming of x-axis and y-axis
plt.xlabel('Months-2021')
plt.ylabel('COVID-19 infection rate')

# naming the title of the plot

plt.title('COVID-19 infections in 2021 of India and Bangladesh')
plt.legend()
plt.show()

