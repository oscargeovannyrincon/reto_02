'''/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */'''
print('OPERADORES DE ASIGNACION \n')
x=5
print(f'Asignacion de un valor, x={x}')
x+=3
print(f'Operador += x+=3, x={x}')
x-=3
print(f'Operador -= x-=3, x={x}')
x*=3
print(f'Operador *= x*=3, x={x}')
x/=3
print(f'Operador /= x/=3, x={x}')
x%=3
print(f'Operador %= x%=3, x={x}')
x=27
x//=3
print(f'Operador //=, x=27, x//=3, x={x}')
x**=3
print(f'Operador **= x**=3, x={x}')
x=10
x&=15
print(f'Operador &=, x={x}')
x=10
x|=5
print(f'Operador |=, x={x}')
x=10
x^=5
print(f'Operador ^=, x={x}')
x>>=3
print(f'Operador >>= x>>=3, x={x}')
x<<=3
print(f'Operador <<= x<<=3, x={x}')

print('\nOPERADORES ARITMETICOS')
x=15
y=7
z=x+y
print(f"\nOperador +\nx={x}\ny={y}\n{x}+{y}={z}")
z=x-y
print(f"\nOperador -\n{x}-{y}={z}")
z=x*y
print(f"\nOperador *\n{x}*{y}={z}")
z=x/y
print(f"\nOperador /\n{x}/{y}={z}")
z=x%y
print(f"\nOperador %\n{x}%{y}={z}")
z=x**y
print(f"\nOperador **\n{x}**{y}={z}")
z=80//6
print(f"\nOperador //\n{x}//{y}={z}")

print('\nOPERADORES COMPARACION')
x=15
y=7
print(f'x={x}, y={y}')
print(f'\nOperador  IGUAL ==\nx==y=>{x==y}')
print(f'\nOperador NO ES IGUAL !=\nx==y=>{x!=y}')
print(f'\nOperador MAYOR QUE >\nx==y=>{x>y}')
print(f'\nOperador de MENOR QUE <\nx==y=>{x<y}')
print(f'\nOperador de MAYOR O IGUAL QUE >=\nx==y=>{x>=y}')
print(f'\nOperador de MENOR O IGUAL QUE <=\nx==y=>{x<=y}')


print('\nOPERADORES LOGICOS')
print('3 > 2 and 4 > 3', 3 > 2 and 4 > 3) 
print('3 > 2 and 4 < 3', 3 > 2 and 4 < 3) 
print('3 < 2 and 4 < 3', 3 < 2 and 4 < 3) 
print('True and True: ', True and True)
print('3 > 2 or 4 > 3', 3 > 2 or 4 > 3)  
print('3 > 2 or 4 < 3', 3 > 2 or 4 < 3)  
print('3 < 2 or 4 < 3', 3 < 2 or 4 < 3)  
print('True or False:', True or False)
print('not 3 > 2', not 3 > 2)     
print('not True=>', not True)      
print('not False=>', not False)     
print('not not True=>', not not True)  
print('not not False=>', not not False,'\n')
