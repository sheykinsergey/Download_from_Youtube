import pafy
import sys
import os

print('Введите URL видео или аудио')
# Получаем url к видео/аудио
url = input()

print('Скачать видео нажмите: 1 | Скачать аудио нажмите: 2')
#Выбор повлияет на то что будем качать видео или аудио
choice = input()

def download(choice):
    try:
        item = pafy.new(url)
        
        if choice == '1':
            streams = item.streams
        elif choice == '2':
            streams = item.audiostreams
        else:
            sys.exit()
        print('Выбрать качество видео: ') if choice == '1' else print('Выбрать качество аудио: ')
        
        streams_obj = {}
        count = 1

        for i in streams:
            streams_obj[count] = i
            print(f'{count}: {i}')
            count += 1
        i_count = int(input('Введите номер: '))
        result = streams[i_count - 1].download()

        
        
        # Если аудио файл то меняем расширение на .mp3
        if choice == '2':
            result = str(streams_obj[i_count])
            result = result.split('@')[0].split(':')[1]
            file_name = item.title
            audio_file = f'{file_name}.{result}'
            base = os.path.splitext(audio_file)[0]
            os.rename(audio_file, base + '.mp3')
            

        print('Скачивание завершено')
    except:
        print('Битая ссылка')


download(choice)