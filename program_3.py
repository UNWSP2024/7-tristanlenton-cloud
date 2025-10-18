yearlyPop = [[]]
singleCity = []
moreInfo = True
while moreInfo:
    singleCity.append(int(input("Year: ")))
    singleCity.append(input("State: "))
    singleCity.append(int(input("Population: ")))
    yearlyPop.append(singleCity.copy())
    moreInfo = input("Continue? (y/n): ")
    if moreInfo == "n":
        moreInfo = False
    singleCity.clear()
year = (int(input("Year: ")))
total = 0
for num in range(len(yearlyPop)):
    if yearlyPop[num][0] == year:
        total += yearlyPop[num][2]
