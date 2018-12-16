import numpy as np 
import cv2
import colorsys
from matplotlib import pyplot as plt
from os import scandir, getcwd
from os.path import abspath

def buscarHU(imagen):
    imagen = cv2.imread(imagen, cv2.IMREAD_COLOR)
    imagen = cv2.GaussianBlur(imagen ,(9,9),0)
    imagenRGB = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    imgray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

    ret, thresh = cv2.threshold(imgray, 250, 255, cv2.THRESH_BINARY_INV)

    im2, contornos, jerarquía = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contornosGrandes = []
    areas = []
    for i in contornos:
        areas.append(cv2.contourArea(i))

    for i in contornos:
        if(cv2.contourArea(i) == max(areas)):
            contornosGrandes.append(i)      

    cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    cv2.drawContours(imagen, contornosGrandes,-1, (255,0,0), 1)

    HU = cv2.HuMoments(cv2.moments(contornosGrandes[0]))
    r, g, b = pixelRGB(imagenRGB)
    h, s, v = rgb_hsv(r, g, b)
    hsv = []
    hsv.append(h)
    hsv.append(s)
    hsv.append(v)
    return imagen, HU, hsv

def pixelRGB(imagen):
    x = 45
    y = 45
    rT = 0
    gT = 0
    bT = 0
    for i in range(5):
        for j in range(5):
            r = imagen[x + i, y + j, 0]
            g = imagen[x + i, y + j, 1]
            b = imagen[x + i, y + j, 2]

            rT += r
            gT += g
            bT += b
            
    rF = rT / 25
    gF = gT / 25 
    bF = bT / 25

    #print("r = " + str(rF) + " g = " + str(gF) + " b = " + str(bF))
    return rF, gF, bF

def rgb_hsv(r, g, b):
    r = r/255
    g = g/255
    b = b/255
    h,s,v = colorsys.rgb_to_hsv( r , g , b )
    h = h * 360
    s = s * 100
    v = v * 100
    #print("h = " + str(h) + " s = " + str(s) + " v = " + str(v))
    return h, s, v



def imprimirImagen(imagen, titulo = ""):
    plt.subplot(111), plt.title(titulo), plt.axis("off")
    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
    plt.show()

def imprimirImagenGris(imagen):
    hist = cv2.calcHist([imagen], [0], None, [256], [0,256])
    cv2.imshow('imagen', imagen)
    plt.subplot(212), plt.title('histo')
    plt.hist(imagen.ravel(), 256, [0,256])
    plt.show()
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()

def getTipo(cadena):
    pos = cadena[::-1].find("\\")
    return cadena[len(cadena) - pos:].replace(" ", "_")

def ls(ruta = '.'):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]

def lsCarpetas(ruta = '.'):
    return [abspath(arch.path) for arch in scandir(ruta)]