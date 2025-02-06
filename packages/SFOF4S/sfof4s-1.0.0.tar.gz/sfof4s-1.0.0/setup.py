from setuptools import setup, find_packages

setup(
    name="SFOF4S",
    version="1.0.0",
    author= "Yassin Riyazi",
    author_email="iyasiniyasin98@gmail.com",
    description="This toolkit aids in analyzing drop sliding on tilted plates, allowing researchers to study various variables and their correlations in detail.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",  # Fix for PyPI description issue
    url="https://github.com/yriyazi/SFOF4S",
    packages=find_packages(),
    install_requires=[
        "torch==2.6.0",
        "torchaudio==2.4.1",
        "torchvision==0.21.0",
        "numpy==1.26.4",
        "opencv-python==4.10.0",
        "scipy==1.15.1",
        "tqdm==4.67.1",
        "pandas==2.2.3",
        "natsort==8.4.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
