spam=True
print(spam)

#se pueden comparar numeros, booleanos, strings "==","<",">".
print(45==45) #True
print(45==5) #False
print("hola"=="hola") #True

#operadores and y or
a=11
b=11
c=20
d=20
print(a==b and c==d) #cuando se usa or, se evalúa la primera de izq a der

not False
print(not False)

print(4<5 and 7>8) #false
print(4<5 or 7>8) #true

#if, :, elif y else

nombre=input("Dame tu nombre\n")
if(nombre=="Daniel"):
 print("Hola Daniel")
 print("Cómo estás?")
elif(nombre=="Juan" or nombre=="Daniela"):  
  
  #si se pone un if normal, se toma como nueva orden y el else cambia al nuevo if
  
 print("Hola de nuevo Invitado")
else:
 print("No te conozco")

a=10
b=10
c=20
d=20
print(a==b and not c==d) #si hay not, se convierte a lo contrario, la prioridad del not es más alta que el and/or y == 






















