"""
    ########################################################################################################################################################
    # This algorithm is part of a code library for optimizing the Artificial Intelligence models of Sapiens Technology®, and its disclosure, distribution, #
    # or reverse engineering without the company's prior consent will be subject to legal proceedings and actions pursued by our legal department.         #
    ########################################################################################################################################################
"""
# setup.py
from setuptools import setup, find_packages
import os
from subprocess import check_call
from setuptools.command.install import install

class PostInstallCommand(install):
    """Classe customizada para executar passos pós-instalação"""
    def run(self):
        # Primeiro executa a instalação normal
        install.run(self)
        
        # Depois executa o script de pós-instalação
        try:
            check_call(['python', 'post_install.py'])
        except Exception as e:
            print(f"Erro durante a execução do post_install: {e}")

package_name = 'sapiens_machine'
version = '1.0.5'

setup(
    name=package_name,
    version=version,
    author='OPENSAPI',
    packages=find_packages(),
    install_requires=['scipy==1.15.1', 'requests==2.31.0'],
    url='https://github.com/',
    license='Proprietary Software',
    cmdclass={
        'install': PostInstallCommand,
    },
    # Inclui o script de pós-instalação no pacote
    data_files=[('', ['post_install.py'])],
)
"""
    ########################################################################################################################################################
    # This algorithm is part of a code library for optimizing the Artificial Intelligence models of Sapiens Technology®, and its disclosure, distribution, #
    # or reverse engineering without the company's prior consent will be subject to legal proceedings and actions pursued by our legal department.         #
    ########################################################################################################################################################
"""
