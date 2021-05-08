# -*- coding: utf-8 -*-
from pywikibot import pagegenerators as pg
import pywikibot
import aosbot as tools

def write(data, filename, mode='a'):
    """
    Escribe un archivo filename con los datos enviados en data
    
    @param data: datos a escribir
    @type data: string
    @param filename: nombre del archivo
    @type data: string
    @param mode: tipo de apertura del archivo
    @type data: string
    
    """
    f = open(filename, mode, encoding='utf8')
    f.write(data + '\n')
    f.close()

def obtener_data(archivo, separador="\t"):
    """
    obtener_data(archivo, separador="\t"):
        Obtiene los contenidos del archivo que usa el separador \t
    """
    data = []
    with open(archivo, encoding="utf-8") as f:
        for line in f.readlines():
            data.append(line.split(separador))
    return data
    
# para recoger todas las referencias de un artículo
def main():
    site = pywikibot.Site("en", "wikipedia")
    paginas = tools.obtener_data('../aosbot/entry.txt')
    for articles in paginas:
        gen = [pywikibot.Page(site, title=articles[0])]
        articles = pg.PreloadingGenerator(gen)
        for page in articles:
            try:
                if page.isRedirectPage():
                    page = page.getRedirectTarget()
                texto=page.get()
                nueva=texto.split("<ref")
                print("<<<<<<<<<<<<<< {0} ".format(page.title()))
                nueva.pop(0) # para borrar lo que coge antes del separador
                for url in nueva:
                    definir=url.split("\n")
                    definitiva=definir[0]
                    f = open ("../aosbot/references.txt", "a", encoding="utf-8")
                    f.write(str(page.title()) + "$" + str(definitiva[:2000]) + '\n')
                    f.close()
            except:
                f = open ("../aosbot/errores.txt", "a", encoding="utf-8")
                f.write(str(page.title()) + '\n')
                f.close()
                
if __name__ == "__main__":
    main()