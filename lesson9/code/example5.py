c = 1 # глобальная переменная
    
def add():
    c = c + 2 # прибавляем 2 к c 
    print(c)

add()
# UnboundLocalError: local variable 'c' referenced before assignment