# Mostra informçoes do personagem dentro do game apertando control + C e depois Pause
# Como utilizar!
# 1 - Selecione o nome do player dentro do game 'Tibia Global' e aperte CTR + C
# 2 - Precione a tecla do teclado: Pause
# 3 - pronto ele vai informar o Nome, Level, Vocação do personagem
# Se preferir trocar a tecla vá até hotkeys linha 15 e coloque a tecla desejada!

import requests
from bs4 import BeautifulSoup
import keyboard
import pyautogui
import time
import pyperclip

# Hotkey
hotkey_show_info = "Pause"

# Função onde busca a informaçoes do char no site tibia.com
def escrevendo():
    text = pyperclip.paste()
    text = text.replace(" ", "+")
    url = f"https://www.tibia.com/community/?name={text}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Nome
    element_Name = soup.find(text="Name:")
    next_element_Name = element_Name.find_next()
    # Vocation
    element_Vocation = soup.find(text="Vocation:")
    next_element_Vocation = element_Vocation.find_next()
    # Nome
    element_Level = soup.find(text="Level:")
    next_element_Level = element_Level.find_next()

    pyautogui.write(next_element_Name.text+ " - Vocation: " + next_element_Vocation.text+ " -  Level: " + next_element_Level.text)
    
# Chama função 'escrevendo()' quando precionado a tecla que está setada em 'hotkey_show_info'
while True:
    if keyboard.is_pressed(hotkey_show_info):  # Avalanche
        escrevendo()
    time.sleep(0.1)