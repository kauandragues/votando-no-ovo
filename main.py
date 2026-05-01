from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import time
import os


def configurar_webdriver():
    load_dotenv()
    url = os.getenv("FORM_URL")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get(url)
    return driver


def preencher_formulario(driver):
    lista_de_vencedores = [
        "i6",
        "i35",
        "i46",
        "i81",
        "i98",
        "i115",
        "i144",
        "i152",
        "i169",
        "i186",
        "i203",
        "i220",
        "i237",
        "i254",
    ]

    for vencedor in lista_de_vencedores:
        escolhido = driver.find_element(By.ID, vencedor)
        escolhido.click()


def enviar_formulario(driver):
    botao_enviar = driver.find_element(By.XPATH, "//span[text()='Enviar']")
    botao_enviar.click()


def voltar_para_formulario(driver):
    voltar = driver.find_element(By.XPATH, "//a[text()='Enviar outra resposta']")
    voltar.click()


def main():
    driver = configurar_webdriver()
    numero_de_envios = 0
    limite_de_envios = 50
    try:
        while numero_de_envios < limite_de_envios:

            numero_de_envios += 1
            print(f"Formulário nº{numero_de_envios}")

            preencher_formulario(driver)
            print("Formulário preenchido!")
            time.sleep(3)

            enviar_formulario(driver)
            print("Formulário enviado!")
            time.sleep(3)

            voltar_para_formulario(driver)
            print("Indo para o próximo formulário!")
            print("---------------------------------------------\n")
            time.sleep(3)
    except KeyboardInterrupt:
        print("========= Parando o programa! =========")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
