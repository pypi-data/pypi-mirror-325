# post_install.py
from site import getsitepackages
from os import path, makedirs
from requests import get

def download_libraries(repository_url='https://api.github.com/repos/sapiens-technology/Libs/contents/', destination_directory='./'):
    def download_file(url, local_path):
        response = get(url)
        with open(local_path, "wb") as file:
            file.write(response.content)

    def download_repository(url, destination_directory):
        response = get(url)
        if response.status_code == 200:
            contents = response.json()
            for content in contents:
                if content["type"] == "file":
                    print(f"Downloading file: {content['name']}")
                    download_file(content["download_url"], path.join(destination_directory, content["name"]))
                elif content["type"] == "dir":
                    new_directory = path.join(destination_directory, content["name"])
                    makedirs(new_directory, exist_ok=True)
                    print(f"Entering directory: {content['name']}")
                    download_repository(content["url"], new_directory)
        else:
            print(f"ERROR accessing the repository: {response.status_code}")

    makedirs(destination_directory, exist_ok=True)
    download_repository(repository_url, destination_directory)
    print("Repository download completed!")

def main():
    """Função principal que será executada após a instalação"""
    print("Iniciando download pós-instalação...")
    package_name = 'sapiens_machine'
    installation_directory = path.join(getsitepackages()[0], package_name)
    download_libraries(destination_directory=installation_directory)

if __name__ == '__main__':
    main()
