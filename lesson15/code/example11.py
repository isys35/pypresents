import os
for root, directories, files in os.walk(r"D:\folder"):
    print(root)
    for directory in directories:
        print(directory)
    for file in files:
        print(file)

# D:\folder
# first
# D:\folder\first
# second
# D:\folder\first\second
# third
# D:\folder\first\second\third
# test.txt
