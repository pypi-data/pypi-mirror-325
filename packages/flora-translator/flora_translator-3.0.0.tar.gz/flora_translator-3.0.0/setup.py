from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_des = str(f.read())

setup(
    name='flora_translator',
    version='3.0.0',
    author='Flora',
    author_email="floraplantprocessing@gmail.com",
    description='A package that help flet developers to make their apps support multiple languages',
    long_description=long_des,
    long_description_content_type='text/markdown',
    url='https://floraplant.ir',
    install_requires=["flet"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ],
)