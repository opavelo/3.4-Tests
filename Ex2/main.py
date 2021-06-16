from pprint import pprint
import requests
import json
import cv2
import time
import datetime

class Yandex:
    def __init__(self, token_yd):
        self.token_yd = token_yd
        self.yd_file_list = []
        self.file_path = ''


    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token_yd)}

    # создание папки и списка файлов внутри
    def yd_folder_create(self, folder_name):
        self.file_path = str(folder_name)   #создаем папку с заданным именем
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {
            'path': self.file_path
        }
        response = requests.put(url, headers=headers, params=params)
        if response.status_code == 201:
            print(f'Папка {self.file_path} создана')
        elif response.status_code == 409:
            print(f'Папка {self.file_path} уже была создана')
            # Если папка уже создана получаем имена файлов из этой папки
        else:
            print('Ошибка', response)
        return response

    # Проверка что записано на яндекс диске
    def checking_avaliability(self):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': 'disk:/'}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.json())
        for i in range(0, len(response.json()['_embedded']['items'])):
            self.yd_file_list.append(response.json()['_embedded']['items'][i]['name'])
        print('Список файлов на Яндекс-диске', self.yd_file_list)
        return self.yd_file_list

if __name__ == "__main__":
    yd = Yandex('YD token')

    yd.yd_folder_create('Name2')
    yd.checking_avaliability()