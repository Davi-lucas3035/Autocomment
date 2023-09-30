from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def fazer_login(usuario, senha):
    driver = webdriver.Chrome()  # Certifique-se de ter o ChromeDriver instalado e no PATH
    driver.get("https://www.instagram.com/")
    time.sleep(5)

    # Localiza os campos de login e senha e os preenche
    username_input = driver.find_element_by_name("Davi_lucas3035")
    password_input = driver.find_element_by_name("kerlly05102004")
    username_input.send_keys(Davi_lucas3035)
    password_input.send_keys(kerlly05102004)

    # Faz login
    login_button = driver.find_element_by_xpath('//button[@type="submit"]')
    login_button.click()
    time.sleep(4)

    # Fecha pop-up de notificações, se houver
    try:
        not_now_button = driver.find_element_by_xpath('//button[text()="Agora não"]')
        not_now_button.click()
    except Exception:
        pass

    return driver

def fazer_comentario(driver, url_postagem, comentario):
    driver.get(url_postagem)
    time.sleep(2)

    # Encontra a área de comentários e digita o comentário
    comment_input = driver.find_element_by_xpath('//textarea[@placeholder="Adicione um comentário..."]')
    comment_input.send_keys(comentario)
    comment_input.send_keys(Keys.ENTER)
    time.sleep(2)

    print(f"Comentário '{comentario}' postado com sucesso!")

def main():
    # Substitua 'seu_usuario' e 'sua_senha' pelas suas credenciais do Instagram
    usuario = "Davi_Lucas3035"
    senha = "kerlly05102004"
    comentario = "Este é um comentário de exemplo!"

    driver = fazer_login(Davi_Lucas3035, kerlly05102004)

    # Substitua 'URL_DO_POST' pela URL da postagem em que você deseja fazer o comentário
    url_postagem = "https://www.instagram.com/p/CuKglHuusVn/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=="

    fazer_comentario(driver, url_postagem, comentario)

    # Encerra o navegador
    driver.quit()

if __name__ == "__main__":
    main()
