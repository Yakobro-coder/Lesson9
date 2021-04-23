import requests
from pprint import pprint


class YaUploader:
    def __init__(self):
        # Читает токен из файла
        with open('token.txt', encoding='utf=8') as file:
            self.token = file.read()

        print('Укажите путь от корня диска, до файла.\n'
              'Пример: C:\my_folder\\file.txt')

        self.file_path = str(input('Введите путь: '))
        # Разбивает ссылку по "\" и по индексу [-1] получаем имя файла и его расширение.
        self.name_files = self.file_path.split('\\')[-1]

    def upload(self):
        # Получения ссылки для загрузки файла, с таким же именем как у загружаемого файла.
        url_uploade = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = { 'Content-Type' : 'application/json', 'Authorization' : f'OAuth {self.token}'}
        params = {'path': self.name_files, 'overwrite': 'true'}
        response = requests.get(url_uploade, headers=headers, params=params).json()
        # pprint(response)
        # Загружаем файл по полученной ссылке
        href = response.get('href', '')
        response = requests.put(href, data=open(self.file_path, 'rb'))
        # response.raise_for_status()
        if response.status_code == 201:
            print('Загрузка файла завершена.')
        else:
            print('Что то пошло не так... |*_*|')


if __name__ == '__main__':
    uploader = YaUploader()
    result = uploader.upload()
