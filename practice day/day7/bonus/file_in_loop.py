contents = [
    "To infinity and beyond",
    "Life is an Illusion",
    "May the force be with you"
]

fileNames = [
    "buz_lightyear.txt",
    "gravity_fall.txt",
    "star_wars.txt"
]

for contents, fileNames in zip(contents, fileNames):
    file = open(f"../files/{fileNames}", "w")
    file.writelines(contents)
    file.close()
