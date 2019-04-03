# -*- coding: utf-8 -*-

def main():
    print('Mision 07')
    print('----------------------------------')
    print('1. Calcular divisiones')
    print('2. Encontrar el mayor')
    print('3. Salir')
    print('----------------------------------')
    usr=input('Teclea tu opcion: ')
    if usr=='1':
        print()
        dividendo=int(input('Dividendo: '))
        divisor=int(input('Divisor: '))
        dividir(dividendo,divisor)
        return main()
    elif usr=='2':
        print()
        encontrarMayor()
        return main()
    elif usr=='3':
        exit()
    else:
        print('Reintente...entrada invalida')
        return main()
    
def dividir(dividendo,divisor):
    resultado = 0
    residuo = dividendo
    while(residuo>=divisor):
        residuo = residuo - divisor
        resultado+=1
    print(dividendo,'/',divisor,'=',resultado,', sobra',residuo)
    print()
    
def encontrarMayor():
    print('Teclea una serie de números para encontrar el mayor ')
    num=int(input('Teclea un número [-1 para salir]: '))
    mayor=-1
    while(num!=-1):
        num=int(input('Teclea un número [-1 para salir]: '))
        if mayor<num:
            mayor=num
    if mayor!=-1:
        print('El mayor es: ',mayor)
        print()
    else:
        print('No hay valor menor')
        print()
    
main()