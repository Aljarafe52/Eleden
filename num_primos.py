#Pequeño programa de inicio de estudios en Python
#Calcula los números primos dentro de unos límites
#Los resultados se pueden ver en el terminal y guardar en archivo .txt

#Crear variables

flag = 0

num_inicio = int(input("Número mínimo para encontrar los primos: "))
if num_inicio < 8:
    num_minimo = 8
    flag = 1
else:
    num_minimo = num_inicio
 
comp = 0 
while comp == 0 :   
    num_maximo = int(input("Número máximo para encontrar los primos: "))
    if num_maximo <= num_inicio:
        print("El número máximo tiene que ser mayor que el mínimo")
    else:
        comp=1

contador = num_minimo

my_path ="[My_path].txt" #[Sustituir por el path de tu archivo .txt]

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
             
#imprimir y guardar resultados

if num_inicio < 8:
    num_minimo = 1
    num_maximo = 8
    
if len(num_primos) != 0:
    print(f"Entre el {num_minimo} y el {num_maximo} hay {len(num_primos)} números primos que representan un {por_ciento}% de una muestra de {muestra} números.")
    preg = input("¿Quiere ver la lista completa? (S): ").lower()
else:
     print(f"Entre el {num_minimo} y el {num_maximo} no hay ningún número primo")
     preg = "n"

if preg == "s" and len(num_primos) !=0:
    print(num_primos)
    
    #guarda en archivo txt(lista_inicial)
    preg = input("¿Quiere guardar la lista en archivo .txt? (S): ").lower()
    if preg == "s":
        with open(my_path, 'a+')  as f:
            f.write(f"\nNúmeros primos del {num_inicio} al {num_maximo}\n")
            for i in num_primos:
                f.write(f"{i},")
        f.close()
else:
    if len(num_primos) != 0:
        print("No se mostrará  ni se guardará la lista")
    
