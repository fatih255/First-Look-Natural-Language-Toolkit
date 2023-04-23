

**Explanation about the files in the repo:**

- With the **getKeywords.py** file, you can get a graph showing the frequency of meaningful words in all articles on a blog page.
- You can find annotated examples in the **nltkGuide.py** file.


## First Look  Natural Language Toolkit

This is a Python script that showcases Natural Language Processing techniques using the Natural Language Toolkit (NLTK).

The following NLP techniques are demonstrated:

- Tokenization
- Filtering Stop Words
- Stemming
- Lemmatization
- Tagging Parts of Speech
- Chinking

## Tokenization

Tokenization is the process of splitting text into words or sentences. This is useful because it allows you to process text in smaller, more meaningful units. In this script, the sent_tokenize and word_tokenize functions from the NLTK tokenize module are used to tokenize a sample sentence.

### Filtering Stop Words

Stop words are commonly used words (e.g. "the", "and", "a") that do not provide any meaning to text. The stopwords module from the NLTK corpus is used to create a set of stop words that can be filtered out of text using a list comprehension.

### Stemming

Stemming is the process of reducing words to their root form. This is useful because it allows you to treat different forms of a word (e.g. "helping" and "helper") as the same word. In this script, the Porter stemmer from the NLTK stem module is used to stem a list of words.

## Lemmatization

Lemmatization is the process of reducing words to their base or dictionary form. This is similar to stemming, but produces a valid word that can be found in a dictionary. In this script, the WordNet lemmatizer from the NLTK stem module is used to lemmatize a list of words.

## Tagging Parts of Speech

Part of speech (POS) is a grammatical term that deals with the roles words play when used together in sentences. POS tagging is the task of labeling the words in text according to their part of speech. In this script, the pos_tag function from the NLTK tag module is used to tag a list of words with their corresponding POS.

## Chinking

Chinking is used in conjunction with chunking, but while chunking is used to include a pattern, chinking is used to exclude a pattern. In this script, the RegexpParser class from the NLTK parse module is used to create a grammar that matches noun phrases and then exclude adjective-noun pairs using chinking.

For more information about the NLTK, refer to the [official documentation](https://www.nltk.org/).



## Info: NLTK process for an AI chatbot

<img width="1224" alt="Screenshot 2023-04-24 at 00 28 40" src="https://user-images.githubusercontent.com/52957100/233867197-ebd4e6c6-e92e-4c0f-b0d2-f079ff70d908.png">

1. **Corpus Collection:** Gathering a large dataset of text to train the chatbot, which could include books, articles, social media posts, and other sources.
2. **Tokenization:** Breaking down the text into individual words or phrases, known as tokens, which can then be processed further.
3. **Stopword Removal:** Removing common words that don't provide much meaning or context, such as "the" or "and."
4. **Stemming/Lemmatization:** Reducing words to their root form, which can help group related words together and improve accuracy.
5. **Part-of-Speech (POS) Tagging:** Labeling each token with its grammatical role, such as noun, verb, or adjective.
6. **Named Entity Recognition (NER):** Identifying and labeling specific entities in the text, such as people, places, and organizations.
7. **Sentiment Analysis:** Analyzing the tone and emotion behind the text, which can help the chatbot understand the user's mood and respond appropriately.
8. **Machine Learning:** Using algorithms to train the chatbot to recognize patterns in the text and generate appropriate responses.
9. **Natural Language Generation:** Generating responses that sound natural and conversational, rather than robotic or scripted.
10. **Chatbot Integration:** Building the chatbot into a messaging platform or other application, so that users can interact with it in real time.
