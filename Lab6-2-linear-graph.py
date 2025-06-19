import matplotlib.pyplot as plt

print("This program will graph a line when given the slope and the intercept.")
print("Please enter the values for m and b given the form y = mx + b")

#the try / except input validation technique hasn't been covered in the book chapters yet,
#but was mentioned in Mr Geiger's video "Py - More List Methods - Index-Sort-Min-Max"
#So I am hoping it is acceptable to use. 
while True:
    try:
        m = float(input("m: "))
        break
    except ValueError:
        print("Please enter a valid number for the slope (m)")    
while True:
    try:
        b = float(input("b: "))
        break
    except ValueError:
        print("Please enter a valid bumber for the y intercept (b)") 

#Use list comprehension to populate a list with values for x from -20 to 20 and assign
    #to the variable x_coordinates.
x_coordinates = [x for x in range(-20, 21)]
#Use list comprehension to populate a list with values for y based on equation and 
    #assign to variable y_coordinates
y_coordinates = [(m * x + b) for x in x_coordinates]

#turn on the x and y axis
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")

#force grid to be a square
plt.axis("square")

#set the limits for the x and y axis on the graph
plt.xlim(xmin=-20, xmax=20)
plt.ylim(ymin=-20, ymax=20)

#turn on the grid
plt.grid(True)

#plot the cordinates to create the slope
plt.plot(x_coordinates, y_coordinates)

#display the graph
plt.show()

