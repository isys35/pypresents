message1 = "Global Variable"
def my_function():
    print("\nINSIDE THE FUNCTION")
    # Глобальные переменные доступны внутри функции
    print(message1)
    # Объявление локальной переменной
    message2 = "Local Variable"
    print(message2)


my_function()
print("\nOUTSIDE THE FUNCTION")
# Глобальные переменные доступны за пределами функции
print(message1)
# Локальные переменные НЕДОСТУПНЫ за пределами функции
print(message2)