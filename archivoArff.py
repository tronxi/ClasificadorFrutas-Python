f = None
def abrirFichero(nombre):
    global f
    f = open(nombre, "w")

def relation(relation):
    global f
    f.write("@relation " + relation + "\n")

def attribute(attribute, tipo):
    global f
    f.write("@attribute " + attribute + " " + tipo + "\n")

def attributeArray(attribute, tipo):
    global f
    cadena = ""
    f.write("@attribute " + attribute + " " + "{")
    for t in tipo:
        cadena += str(t) + ", "
    longitud = len(cadena)
    cadena = cadena[:longitud - 2]
    f.write(cadena + "}\n")
    

def cerrarFichero():
    global f
    f.close()

def empezarDatos():
    global f
    f.write("@data\n")

def escribirDatosString(datos):
    global f
    f.write(datos + "\n")

def escribirDatosArray(datos):
    global f
    cadena = ""
    for d in datos:
        cadena += str(d) +", "
    longitud = len(cadena)
    cadena = cadena[:longitud - 2]
    escribirDatosString(cadena)
