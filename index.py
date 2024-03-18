import pywhatkit
import pyautogui
import keyboard

#DENTRO DAS AS ASPAS DUPLAS, ADICONA O NÚMERO NO QUAL DESEJA ENVIAR A MENSAGEM.
listNumber = ['', '']

for number in listNumber:
    #DENTRO DAS ASPAS DUPLAS, ADICIONA A MENSAGEM QUE DESEJA ENVIAR
    pywhatkit.sendwhatmsg_i(number, '')
    pyautogui.click(1050, 950)
    keyboard.press_and_release('enter')
