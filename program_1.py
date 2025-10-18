rainfall = []
for month in range(1,13):
    rainfall.append(float(input("Enter the rainfall in inches: ")))
sum = sum(rainfall)
print("Total rainfall is", sum, "inches")
print("Average rainfall is", sum/len(rainfall), "inches")
print("Most amount of rainfall was", max(rainfall), "inches")
print("Least amount of rainfall was", min(rainfall), "inches")