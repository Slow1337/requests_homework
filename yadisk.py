import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_href(self, file_adress):
        url = f'https://cloud-api.yandex.net/v1/disk/resources/upload?path={file_adress}'
        headers = {'Authorization': f'OAuth {self.token}'}
        response = requests.get(url=url, headers=headers)
        response = response.json()
        href = response['href']
        return href

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = self.get_href(file_path)
        headers = {'Authorization': f'OAuth {self.token}'}
        with open(file_path, 'rb') as f:
            got = requests.post(url=url, headers=headers, files={'file': f})
        return got
        # Тут ваша логика
        # Функция может ничего не возвращать
