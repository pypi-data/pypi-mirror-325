from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai-gemini-scraper",
    version="0.1.3",
    author="Cyrille Gattiker",
    author_email="cyrille.gattiker@gmail.com",
    description="A simple package for scraping websites and generating responses using Google's Generative AI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cyruszevirus/ai-scraper",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "google-generativeai",
        "urllib3"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
