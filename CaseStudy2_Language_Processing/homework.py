import pandas as pd
from collections import Counter

def count_words_fast(text):
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

hamlets = pd.DataFrame(columns=("language", "text"))
book_dir = "Books"
title_num = 1
for language in book_titles:
    for author in book_titles[language]:
        for title in book_titles[language][author]:
            if title == "Hamlet":
                inputfile = data_filepath+"Books/"+language+"/"+author+"/"+title+".txt"
                text = read_book(inputfile)
                hamlets.loc[title_num] = language, text
                title_num += 1

counted_text = count_words_fast(text)

data = pd.DataFrame({
    "word": list(counted_text.keys()),
    "count": list(counted_text.values())
})

data["length"] = data["word"].apply(len)

def func(count):
    if count == 1:
        return "unique"
    elif count <= 10:
        return "infrequent"
    elif count > 10:
        return "frequent"

data["frequency"] = data["count"].apply(func)

meanLen = data.groupby("frequency").mean()
sizeLen = data.groupby("frequency").size()

sub_data = pd.DataFrame({
    "language": language,
    "frequency": ["frequent", "infrequent", "unique"],
    "mean_word_length": meanLen["length"],
    "num_words": sizeLen
})

def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })

    data.loc[data["count"] > 10,  "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1,  "frequency"] = "unique"

    data["length"] = data["word"].apply(len)

    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent", "infrequent", "unique"],
        "mean_word_length": data.groupby(by="frequency")["length"].mean(),
        "num_words": data.groupby(by="frequency").size()
    })

    return(sub_data)


grouped_data = pd.DataFrame(
    columns=["language", "frequency", "mean_word_length", "num_words"])

for i in range(len(hamlets)):
    language, text = hamlets.iloc[i]
    sub_data = summarize_text(language, text)
    grouped_data = grouped_data.append(sub_data)

colors = {"Portuguese": "green", "English": "blue", "German": "red"}
markers = {"frequent": "o", "infrequent": "s", "unique": "^"}
import matplotlib.pyplot as plt
for i in range(grouped_data.shape[0]):
    row = grouped_data.iloc[i]
    plt.plot(row.mean_word_length, row.num_words,
             marker=markers[row.frequency],
             color=colors[row.language],
             markersize=10
             )

color_legend = []
marker_legend = []
for color in colors:
    color_legend.append(
        plt.plot([], [],
                 color=colors[color],
                 marker="o",
                 label=color, markersize=10, linestyle="None")
    )
for marker in markers:
    marker_legend.append(
        plt.plot([], [],
                 color="k",
                 marker=markers[marker],
                 label=marker, markersize=10, linestyle="None")
    )
plt.legend(numpoints=1, loc="upper left")

plt.xlabel("Mean Word Length")
plt.ylabel("Number of Words")
# show your plot using `plt.show`!
plt.show()
