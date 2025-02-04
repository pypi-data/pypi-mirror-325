from setuptools import setup, find_packages
from pathlib import Path


setup(
    name='pro-video-ferramentas-DOUGLAS-DC',
    version=1.0,
    description='Este pacote irá fornecer ferramentas de processamento de vídeo',
    long_description=Path('README.md').read_text(), 
    author='Douglas',
    author_email='douglascristiano112@gmail.com',
    keywords=['camera','video','processamento'],
    packages=find_packages()
)