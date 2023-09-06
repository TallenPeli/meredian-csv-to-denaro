import matplotlib.pyplot as plt
import csv

# Lists to store the data
x = []
y1 = []
y2 = []

# Read data from the file and reverse it
with open("string.txt", "r") as file:
    reader = csv.reader(file)
    data = list(reader)[1:]  # Skip the header line and convert to a list
    data.reverse()  # Reverse the list

for i, row in enumerate(data):
    x.append(i + 1)  # Increase X by 1 for each row
    y1.append(float(row[0]))
    y2.append(float(row[1]))

# Create the plot
plt.plot(x, y1, label="Purchase Value", color="Orange")
plt.plot(x, y2, label="Total", color="Blue")

# Add labels and title
plt.xlabel("Purchases")
plt.ylabel("Total Money")
plt.title("Money Graph")

# Add a legend
plt.legend()

# Set a custom resolution (dpi)
custom_dpi = 300  # Change this to your desired resolution
plt.savefig("graph.png", dpi=400)

# Display the graph (optional)
plt.show()

