import archivoArff as fichero
import procesarImagen as pi

def escrbirFichero(nombre, tipos):
    fichero.abrirFichero(nombre + ".arff")
    fichero.relation(nombre)
    fichero.attribute("hu1", "numeric")
    fichero.attribute("hu2", "numeric")
    fichero.attribute("hu3", "numeric")
    fichero.attribute("hu4", "numeric")
    fichero.attribute("hu5", "numeric")
    fichero.attribute("hu6", "numeric")
    fichero.attribute("hu7", "numeric")
    fichero.attribute("h", "numeric")
    fichero.attribute("s", "numeric")
    fichero.attribute("v", "numeric")
    fichero.attributeArray("tipo",tipos)
    fichero.empezarDatos()

def aniadirDatos(carpeta, tipo):
    for foto in carpeta:
        imagen, hu, hsv = pi.buscarHU(foto)
        #pi.imprimirImagen(imagen, foto)
        array = []
        for h in hu:
            array.append(h[0])
        for valor in hsv:
            array.append(valor)
        array.append(tipo)
        fichero.escribirDatosArray(array)


def crearFichero(nombreFichero, carpeta):
    frutas = pi.lsCarpetas(carpeta)
    tipos = []
    for fruta in frutas:
        tipos.append(pi.getTipo(fruta))

    escrbirFichero(nombreFichero, tipos)

    for fruta in frutas:
        temp = pi.ls(fruta)
        aniadirDatos(temp, pi.getTipo(fruta))

    fichero.cerrarFichero()


crearFichero("FicherosArff/frutasEntrenamientoCompleto", "Fotos/fotosEntrenamientoCompleto")
crearFichero("FicherosArff/frutasTestCompleto", "Fotos/fotosTestCompleto")