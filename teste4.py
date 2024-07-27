import keyboard
from playwright.sync_api import sync_playwright
import time
import requests
import speech_recognition as sr

# Informações de login
email = 'annyhirosh@gmail.com'
password = 'Anny@2024@1991'

# Função para baixar o áudio do CAPTCHA
def download_audio(url, file_path):
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)

# Função para transcrever o áudio usando reconhecimento de fala
def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
        return recognizer.recognize_google(audio, language='pt-BR')

# Função principal usando Playwright
def main():
    with sync_playwright() as p:
        # Inicializar o navegador
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(user_agent='Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36')
        page = context.new_page()

        # Abrir a página de login
        page.goto('https://login.sejaefi.com.br/?cache')

        # Esperar até que os campos de email e senha estejam presentes e preenchê-los
        page.fill('//input[@placeholder="Digite aqui" and @type="text"]', email)
        page.fill('//input[@placeholder="Digite aqui" and @type="password"]', password)

        # Esperar até que o iframe do reCAPTCHA esteja presente
        page.wait_for_selector('//iframe[@title="reCAPTCHA"]')

        # Esperar até que uma tecla seja pressionada para resolver o CAPTCHA
        print("Pressione 'r' para resolver o CAPTCHA")
        keyboard.wait('r')

        # Re-obter o iframe imediatamente antes de interagir com ele para evitar stale element reference
        recaptcha_iframe = page.frame_locator('//iframe[@title="reCAPTCHA"]').first
        recaptcha_iframe.locator('span[role="checkbox"]').click()

        # Esperar alguns segundos para que o reCAPTCHA seja carregado
        time.sleep(5)

        # Aguardar até que o iframe do CAPTCHA com o botão de áudio esteja presente
        page.wait_for_selector('//iframe[contains(@src, "bframe")]')

        # Re-obter o iframe do CAPTCHA de áudio
        audio_iframe = page.frame_locator('//iframe[contains(@src, "bframe")]').first
        
        # Esperar até que o botão de áudio esteja presente e clicar nele
        audio_iframe.locator('#recaptcha-audio-button').click()
        
        # Esperar até que o link do áudio esteja presente e obter o link
        time.sleep(3)  # Ajuste o tempo conforme necessário
        audio_src = audio_iframe.locator('audio').get_attribute('src')
        print(f'Link do áudio: {audio_src}')



        # Preencher o campo de resposta com a transcrição
        audio_iframe.locator('#audio-response').fill("eaeman")
        
        # Clicar no botão de verificação
        audio_iframe.locator('#recaptcha-verify-button').click()

        input('Pressione Enter para sair')

        # Fechar o navegador após as operações
        browser.close()

# Executar a função principal
if __name__ == "__main__":
    main()
