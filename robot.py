from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import openpyxl as xl

def cadastro_web(dataframe):

    # Logging in to the system
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('http://automacao.empowerdata.com.br/')
    #time.sleep(2)

    email = browser.find_element(By.XPATH, '//*[@id="email"]')
    email.send_keys('aluno@empowerdata.com.br')
    #time.sleep(1)
    email.send_keys(Keys.TAB)

    login = browser.find_element(By.XPATH, '//*[@id="password"]')
    login.send_keys('empowerpython')

    time.sleep(2)

    botao_entrar = browser.find_element(By.XPATH, '//*[@id="submit"]').click()
    time.sleep(3)

    # Reading all dataframe rows
    for _, linha in dataframe.iterrows():

        cliente = browser.find_element(By.XPATH, '//*[@id="nome"]')
        cliente.send_keys(linha['Nome'])

        email_cliente = browser.find_element(By.XPATH, '//*[@id="email"]')
        email_cliente.send_keys(linha['E-mail'])

        telefone = browser.find_element(By.XPATH, '//*[@id="telefone"]')
        telefone.send_keys(linha['Telefone'])

        cidade = browser.find_element(By.XPATH, '//*[@id="cidade"]')
        cidade.send_keys(linha['Cidade'])

        estado = browser.find_element(By.XPATH, '//*[@id="estado"]')
        estado.send_keys(linha['Estado'])

        time.sleep(2)

        botao_cadastrar = browser.find_element(By.XPATH, '//*[@id="submit"]').click()

        time.sleep(3)

    browser.close()