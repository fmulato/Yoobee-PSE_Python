# training read file

arq = "demo_file.txt"
arq2 = "demo_file2.txt"
arq3 = "demo_file3.txt"
arq4 = "top_10_word_demo_file.txt"

with open(arq2, 'w') as file:
    file.write("Hello World\n")
    file.write("This is a test\n")
    file.write("This is the line 3\n")

with open(arq3, "a") as file:
    file.write("This is the line 1 with add\n")
    file.write("This is the line 2 with add\n")
    file.write("This is the line 3 with add\n")

with open(arq, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        if ("Title" in line) or ("Translator" in line):
            print(line[0:-1])

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd
#nltk.download('punkt')

with open(arq, 'r', encoding='utf-8') as file:
    contend = file.read()

words = nltk.word_tokenize(contend)
words = [w.lower() for w in words if w.isalpha() and len(w) >=2 ]

# list of stop words
stop_words = stopwords.words('english')

words2 = [p for p in words if p not in stop_words] # without stopwords
freq = {}
for w in words2:
    freq[w] = freq.get(w, 0) + 1 # use 0 if the word not in the dic

df = pd.DataFrame.from_dict(freq, orient='index', columns=['frequent']) # use keys of dic as index e the column 'frequencia' to values
df = df.sort_values(by='frequent', ascending=False)

print("")
print("Top 10 words more frequent")
print(df.head(10))

with open(arq4, 'w') as file:
    file.write(df.head(10).to_string())
