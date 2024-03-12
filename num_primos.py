#Pequeño programa de inicio de estudios en Python
#Calcula los números primos dentro de unos límites
#Los resultados se pueden ver en el terminal y en archivo .txt

#Crear variables

flag = 0
num_inicio = int(input("Número mínimo para encontrar los primos: "))
if num_inicio < 8:
    num_minimo = 8
    flag = 1
else:
    num_minimo = num_inicio
    
num_maximo = int(input("Número máximo para encontrar los primos: "))
contador = num_minimo
my_path ="D:/Python_LDN/Practicas/Tutorial/my_files/primos.txt"

#Crear listas

lista_inicial = [2, 3, 5, 7] #para números menores de 8
num_primos= []

#Bucle principal

for contador in range (2, num_maximo+1, 1):
    for num_primo in lista_inicial:
        if contador % num_primo == 0:
            break
    else:
        lista_inicial.append(contador)

if flag == 0:
    for num_primo in lista_inicial:
        if num_primo < num_minimo:
            lista_inicial.remove(num_primo)
        else:
            num_primos.append(num_primo)
else:
    num_primos = lista_inicial 

muestra = (num_maximo - num_inicio) + 1
por_ciento = round((100 * int(len(num_primos)))/muestra, 2)
             
#imprimir resultados

if num_inicio < 8:
    num_minimo = num_inicio
    
print(f"Entre el {num_minimo} y el {num_maximo} hay {len(num_primos)} números primos que representan un {por_ciento}% de una muestra de {muestra} números.")
preg = input("¿Quiere ver la lista completa? (S): ").lower()

if preg == "s":
    print(num_primos)
    
    #guarda en archivo txt(lista_inicial)
    with open(my_path, 'a+')  as f:
        f.write(f"\nNúmeros primos del {num_inicio} al {num_maximo}\n")
        for i in num_primos:
            f.write(f"{i},")
    f.close()
    
else:
    print("No se mostrará la lista")
