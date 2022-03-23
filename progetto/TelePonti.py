import PySimpleGUI as sg
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

token= "5255941942:AAEF1A2rhMX-FxFMbOLw4PNGrDqIlT5K0rc"
chat_id= "-1001170843214"
bot = telegram.Bot(token=token)

def telegram(values):
    try:
        bot.send_message(chat_id=chat_id, text=values['msg'])
        sg.popup_quick_message('messaggio inviato correttamente', grab_anywhere=True)
    except Exception as ex:
        sg.Popup('nessun messaggio inserito: riprovare', title='ERROR',icon='images/icona.ico',grab_anywhere=True)

def telegram_allegato(values):
    try:
        bot.send_photo(chat_id=chat_id, photo=open(values['img'], 'rb'))
        sg.popup_quick_message('immagine inviata correttamente',grab_anywhere=True)
        window['img'].update("")
    except Exception as ex:
        sg.popup("    immagine non inserita: riprovare   ", icon='images/icona.ico',grab_anywhere=True)

sg.theme('LightPurple')
   
layout_column = [[sg.Button('invia', key="messaggio", font=('Sans-serif', 13)), 
    sg.FilesBrowse('allega', font=('Sans-serif', 13), target='img', file_types=(("JPEG", ".jpg"), ("PNG", ".png")))]]
    
layout_Crediti = [[sg.Text(""'v1.0 Matteo Corda®', pad=[10,0], font=('Sans-serif', 8))]]

layout = [  [sg.Text('inserire messaggio:', pad=[10,5], font=('Sans-serif', 10, 'bold'))],
            [sg.Multiline(default_text='messaggio...', key='msg', size=(70,13), no_scrollbar=True, pad=[10,0])],
            [sg.Input(key='img', enable_events=True, visible=False, expand_x=True, default_text='allegato', pad=[10,5])],
            [sg.Column(layout_column, expand_x=True, element_justification='center', pad=[10,15])],
            [sg.Column(layout_Crediti, expand_x=True, element_justification='right')]   
        ]          

window = sg.Window('TelePonti', grab_anywhere =True, margins = (0, 0), icon='images/icona.ico').Layout(layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED :
        break
    if event =='img': 
        telegram_allegato(values) 
    if event =='messaggio': 
        telegram(values)
window.close()