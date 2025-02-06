# setup.py
from setuptools import setup, find_packages

setup(
    name='webp-converter-kmj',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    entry_points={
        'console_scripts': [
            'webp-converter-gui=webp_converter:launch_gui',
        ]
    },
    author='dev_kimminjun',
    description='WebP 이미지 변환기',
    long_description=open('README.md', 'rt', encoding='UTF-8').read(),
    long_description_content_type='text/markdown',
    url='',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)