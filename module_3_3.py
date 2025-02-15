# 1.Функция с параметрами по умолчанию:

def print_params(a=1, b='строка', c=True):                # Создаём функцию с пар-ми по умолчанию
    print(a, b, c)


print_params()                                            # Вызоваем функцию print_params
print_params(15, 'кошка')                           # с разным кол-вом аргументов, включая вызов без аргументов.

print_params(b=25)                                        # Проверяем, работают ли вызовы
print_params(c=[1, 2, 3])                                 # print_params(b = 25) print_params(c = [1,2,3])

# 2.Распаковка параметров:

values_list = [43, 'собака', False]                       # Создаём список с тремя элементами разных типов.
values_dict = {'a':8, 'b':'Попугай', 'c':True}            # Создаём словарь с тремя ключами, и значениями разных типов.

print_params(*values_list), print_params(**values_dict)   # Передаём пар-тры в функцию, используя распаковку (* и **).

# 3.Распаковка + отдельные параметры:

values_list_2 = [32, 'Банан']                             # Создаём список с двумя элементами разных типов.
print_params(*values_list_2, 42)                       # Проверяем, работает ли print_params(*values_list_2, 42)