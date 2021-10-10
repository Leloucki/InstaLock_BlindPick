import pyautogui
import time
import PySimpleGUI as sg
import keyboard
import threading

def stopLoop():
    global loop
    loop = False

def startLoop():
    global loop
    loop = True

def instaLock(laneInput, champInput):
    print('dentro de instalock')
    lane = laneInput
    champN = str.lower(champInput)
    choose = 'menu/jungle.png'
    global loop

    while loop:
        print('esperando tela de aceitar ou seleçao de campeao')
        aceitarP = pyautogui.locateCenterOnScreen('menu/aceitar.png', confidence=0.8)
        if aceitarP != None:
            pyautogui.click(aceitarP)

        pesqP = pyautogui.locateCenterOnScreen('menu/pesquisa.png', confidence=0.8, grayscale=True)
        if pesqP != None:
            print('pesquisa encontrada')
            pyautogui.click(pesqP)
            pyautogui.write(champN)

            time.sleep(0.3)
            if champN == 'vi':
                champP = pyautogui.locateCenterOnScreen(f'champs/{champN}.png', confidence=0.8)
                pyautogui.click(champP)
            else:
                champP = pyautogui.locateCenterOnScreen(choose, confidence=0.8)
                champP = (champP.x - 15, champP.y + 80)
                pyautogui.click(champP)

            time.sleep(0.3)
            confirmP = pyautogui.locateCenterOnScreen('menu/confirm.png', confidence=0.8)
            pyautogui.click(confirmP)

            while 1:
                if pyautogui.locateOnScreen('menu/conectando_chat.png', confidence=0.8) is None:
                    chatP = pyautogui.locateCenterOnScreen('menu/chat.png', confidence=0.8)
                    pyautogui.click(chatP)
                    pyautogui.write(lane)
                    pyautogui.hotkey('Enter')
                    break
            break


if __name__ == '__main__':
    layout = [
        [sg.Text('Champ', size=(8, 0), pad=10), sg.Input(size=(15, 0), pad=10, key='champ')],
        [sg.Text('Lane', size=(8, 0), pad=10), sg.Input(size=(15, 0), pad=10, key='lane')],
        [sg.Button('Run'), sg.Button('Stop')]
    ]

    janela = sg.Window('InstaLock_BlindPick').layout(layout)
    loop = True
    while True:
        event, values = janela.Read()

        if event == 'Run':
            champ = values['champ']
            lane = values['lane']
            stopLoop()
            time.sleep(0.5)
            startLoop()
            t = threading.Thread(target=instaLock, args=(lane, champ,))
            t.start()
        if event == 'Stop':
            stopLoop()
        if event == sg.WIN_CLOSED:
            stopLoop()
            break
