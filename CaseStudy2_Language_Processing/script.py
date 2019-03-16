import re
from collections import Counter
import os
import pandas as pd
import matplotlib.pyplot as plt

words = "Here are some words. This sentence also has punctuation punctuation words marks."

def countWords (text):
    text = text.lower()
    newText = re.sub(r'\.|\,|\;|\:|\'|\"', "", text)
    # wordCount = {}
    # for word in newText.split(" "):
    #     if word in wordCount:
    #         wordCount[word] += 1
    #     else:
    #         wordCount[word] = 1
    wordCount = Counter(newText.split(" "))
    return wordCount

def read_book(title_path):
    with open(title_path, 'r', encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace('\n', "").replace('\r', "")
    return text

def word_stats(wordCount):
    num_unique = len(wordCount)
    counts = wordCount.values()
    return (num_unique, counts)

book_dir = r"./Books"

inputFile = ""

stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))
title_num = 1
for lang in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + lang):
        for title in os.listdir(book_dir + "/" + lang + "/" + author):
            inputFile = book_dir + "/" + lang + "/" + author + "/" + title
            #print(inputFile)
            text = read_book(inputFile)
            (num_unique, counts) = word_stats(countWords(text))
            stats.loc[title_num] = lang, author.capitalize(), title.replace(".txt", ""), sum(counts), num_unique
            title_num += 1

print(stats.head())
print(stats.tail())
print(stats.length)

# plt.plot(stats.length, stats.unique, "bo")
# plt.show()

plt.figure(figsize=(10,10))
subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label="English", color="crimson")
subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, "o", label="French", color="forestgreen")
subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, "o", label="German", color="orange")
subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length, subset.unique, "o",
           label="Portuguese", color="blueviolet")
plt.legend()
plt.xlabel("Book Length")
plt.ylabel("Number of unique words")
# plt.savefig("lang_plot.pdf")
plt.show()
