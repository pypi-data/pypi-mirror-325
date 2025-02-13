from setuptools import setup, find_packages

setup(
    name="tuik_scraper",
    version="0.1.8",  # Versiyonu yükseltin
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
        "beautifulsoup4",
        "selenium",
        "webdriver-manager"
    ],
    author="Bora Kaya",
    author_email="bora.587@hotmail.com",
    description="TÜİK veri çekme ve indirme kütüphanesi",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kaboya19/tuik_scraper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
