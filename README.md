<h1 align="center">
    NLP script test
</h1>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#project-structure">Project Structure</a> •
  <a href="#requirements">Requirements</a> •
  <a href="#installation">Installation</a> •
  <a href="#license">License</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  <img src="https://img.shields.io/badge/Authors-SmartMatt-blue" />
</p>

## Overview
The `First-NLP-Script` repository contains scripts for analyzing and processing text data. It consists of two main Python scripts (`manage_classes.py` and `key_terms.py`), which use Natural Language Processing (NLP) to analyze articles. The project utilizes libraries such as NLTK, pandas, scikit-learn, and lxml for text data processing and analysis.

## Project Structure
- `manage_classes.py`: Contains class definitions and methods for processing text data, including tokenization, lemmatization, filtering stopwords, and calculating most common words.
- `key_terms.py`: The main script that runs the analysis of text data loaded from an XML file. Uses TfidfVectorizer to analyze the importance of words in documents.
- `news.xml`: An XML file containing text data for analysis.

## Requirements
The project requires Python version 3.8 or newer, along with the following libraries:
- pandas
- nltk
- scikit-learn
- lxml

## Installation
1. Create python virtual environment.
2. To install the required dependencies, run the following command in the terminal:
```bash
pip install -r requirements.txt
```
3. To run the script, execute the command:
```bash
python key_terms.py
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
&copy; 2023 Mateusz Płonka (SmartMatt). All rights reserved.
<a href="https://smartmatt.pl/">
    <img src="https://smartmatt.pl/github/smartmatt-logo.png" title="SmartMatt Logo" align="right" width="60" />
</a>

<p align="left">
  <a href="https://smartmatt.pl/">Portfolio</a> •
  <a href="https://github.com/SmartMaatt">GitHub</a> •
  <a href="https://www.linkedin.com/in/mateusz-p%C5%82onka-328a48214/">LinkedIn</a> •
  <a href="https://www.youtube.com/user/SmartHDesigner">YouTube</a> •
  <a href="https://www.tiktok.com/@smartmaatt">TikTok</a>
</p>
