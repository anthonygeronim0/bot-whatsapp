import pywhatkit
import pyautogui
import keyboard

listNumber = ['+5579998336721', '+5579998173662']

for number in listNumber:
    pywhatkit.sendwhats_image(number, "C:/Users/antho/OneDrive/Área de Trabalho/receba", 'Você recebeu a inteligência do BOT criado por Anthony Geronimo. Agora seu QI aumentou 200%.')
    pyautogui.click(1050, 950)
    keyboard.press_and_release('enter')