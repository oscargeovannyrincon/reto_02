'''/*
* DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */'''
numbers=list(range(10,56))
#print(numbers)
for number in numbers:
    if number%2==0:
        if number!=16:
            if number%3!=0:
                print(number)
                