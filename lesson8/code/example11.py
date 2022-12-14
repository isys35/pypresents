def greet(name, msg):
    """
    Эта функция выводит 
    для человека с именем name
    сообщение msg.

    Если текст сообщения не передан,
    по умолчанию используется "Доброе
    утро!"
    """

    print("Привет, ", name + '. ' + msg)

# 2 именованных аргумента
greet(name = "Борис", msg = "Как дела?")

# 2 именованных аргумента (идут не по порядку)
greet(msg = "Как дела?", name = "Борис") 

# 1 позиционный, 1 именованный аргумент
greet("Борис", msg = "Как дела?")     
