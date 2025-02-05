# KanaSplit - Japanese Text Tokenizer

KanaSplit is a powerful and efficient Japanese text tokenizer with part-of-speech (POS) tagging and Jisho.org integration.

![KanaSplit Logo](assets/dancing_shigure.gif)

## 🚀 Features
- **Tokenization:** Splits Japanese sentences into words and morphemes.
- **POS Tagging:** Provides grammatical category for each token.
- **Furigana Support:** Extracts readings for kanji words.
- **Jisho.org API Integration:** Retrieves word meanings and definitions.
- **Command-Line Interface (CLI):** Allows easy text tokenization from the terminal.
- **Graphical User Interface (GUI):** Provides a user-friendly Tkinter-based interface.

---

## 📦 Installation

### Install from PyPI (Recommended)
The easiest way to install KanaSplit is via `pip`:

```sh
pip install kanasplit
```

### Install from Source
Alternatively, you can clone the repository and install it manually:

```sh
git clone https://github.com/byteMe394/KanaSplit.git
cd KanaSplit
pip install -r requirements.txt
```

---

## 🖥 OS-Specific Installation Instructions

### **Windows**
Simply run:
```sh
pip install kanasplit
```

### **macOS**
macOS users need to install `MeCab` manually before using KanaSplit:
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install mecab mecab-ipadic
pip install mecab-python3
pip install kanasplit
```

### **GNU/Linux (Debian/Ubuntu-based)**
For Debian-based Linux distributions, install `MeCab` before installing KanaSplit:
```sh
sudo apt update
sudo apt install mecab mecab-ipadic-utf8
pip install mecab-python3
pip install kanasplit
```

For other distributions, use the package manager of your choice.

---

## 🎮 Usage

### **Command Line Interface (CLI)**
You can tokenize Japanese text directly from the terminal:

```sh
kanasplit-cli "こんにちは世界"
```

Example Output:
```
Tokenized Text:
- こんにちは (Interjection)
- 世界 (Noun)

Fetching meanings from Jisho.org...
Word: こんにちは - Reading: こんにちは - Meanings: hello, good day
Word: 世界 - Reading: せかい - Meanings: world, society, universe
```

### **Graphical User Interface (GUI)**
KanaSplit also includes a Tkinter-based GUI for users who prefer a graphical interface.

To launch the GUI, simply run:

```sh
python GUI.py
```

This will open a window where you can enter Japanese text, process it, and view tokenized results.

---

## 🛠 Dependencies
KanaSplit requires the following dependencies, which are installed automatically:

- `ratelimit`
- `MeCab`
- `requests`

**Note:** Tkinter is built into Python and does not require installation.

---

## 🤝 Contributing
If you'd like to contribute, clone the repository and submit a pull request! You can install additional development tools with:

```sh
pip install -r requirements.txt
```

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 📬 Contact
For questions or support, feel free to reach out:

- GitHub: [byteMe394](https://github.com/byteMe394)
- Email: joseantonio_tf@outlook.com

---

🎌 **Happy Tokenizing!** 🎌

