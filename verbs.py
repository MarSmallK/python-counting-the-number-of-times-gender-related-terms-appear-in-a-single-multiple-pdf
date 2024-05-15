import PyPDF2
import nltk
from collections import Counter
import os
import re

# 添加NLTK数据路径
nltk.data.path.append('/Users/xukai/nltk_data')


# 读取PDF文档的文本内容
def extract_text_from_pdf(pdf_path):
    """
    从PDF文档中提取文本内容。

    参数:
        pdf_path (str): PDF文档的路径。

    返回:
        str: 提取的文本内容。
    """
    pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text


# 统计单词出现次数
def count_words_in_text(text, words_to_count):
    """
    统计文本中指定单词的出现次数。

    参数:
        text (str): 文本内容。
        words_to_count (list): 要统计的单词列表。

    返回:
        dict: 每个单词的出现次数。
    """
    words = nltk.word_tokenize(text.lower())
    word_counts = Counter(words)
    counts = {word: 0 for word in words_to_count}

    for word in words_to_count:
        pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
        counts[word] = len(pattern.findall(text))

    return counts


# 统计单个PDF文档中的单词次数
def count_words_in_pdf(pdf_path, words_to_count):
    """
    统计单个PDF文档中的指定单词次数。

    参数:
        pdf_path (str): PDF文档的路径。
        words_to_count (list): 要统计的单词列表。

    返回:
        dict: 每个单词的出现次数。
    """
    text = extract_text_from_pdf(pdf_path)
    return count_words_in_text(text, words_to_count)


# 统计多个PDF文档中的单词次数
def count_words_in_multiple_pdfs(pdf_dir, words_to_count):
    """
    统计多个PDF文档中的指定单词次数。

    参数:
        pdf_dir (str): 包含PDF文档的目录路径。
        words_to_count (list): 要统计的单词列表。

    返回:
        Counter: 每个单词在所有文档中的总出现次数。
    """
    total_counts = Counter()
    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_dir, pdf_file)
            counts = count_words_in_pdf(pdf_path, words_to_count)
            total_counts.update(counts)
    return total_counts


# 示例性别相关单词列表（英文）
gender_related_words = [
    "male", "female", "mr", "ms", "boy", "girl", "father", "mother", "brother", "sister",
    "husband", "wife", "man", "woman", "he", "she", "son", "daughter", "uncle", "aunt"
]

# 统计单个PDF文档
single_pdf_path = "/Users/xukai/Downloads/01_Gender_Concepts.pdf"
single_pdf_word_counts = count_words_in_pdf(single_pdf_path, gender_related_words)
print("单个PDF文档中的单词次数：")
print(single_pdf_word_counts)

# 统计多个PDF文档
pdf_paths = [
    "/Users/xukai/Downloads/01_Gender_Concepts.pdf",
    # "/Users/xukai/Downloads/Gender glossary of terms and concepts.pdf",
    "/Users/xukai/Downloads/DefinGenderRelatedTerms.pdf",
    "/Users/xukai/Downloads/contry_presentation_japan_09.pdf"
]

total_counts = Counter()
for pdf_path in pdf_paths:
    counts = count_words_in_pdf(pdf_path, gender_related_words)
    total_counts.update(counts)

print("多个PDF文档中的单词次数：")
print(total_counts)
