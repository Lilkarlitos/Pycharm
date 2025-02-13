Nombre="Carlitos"
Apellido="Ruiz"
Especialidad="Estudiante"

# Primera forma concatenacion
print(Nombre+Apellido)

# Segunda forma de concatenacion
print("Mi nombre es: %s " %Nombre)
print("Mi nombre completo es:%s %s" %(Nombre,Apellido))

#Tercera forma de concatenacion
print("Mi nombre es: {0} y mi especialidad es {1} y mi apellido es {2}". format(Nombre,Especialidad,Apellido))

#Cuarta forma de concatenacion
print("Mi name es:{a} y mi apellido es :{b}".format(a=Nombre,b=Apellido))