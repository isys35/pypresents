with open("examp.le", "r") as f: # 'Hello, world!'
    first_part = f.read(8)       # 'Hello, w'
    f.seek(4)
    second_part = f.read(8)      # 'o, world'