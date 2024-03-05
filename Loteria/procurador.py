from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import json


def megasena_numb():
    driver = webdriver.Edge()
    driver.get('https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx')

    numeros = []
    passos = 0

    texto = driver.find_element(By.XPATH, '//span[@class="ng-binding"]')
    print(texto.text)

    while passos < 300:
        passos += 1
        bg = driver.find_elements(By.XPATH, "//li[@class='ng-binding ng-scope']")
        for i in bg:
            numeros += [i.text]
        numeros.sort()
        ant = driver.find_element(By.LINK_TEXT, '< Anterior')
        ant.click()
        sleep(1)

    texto = driver.find_element(By.XPATH, '//span[@class="ng-binding"]')
    print(texto.text)

    # salvando os números como dict
    tu = {}
    for i in numeros:
        tu[i] = numeros.count(i)
    # criando e salvando dict em um doc.text
    f = open('numeros_da_megasena.txt', 'w')
    for num, quant in tu.items():
        razao = 100*quant/300
        f.write(f'"{num}" : {quant},  {razao:.1f} \n')
    # salving dict as Json
    with open('numeros_da_megasena.json', 'w') as dog:
        json.dump(tu, dog)


def lotofacil_numb():
    driver = webdriver.Edge()
    driver.get('https://loterias.caixa.gov.br/Paginas/Lotofacil.aspx')

    numeros = []
    passos = 0

    texto = driver.find_element(By.XPATH, '//span[@class="ng-binding"]')
    print(texto.text)

    while passos < 300:
        passos += 1
        bg = driver.find_elements(By.XPATH, '//li[@class="ng-binding dezena ng-scope"]')
        for i in bg:
            numeros += [i.text]
        numeros.sort()
        ant = driver.find_element(By.LINK_TEXT, '< Anterior')
        ant.click()
        sleep(1)

    texto = driver.find_element(By.XPATH, '//span[@class="ng-binding"]')
    print(texto.text)

    # salvando os números como dict
    tu = {}
    for i in numeros:
        tu[i] = numeros.count(i)
    # criando e salvando dict em um doc.text
    f = open('numeros_da_lotofacil.txt', 'w')
    for num, quant in tu.items():
        razao = 100 * quant / 300
        f.write(f'"{num}" : {quant},  {razao:.1f} \n')
    # salving dict as Json
    with open('numeros_da_lotofacil.json', 'w') as dog:
        json.dump(tu, dog)


