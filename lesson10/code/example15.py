myfile = open(r'С:\misc\data')
try:
    for line in myfile:
        print(line)
finally:
    myfile.close()