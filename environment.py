'''
Created on 29 de mai de 2018

@author: mconceicaos
'''
from Pyautomators.Pywebautomator import Web
from Pyautomators import Pyambautomator

def before_all(context):
    context.path="C:/Users/mconceicaos/Desktop/"
    print(context.path)
    context.pagina=Web("Chrome", context.path)
    context.pagina.maximiza()
'''    
def before_step(context,step):
    context.pagina.atualizar()
    context.pagina.print_janela("steps.png")'''