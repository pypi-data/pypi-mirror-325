from setuptools import setup, find_packages
import sys

# Display a warning if the user is on macOS or Linux and hasn't installed MeCab manually
if sys.platform in ["darwin", "linux"]:
    print(
        "⚠️ MeCab must be installed manually on macOS/Linux. "
        "Run the appropriate command from the installation instructions in README.md before proceeding."
    )

setup(
    name="kanasplit",
    version="1.0.2",  # Asegúrate de mantener la versión actualizada
    author="José Trujillo",
    author_email="joseantonio_tf@outlook.com",
    description="A Japanese text tokenizer with POS tagging and Jisho.org integration.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/byteMe394/KanaSplit",
    packages=find_packages(),  # Detecta la carpeta kanasplit/
    install_requires=[
        "ratelimit>=2.2,<3.0",
        "requests>=2.31.0",
        "mecab-python3"  # Python wrapper for MeCab
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: Japanese",
        "Topic :: Text Processing :: Linguistic",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "kanasplit-cli=kanasplit.tokenizer:cli",  # Ajustado para la nueva estructura
        ]
    },
    include_package_data=True,
    zip_safe=False,
    project_urls={
        "Documentation": "https://github.com/byteMe394/KanaSplit#readme",
        "Source": "https://github.com/byteMe394/KanaSplit",
        "Issue Tracker": "https://github.com/byteMe394/KanaSplit/issues",
    },
    keywords="Japanese NLP tokenizer MeCab Jisho",
)
