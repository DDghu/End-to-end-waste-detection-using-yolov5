#installing this as the local package

from setuptools import find_packages, setup

setup(
    name='WasteDetection',
    version='0.0.0',
    author='Deepjoy Das',
    author_email='deepjoydas02@gmail.com',
    packages=find_packages(), # it looks for constructor file in every folder
    install_requires=[]
    
)