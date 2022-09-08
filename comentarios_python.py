num1 = 42 #variable numerica int
num2 = 2.3 #variable numerica float
boolean = True # booleano indica verdadero
string = 'Hello World' # variable que se llama string y es un string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #lista compuesta de string
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #diccionario compuesto de string, int, booleano
fruit = ('blueberry', 'strawberry', 'banana') #tupla de string que no puede ser modificada pero si se puede agregar un elemento
print(type(fruit)) #imprimir en consola de que tipo es fruit
print(pizza_toppings[1]) # imprimir el elemento que ocupa la posicion [1] en pizza_toppings
pizza_toppings.append('Mushrooms') # que se agrege mushrooms a la lista pizza_toppings al final
print(person['name']) # imprimir del diccionario person lo que hay en name
person['name'] = 'George'# para cambiar del diccionario person dentro de name a George
person['eye_color'] = 'blue'# como eye_color no existe dentro del diccionario person, se agrega mas su contenido blue
print(fruit[2]) #imprimir de la tupla fruit lo que ocupa en su posicion 2

if num1 > 45:# si num1 es mayor que 45
    print("It's greater") #imprime "It's greater"
else:  #si no
    print("It's lower")  #imprime "It's lower"

if len(string) < 5:   # si el largo que tiene la variable string 'hello world' es menor que 5 ojo el espacio se cuenta
    print("It's a short word!")  # imprime "It's a short word!"
elif len(string) > 15: # entonces si el largo de string es mayor que 15
    print("It's a long word!")  # imprime "It's a long word!"
else:   # si no 
    print("Just right!")  # imprime "Just right!"

for x in range(5): # dentro recorre x hasta 5, debiera ser desde 0 hasta 4 porque no toma el 5
    print(x) # imprime 0,1,2,3,4
for x in range(2,5): # dentro  recorre x donde comienza en 2 hasta el 4 porque el cinco no lo toma de uno en uno  
    print(x) # imprime 2,3,4
for x in range(2,10,3): # dentro  recorre x(2) hasta 10 de 3 en 3
    print(x) # imprime 2,5,8
x = 0 #  la variable x es igual a 0
while(x < 5): # ejecuta siempre que x sea menor que 5
    print(x) # imprime x
    x += 1 # x toma valor de x+1

pizza_toppings.pop() # la lista pizza_toppings saca el ultimo elemento
pizza_toppings.pop(1) # saca el elemento de la posicion 1

print(person) # imprime el diccionario person
person.pop('eye_color') # sacar 'eye_color' de diccionario person
print(person) # imprime diccionario person y va ha aparecer sin 'eye_color'

for topping in pizza_toppings: # desde la variable topping dentro  de pizza_toppings, va a dar el valor del elemento de la primera posicion a topping hasta que 
    if topping == 'Pepperoni':# se encuentre con el valor 'Pepperoni' si no es igual continua e imprime
        continue
    print('After 1st if statement')  #imprime 'After 1st if statement' y asi hasta que lo encuentre y sigue al if
    if topping == 'Olives':  # si topping es == 'Olives' continua el for hasta que lo encuentra y se quiebra
        break

def print_hello_ten_times(): # definicion de funcion .....
    for num in range(10):  # desde num recorre dentro hasta 9
        print('Hello')  #imprime ('Hello')

print_hello_ten_times() #ejecuta la funcion definida

def print_hello_x_times(x): # definicion de funcion ...
    for num in range(x): 
        print('Hello')

print_hello_x_times(4) #ejecuta la funcion definida

def print_hello_x_or_ten_times(x = 10): #definicion de funcion
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #ejecuta la funcion
print_hello_x_or_ten_times(4) # ejecuta la funcion


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)