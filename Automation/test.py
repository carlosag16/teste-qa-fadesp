from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://demo.automationtesting.in/Register.html"
driver.get(url)


try:
    

    # Realizando ações no site (exemplo: preenchendo um nome)
    input_firstName = driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[1]/div[1]/input")
    input_firstName.send_keys("José")

    # Realizando ações no site (exemplo: preenchendo um sobrenome)
    input_lastName = driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[1]/div[2]/input")
    input_lastName.send_keys("Costa")

    # Realizando ações no site (exemplo: preenchendo um endereço)
    input_address = driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[2]/div/textarea")
    input_address.send_keys("vila do conde, 32")

    # Realizando ações no site (exemplo: preenchendo um email)
    input_email = driver.find_element(By.XPATH, "//*[@id='eid']/input")
    input_email.send_keys("josecosta@gmail.com")

    # Realizando ações no site (preenchendo um telefone)
    input_phone = driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[4]/div/input")
    input_phone.send_keys("9180090000")

    #preencher gênero 
    input_gender = driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[5]/div/label[1]/input").click()
    #preencher hobbies
    input_hobbies = driver.find_element(By.ID, "checkbox2").click()
    
    #selecionar a lingua 
    input_languages = driver.find_element(By.ID, "msdd").click()
    select_language = driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[7]/div/multi-select/div[2]/ul/li[2]/a").click()

    #selecionar o skill pelo valor do input select
    multi_selector_skill = driver.find_element(By.ID,"Skills")
    select = Select(multi_selector_skill)
    select.select_by_value("Analytics")

    #selecionar o países pelo valor do input select
    multi_selector_country = driver.find_element(By.ID,"country")
    select = Select(multi_selector_country)
    select.select_by_value("Australia")

    #selecionar o ano de nascimento pelo valor do input select
    multi_selector_year = driver.find_element(By.ID,"yearbox")
    select = Select(multi_selector_year)
    select.select_by_value("1957")

    #selecionar o mês de nascimento pelo valor do input select
    multi_selector_month = driver.find_element(By.XPATH,"//*[@id='basicBootstrapForm']/div[11]/div[2]/select")
    select = Select(multi_selector_month)
    select.select_by_value("November")

    #selecionar o dia de nascimento pelo valor do input select
    multi_selector_day = driver.find_element(By.ID,"daybox")
    select = Select(multi_selector_day)
    select.select_by_value("9")

    password = "123456789"
    #preencher senha
    input_first_password = driver.find_element(By.ID, "firstpassword")
    input_first_password.send_keys(password)
    #preencher senha pela segunda vez
    input_second_password = driver.find_element(By.ID, "secondpassword")
    input_second_password.send_keys(password)

    #clicar no botão de submeter
    submit_button = driver.find_element(By.ID, "submitbtn").click()
    # Espera até que um elemento específico seja carregado na página (mensagem que não pode ser encontrada, mas usando id como exemplo)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mensagem"))
    )


finally:
    # Certificando-se de fechar o navegador, mesmo se ocorrer uma exceção
    driver.quit()
