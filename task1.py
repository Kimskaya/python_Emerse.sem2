"""Напишите программу, которая получает целое число
и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата."""

#Шестнадцатеричные цифры
h_nums = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',
          8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}

n = int(input('Введите целое десятичное число: '))
hex_n = hex(n)   #Вычисляем 16тиричное представление n при помощи hex()

#Вычисляем 16тиричное представление n "вручную"
calculate_n = ''
while n>0:
    #Вычисляем 16тиричную цифру и добавляем её к числу
    calculate_n = h_nums[n%16] + calculate_n
    #Делим нацело n на 16
    n //= 16
    
print(f'Без использования hex: 0x{calculate_n}')
print(f'С использованием hex:  {hex_n}')
