import PySimpleGUI as sg
import sys

'''----------------  browser the install path  ----------------'''
sg.theme('DarkAmber')

layout = [[sg.Text('Welcome to Youtuber download tool, please press the buttom to continue', size=(50, 2), font=('Helvetica', 14), justification='center')],
          [sg.Text('歡迎來到油管下載工具，點擊按鈕繼續', size=(100, 10), font=('Helvetica', 14), justification='center')],
          [sg.T(' ' * 100), sg.Button('continue', focus=True, font=('Helvetica', 14))]]
window = sg.Window('Youtuber download tool', layout, size=(600,350))
while True:
    event, values = window.read(timeout=4)
    if event == 'continue':
        break
    if (event == sg.WIN_CLOSED):
        sys.exit()
window.close()

layout = [[sg.Text('please select transform type', size=(50, 2), font=('Helvetica', 14), justification='center')],
          [sg.Text('請選擇轉換型式', size=(100, 5), font=('Helvetica', 14), justification='center')],
          [sg.T(' ' * 2), sg.Button('to mp4(轉mp4)', font=('Helvetica', 14)), sg.T(' ' * 5), sg.Button('to mp3(轉mp3)',
           font=('Helvetica', 14)), sg.T(' ' * 5), sg.Button('advanced(進階模式)', font=('Helvetica', 14))]]
window = sg.Window('Youtuber download tool', layout, size=(600,350))
while True:
    event, values = window.read(timeout=4)
    if event == 'to mp4(轉mp4)':
        mode = 1
        break
    if event == 'to mp3(轉mp3)':
        mode = 2
        break
    if event == 'advanced(進階模式)':
        mode = 3
        break
    if (event == sg.WIN_CLOSED):
        sys.exit()
window.close()





layout = [[sg.Text('plesae input the URL', size=(50, 2), font=('Helvetica', 14), justification='center')],
          [sg.Text('請輸入油管網址', size=(50, 2), font=('Helvetica', 14), justification='center')],
          [sg.T(' ' * 25),sg.InputText(justification='center')],
          [sg.T('\n' * 20), sg.T(' ' * 120), sg.Button('Ok', font=('Helvetica', 14))]]
window = sg.Window('Input URL', layout, size=(600,350))

while True:
    event, values = window.read(timeout=4)
    youtube_url = values[0]
    if event == 'Ok':
        break
    if (event == sg.WIN_CLOSED):
        sys.exit()

window.close()




file_path = sg.PopupGetFolder('選擇下載位置 select download path ')
print(file_path)
while (file_path == ''):
	file_path = sg.PopupGetFile('please select again')
	print(file_path)
