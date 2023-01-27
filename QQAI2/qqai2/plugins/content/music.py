import re
import os
import json
import requests
import config.yml_DATA
def music(name:str):
    try:
        number = re.findall(re.compile('(\d+)'), name)
        Str = ''
        for i in number:
            Str = Str + i
        if len(Str) == len(name):
            ID = int(name)
            return ['http://music.163.com/song/media/outer/url?id=' + str(ID) + '.mp3']
        else:
            print(f'{config.yml_DATA.music_API}search?keywords={name}')
            IdData = requests.get(f'{config.yml_DATA.music_API}search?keywords={name}')
            ID = json.loads(IdData.text)['result']['songs'][0]['id']
            return ['http://music.163.com/song/media/outer/url?id='+str(ID)+'.mp3']
    except:
        return '无效API！'
def MusicDownload(name: str):
    if not os.path.exists(config.yml_DATA.music_File):
        os.mkdir(config.yml_DATA.music_File)
    print(name)
    data = requests.get(music(name)[0]).content
    with open(f'{config.yml_DATA.music_File}/{name}.aac', mode='wb') as f:
        f.write(data)
    print('ok')
    return f'{config.yml_DATA.music_File}/{name}.aac'
