import subprocess
import sys
import PySimpleGUI as sg

'''------------------------------------------------ download process ------------------------------------------------'''
def download_process(cmd):
    download_cmd = cmd
    sg.theme('DarkAmber')
    layout = [[sg.Text(size=(100, 10), font=('Helvetica', 10), justification='left', key='-OUTPUT-')],
              [sg.T(' ' * 120), sg.Button('done', font=('Helvetica', 14))]]
    window = sg.Window('downloading ......', layout, size=(600,350))

    with subprocess.Popen(download_cmd, shell=True, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as event1:
        for line in event1.stdout:
            event, values = window.read(timeout=1)
            window['-OUTPUT-'].update(line)
    window['-OUTPUT-'].update(' download completed ! ! !')
    while True:
        event, values = window.read(timeout=4)
        if event == 'done':
            break
        if (event == sg.WIN_CLOSED):
            sys.exit()
    window.close()


def advanced_optional(cmd, website, path):
    download_cmd = cmd
    sg.theme('DarkAmber')
    layout = [[sg.Text(size=(100, 30), font=('Helvetica', 10), justification='left', key='-OUTPUT-')],
              [sg.Text('please select most format code 請選擇左側格式碼', size=(25, 2), font=('Helvetica', 14), justification='left'), sg.InputText()],
              [sg.T(' ' * 120), sg.Button('ok', font=('Helvetica', 14))]]
    window = sg.Window('advanced option', layout, size=(640,640))
    output_list = []
    with subprocess.Popen(download_cmd, shell=True, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as event1:
        for line in event1.stdout:
            print(line)
            output_list.append(line)
            print(line)
    optional_list = ''.join(output_list)
    print(optional_list)
    event, values = window.read(timeout=1)
    window['-OUTPUT-'].update(optional_list)
    while True:
        event, values = window.read(timeout=4)
        if event == 'ok':
            break
        if (event == sg.WIN_CLOSED):
            sys.exit()
        format_code = values[0]
    window.close()


    download_cmd = '.\youtube-dl -f {} -o "{}\%(title)s.%(ext)s" {}'.format(format_code ,path, website)
    sg.theme('DarkAmber')
    layout = [[sg.Text(size=(100, 10), font=('Helvetica', 10), justification='left', key='-OUTPUT-')],
              [sg.T(' ' * 120), sg.Button('done', font=('Helvetica', 14))]]
    window = sg.Window('downloading ......', layout, size=(600,350))
    with subprocess.Popen(download_cmd, shell=True, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as event1:
        for line in event1.stdout:
            event, values = window.read(timeout=1)
            print(line)
            window['-OUTPUT-'].update(line)
    window['-OUTPUT-'].update(' download completed ! ! !')
    while True:
        event, values = window.read(timeout=4)
        if event == 'done':
            break
        if (event == sg.WIN_CLOSED):
            sys.exit()
    window.close()



def opening():
    sg.theme('DarkAmber')
    layout = [[sg.Text('Welcome to Youtuber download tool, please press the buttom to continue', size=(50, 2), font=('Helvetica', 14), justification='center')],
              [sg.Text('歡迎來到油管下載工具，點擊按鈕繼續', size=(100, 10), font=('Helvetica', 14), justification='center')],
              [sg.T(' ' * 100), sg.Button('continue', focus=True, font=('Helvetica', 14))]]
    window = sg.Window('Youtuber download tool', layout, size=(600,350))
    while True:
        event, values = window.read()
        if event == 'continue':
            break
        if (event == sg.WIN_CLOSED):
            sys.exit()
    window.close()

def select_mode():
    sg.theme('DarkAmber')
    layout = [[sg.Text('please select transform type', size=(50, 2), font=('Helvetica', 14), justification='center')],
              [sg.Text('請選擇轉換型式', size=(100, 5), font=('Helvetica', 14), justification='center')],
              [sg.T(' ' * 2), sg.Button('to mp4(轉mp4)', font=('Helvetica', 14)), sg.T(' ' * 5), sg.Button('to mp3(轉mp3)',
               font=('Helvetica', 14)), sg.T(' ' * 5), sg.Button('advanced(進階模式)', font=('Helvetica', 14))],
              [sg.T(' ' * 2), sg.Button('other formats(其他格式)', font=('Helvetica', 14))]]
    window = sg.Window('Youtuber download tool', layout, size=(600,350))
    while True:
        event, values = window.read()
        if event == 'to mp4(轉mp4)':
            mode = 1
            break
        if event == 'to mp3(轉mp3)':
            mode = 2
            break
        if event == 'advanced(進階模式)':
            mode = 3
            break
        if event == 'other formats(其他格式)':
            mode = 4
            break
        if (event == sg.WIN_CLOSED):
            sys.exit()
    window.close()
    return mode

def input_url():
    sg.theme('DarkAmber')
    layout = [[sg.Text('plesae input the URL', size=(50, 2), font=('Helvetica', 14), justification='center')],
              [sg.Text('請輸入油管網址', size=(50, 2), font=('Helvetica', 14), justification='center')],
              [sg.T(' ' * 25),sg.InputText(justification='center')],
              [sg.T('\n' * 20), sg.T(' ' * 120), sg.Button('Ok', font=('Helvetica', 14))]]
    window = sg.Window('Input URL', layout, size=(600,350))
    while True:
        event, values = window.read()
        youtube_url = values[0]
        if event == 'Ok':
            break
        if (event == sg.WIN_CLOSED):
            sys.exit()
    window.close()
    return youtube_url

def download_path():
    sg.theme('DarkAmber')
    file_path = sg.PopupGetFolder('選擇下載位置 select download path')
    while (file_path == ''):
    	file_path = sg.PopupGetFile('please select again')

    list = []
    for idx in range(0, len(file_path), 1):
        if(file_path[idx] == '/'):
            list.append('\\')
        else:
            list.append(file_path[idx])
    path = ''.join(list)
    return path

def other_format():
    sg.theme('DarkAmber')
    layout = [[sg.Text('please select format type', size=(50, 2), font=('Helvetica', 14), justification='center')],
              [sg.Text('請選擇轉換格式', size=(100, 5), font=('Helvetica', 14), justification='center')],
              [sg.T(' ' * 2), sg.Button('flv', font=('Helvetica', 14)), sg.T(' ' * 5), sg.Button('ogg', font=('Helvetica', 14)),
               sg.T(' ' * 5), sg.Button('webm', font=('Helvetica', 14)), sg.T(' ' * 5), sg.Button('mkv', font=('Helvetica', 14))
               , sg.T(' ' * 5), sg.Button('avi', font=('Helvetica', 14))],
              [sg.T(' ' * 2), sg.Button('wav', font=('Helvetica', 14)), sg.T(' ' * 5), sg.Button('best', font=('Helvetica', 14)),
               sg.T(' ' * 5), sg.Button('aac', font=('Helvetica', 14)), sg.T(' ' * 5), sg.Button('flac', font=('Helvetica', 14))
               , sg.T(' ' * 5), sg.Button('m4a', font=('Helvetica', 14))]]

    window = sg.Window('other formats', layout, size=(600,350))
    while True:
        event, values = window.read()
        if event == 'flv':
            format_type = 1
            break
        if event == 'ogg':
            format_type = 2
            break
        if event == 'webm':
            format_type = 3
            break
        if event == 'mkv':
            format_type = 4
            break
        if event == 'avi':
            format_type = 5
            break
        if event == 'wav':
            format_type = 6
            break
        if event == 'best':
            format_type = 7
            break
        if event == 'aac':
            format_type = 8
            break
        if event == 'flac':
            format_type = 9
            break
        if event == 'm4a':
            format_type = 10
            break
        if (event == sg.WIN_CLOSED):
            sys.exit()
    window.close()
    return format_type

def mp3_quality():
    sg.theme('DarkAmber')
    layout = [[sg.Text('please select mp3 quality', size=(50, 2), font=('Helvetica', 14), justification='center')],
              [sg.Text('請選擇mp3音訊品質', size=(100, 5), font=('Helvetica', 14), justification='center')],
              [sg.T(' ' * 20), sg.Button('worse(低)', font=('Helvetica', 14)), sg.T(' ' * 5), sg.Button('medium(中)',
               font=('Helvetica', 14)), sg.T(' ' * 5), sg.Button('best(高)', font=('Helvetica', 14))]]
    window = sg.Window('select mp3 quality', layout, size=(600,350))
    while True:
        event, values = window.read()
        if event == 'worse(低)':
            quality = 9
            break
        if event == 'medium(中)':
            quality = 4
            break
        if event == 'best(高)':
            quality = 0
            break
        if (event == sg.WIN_CLOSED):
            sys.exit()
    window.close()
    return quality


if __name__ == '__main__':
    opening()
    mode = select_mode()
    website = input_url()
    path = download_path()
    if mode == 1:
        command_line = '.\youtube-dl --format mp4 -o "{}\%(title)s.%(ext)s" {}'.format(path, website)
        print(command_line)
        download_process(command_line)
    elif mode == 2:
        quality = mp3_quality()
        command_line = '.\youtube-dl --extract-audio --audio-format mp3 --audio-quality {} -o "{}\%(title)s.%(ext)s" {}'.format(quality, path, website)
        download_process(command_line)
    elif mode == 3:
        command_line = '.\youtube-dl -F {}'.format(website)
        advanced_optional(command_line, website, path)
    elif mode == 4:
        format_type = other_format()
        type = ['flv', 'ogg', 'webm', 'mkv', 'avi', 'wav', 'best', 'aac', 'flac', 'm4a']
        if format_type <= 5:
            command_line = '.\youtube-dl --recode-video {} -o "{}\%(title)s.%(ext)s" {}'.format(type[format_type-1], path, website)
        else:
            command_line = '.\youtube-dl --extract-audio --audio-format {} -o "{}\%(title)s.%(ext)s" {}'.format(type[format_type-1], path, website)
        download_process(command_line)

#.\youtube-dl --format avi https://www.youtube.com/watch?v=hfgxAL3t2Tw
#download_cmd2 = '.\youtube-dl --extract-audio --audio-format mp3 -o "I:\Youtube downloader\download_place\%(title)s.%(ext)s" https://www.youtube.com/watch?v=hfgxAL3t2Tw'
#download_cmd3 = '.\youtube-dl --recode-video avi -o "I:\Youtube downloader\download_place\%(title)s.%(ext)s" https://www.youtube.com/watch?v=hfgxAL3t2Tw'
#download_cmd4 = '.\youtube-dl -F https://www.youtube.com/watch?v=hfgxAL3t2Tw'
''' audio format  "best", "aac","flac", "mp3", "m4a", "opus", "vorbis","wav" '''
''' video FORMAT  mp4,flv,ogg,webm,mkv,avi '''
