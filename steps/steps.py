'''
Created on 29 de mai de 2018

@author: mconceicaos
'''
from behave import *
from time import sleep
from selenium.webdriver.support.ui import Select
from django.db.models.expressions import When
from Pyautomators.Pywebautomator import Web
from Pyautomators import Pyambautomator 

@given("Estou na tela main")
def step_imple(context):
        context.pagina.pagina("http://www.submarino.com.br")
        
@when("Vou para tela de viagens")
def step_imple(context):
    pass

@then("aparece o titulo de viagem")    
def step_imple(context):
    pass
    
@given("estou na pagina de viagens")
def step_imple(context):
    context.pagina.pagina("https://www.submarinoviagens.com.br/index.aspx")

@when("preencho o formulario de busca")
def step_imple(context):
    context.pagina.clica("txtOrigin","id")
    context.pagina.escreve("txtOrigin","Sao Paulo","id")
    sleep(3)
    context.pagina.digitos("tab")
    sleep(3)
    context.pagina.clica("txtDestination","id")
    context.pagina.escreve("txtDestination","Roma","id")
    sleep(3)
    context.pagina.digitos("tab")
    sleep(3)
    context.pagina.escreve("txtOutboundPackage", "04062018", "id")
    context.pagina.escreve("txtInboundPackage", "04072018", "id")
    context.pagina.digitos("tab")
    slc = Select(context.pagina.elemento("drpAdultsQtd","id"))
    slc.select_by_value("2")
    slc = Select(context.pagina.elemento("drpChildrenQtd","id"))
    slc.select_by_value("1")
    context.pagina.clica("btnSearch","id")
            
    
@then("aparece o resultado da busca")
def step_imple(context):
    pass