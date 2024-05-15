# Gender-Related Word Count in PDF Documents

This project provides a Python script to count the occurrences of gender-related words in PDF documents. The script can handle both single and multiple PDF files.

## Prerequisites

- Python 3.10.0
- Recommended IDE: PyCharm

## Installation

1. **Install Python 3.10.0**
   - Download and install Python 3.10.0 from the official [Python website](https://www.python.org/downloads/release/python-3100/).

2. **Install Required Packages**
   - Open a terminal and run the following commands to install the necessary Python packages:
     ```bash
     pip install PyPDF2 nltk
     ```

3. **Download and Install NLTK Data**
   - Manually download the `punkt` tokenizer data from the following link: [punkt.zip](https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/tokenizers/punkt.zip)
   - Extract the downloaded `punkt.zip` file to the directory `~/nltk_data/tokenizers/`.

## Project Setup

1. **Clone the Repository**
   - Clone this repository to your local machine or download the script.

2. **Configure PyCharm**
   - Open PyCharm and create a new project.
   - Add the cloned repository or the script file to your PyCharm project.

3. **Add NLTK Data Path**
   - Ensure the script includes the path to the NLTK data:
     ```python
     import nltk
     nltk.data.path.append('/Users/xukai/nltk_data')
     ```

## Usage

1. **Define PDF Paths**
   - Modify the script to include the paths to your PDF files:
     ```python
     single_pdf_path = "/Users/xukai/Downloads/01_Gender_Concepts.pdf"
     pdf_paths = [
         "/Users/xukai/Downloads/01_Gender_Concepts.pdf",
         "/Users/xukai/Downloads/DefinGenderRelatedTerms.pdf",
         "/Users/xukai/Downloads/contry_presentation_japan_09.pdf"
     ]
     ```

2. **Run the Script**
   - Run the script in PyCharm. The script will output the word count for each specified gender-related word in the provided PDF files.

## Script Explanation

The script performs the following functions:

1. **Extract Text from PDF**: Uses `PyPDF2` to read and extract text from PDF files.
2. **Count Word Occurrences**: Uses `nltk` to tokenize the text and count the occurrences of specified gender-related words.
3. **Single PDF Analysis**: Counts words in a single PDF file.
4. **Multiple PDF Analysis**: Counts words across multiple PDF files.

Here is the full script:

```python
import PyPDF2
import nltk
from collections import Counter
import os
import re

# Add NLTK data path
nltk.data.path.append('/Users/xukai/nltk_data')

# Download NLTK punkt tokenizer
nltk.download('punkt')

# Extract text from PDF document
def extract_text_from_pdf(pdf_path):
    pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

# Count occurrences of words in text
def count_words_in_text(text, words_to_count):
    words = nltk.word_tokenize(text.lower())
    word_counts = Counter(words)
    counts = {word: 0 for word in words_to_count}

    for word in words_to_count:
        pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
        counts[word] = len(pattern.findall(text))
    
    return counts

# Count occurrences of words in a single PDF
def count_words_in_pdf(pdf_path, words_to_count):
    text = extract_text_from_pdf(pdf_path)
    return count_words_in_text(text, words_to_count)

# Count occurrences of words in multiple PDFs
def count_words_in_multiple_pdfs(pdf_paths, words_to_count):
    total_counts = Counter()
    for pdf_path in pdf_paths:
        counts = count_words_in_pdf(pdf_path, words_to_count)
        total_counts.update(counts)
    return total_counts

# List of gender-related words
gender_related_words = [
    "male", "female", "mr", "ms", "boy", "girl", "father", "mother", "brother", "sister", 
    "husband", "wife", "man", "woman", "he", "she", "son", "daughter", "uncle", "aunt"
]

# Single PDF analysis
single_pdf_path = "/Users/xukai/Downloads/01_Gender_Concepts.pdf"
single_pdf_word_counts = count_words_in_pdf(single_pdf_path, gender_related_words)
print("Single PDF word counts:")
print(single_pdf_word_counts)

# Multiple PDFs analysis
pdf_paths = [
    "/Users/xukai/Downloads/01_Gender_Concepts.pdf",
    "/Users/xukai/Downloads/DefinGenderRelatedTerms.pdf",
    "/Users/xukai/Downloads/contry_presentation_japan_09.pdf"
]

total_counts = count_words_in_multiple_pdfs(pdf_paths, gender_related_words)
print("Multiple PDFs word counts:")
print(total_counts)
