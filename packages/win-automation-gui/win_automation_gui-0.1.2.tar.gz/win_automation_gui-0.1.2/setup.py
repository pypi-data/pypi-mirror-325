from setuptools import setup, find_packages

setup(
    name="win-automation-gui",
    version="0.1.2",
    description="Uma biblioteca para automação de controles GUI com Win32.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Leonardo Almeida",
    author_email="leonardoti.dev@gmail.com",
    packages=find_packages(),
    install_requires=[
        "pywin32",  # Dependência necessária
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)