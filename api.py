import requests
TOKEN = ""


class YaUploader:
    URI: str = "https://cloud-api.yandex.net/v1/disk/resources"
    URL_UPLOAD_LINK: str = f"{URI}/upload"

    def __init__(self, token: str):
        self.token = token

    @property
    def header(self):
        return {
            "Content_Type": "application/json",
            "Authorization": f"OAuth {self.token}"
        }

    def get_upload_link(self, ya_disk_path: str):
        params = {"path": ya_disk_path, "overwrite": "true"}
        resource = requests.get(self.URL_UPLOAD_LINK, params=params, headers=self.header)
        upload_url = resource.json().get("href")
        return upload_url

    def upload_file(self, ya_disk_path: str, file_path: str):
        upload_link = self.get_upload_link(ya_disk_path)
        with open(file_path, "rb") as file_obj:
            response = requests.put(upload_link, data=file_obj)
        return response.status_code


some_pera = YaUploader(TOKEN)
some_pera.upload_file('/recipes.txt', 'recipes.txt')