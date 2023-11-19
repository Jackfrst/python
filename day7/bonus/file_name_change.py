fileNames = [
    "1.buz_lightyear",
    "2.gravity_fall",
    "3.star_wars"
]

fileNames = [fileName.replace(".", "-") + ".txt" for fileName in fileNames]

print(fileNames)

# ['1-buz_lightyear.txt', '2-gravity_fall.txt', '3-star_wars.txt']
