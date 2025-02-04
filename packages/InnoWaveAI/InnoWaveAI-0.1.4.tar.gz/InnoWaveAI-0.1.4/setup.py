from setuptools import setup, find_packages

setup(
    name="InnoWaveAI",
    version="0.1.4",
    packages=find_packages(),
    install_requires=[],
    author="InnoWave",
    author_email="bodnar.2009@inbox.ru",
    description="Библиотека для генерации кода с использованием Together AI",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)