"""
    ########################################################################################################################################################
    # This algorithm is part of a code library for optimizing the Artificial Intelligence models of Sapiens Technology®, and its disclosure, distribution, #
    # or reverse engineering without the company's prior consent will be subject to legal proceedings and actions pursued by our legal department.         #
    ########################################################################################################################################################
"""
from setuptools import setup, find_packages, Command
from site import getsitepackages
from os import path, makedirs
from requests import get
import atexit

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

def post_install():
    """Função que será executada após a instalação"""
    print("Iniciando download pós-instalação...")
    package_name = 'sapiens_machine'
    installation_directory = path.join(getsitepackages()[0], package_name)
    download_libraries(destination_directory=installation_directory)

class DownloadLibrariesCommand(Command):
    description = "Download libraries from a repository."
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        package_name = 'sapiens_machine'
        installation_directory = path.join(getsitepackages()[0], package_name)
        download_libraries(destination_directory=installation_directory)

# Registra a função para ser executada ao final da instalação
atexit.register(post_install)

package_name = 'sapiens_machine'
version = '1.0.4'

setup(
    name=package_name,
    version=version,
    author='OPENSAPI',
    packages=find_packages(),
    install_requires=['scipy==1.15.1', 'requests==2.31.0'],
    url='https://github.com/',
    license='Proprietary Software',
    cmdclass={
        'download_libraries': DownloadLibrariesCommand,
    },
    options={
        'bdist_wheel': {
            'universal': True
        }
    },
    # Adiciona entry points para pós-instalação
    entry_points={
        'distutils.setup_keywords': [
            'download_libraries = setup:post_install',
        ],
    }
)

# Executa o download se este arquivo for executado diretamente
if __name__ == '__main__':
    post_install()
"""
    ########################################################################################################################################################
    # This algorithm is part of a code library for optimizing the Artificial Intelligence models of Sapiens Technology®, and its disclosure, distribution, #
    # or reverse engineering without the company's prior consent will be subject to legal proceedings and actions pursued by our legal department.         #
    ########################################################################################################################################################
"""
