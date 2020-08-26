from PIL import Image
import requests
from io import BytesIO

origen = requests.get("http://onebitcoinpage.org/img/onebitcoinpage.png")
imagen = Image.open(BytesIO(origen.content))
tupla = imagen.size
lista = list(tupla)
valxstr = str(lista[0])
valystr = str(lista[1])
ws = (" ")
pxlamt = lista[0] * lista[1]

print("One Bitcoin Page Pixel Supply")
print("Type `getpixelsetinfo` to know the pixels supply")

inicio = input("onebitcoinpage-cli ")


def getpxl(lola):
    if lola == "getpixelsetinfo":
        print('{')
        print(ws,'"height": ', valystr + ',')
        print(ws,'"width": ', valxstr + ',')
        print(ws,'"lastblock": (0, 0, 0, 0),')
        print(ws,'"transactions ": 0.00000000,')
        print(ws,'"txouts": 0.00000000,')
        print(ws,'"pixel_size": 0,')
        print(ws,'"blank_size": 1000000,')
        print(ws,'"total_amount:', pxlamt)
        print('}')
    else:
        print("Unknown command: type `getpixelsetinfo` ")
        inicio = input("onebitcoinpage-cli ")
        getpxl(inicio)

getpxl(inicio)
