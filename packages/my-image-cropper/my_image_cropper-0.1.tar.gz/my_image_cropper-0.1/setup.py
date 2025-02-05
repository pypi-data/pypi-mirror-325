
from setuptools import setup, find_packages

setup(
    name='my_image_cropper',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',  # Pillowライブラリを依存関係として指定
    ],
    entry_points={
        'console_scripts': [
            'image_cropper=my_image_cropper.cropper:main',  # main関数を指定
        ],
    },
    package_data={
        'my_image_cropper': ['crop_area.json'],  # JSONファイルをパッケージに含める
    },
    description='A simple image cropping tool',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/my_image_cropper',  # GitHubリポジトリのURL
)
