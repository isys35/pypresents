import os

print(os.environ)
print(os.getenv("TMP"))
print(os.getcwd())
os.chdir(r"D:\folder")
os.mkdir(r"D:\folder")
os.makedirs(r"D:\folder\first\second\third")
