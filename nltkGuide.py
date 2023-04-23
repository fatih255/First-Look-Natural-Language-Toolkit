from nltk import FreqDist
from nltk.book import *
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import download, pos_tag, help, RegexpParser, ne_chunk,Text

import pprint


import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

pp = pprint.PrettyPrinter(indent=2)


"""
- Tokenizing
By tokenizing, you can conveniently split up text by word or by sentence. 
"""

example_string = "The friends of DeSoto love scarves."

# tokenizing sentences
tokenizedSentences = sent_tokenize(example_string)
# print('tokenized sentences')
# pp.pprint(tokenizedSentences)

# tokenizing words
words = word_tokenize(example_string)
# print('tokenized words')
# pp.pprint(words)


"""
- Filtering Stop Words:
Stop words are words that you want to ignore, so you filter them out of your text when you’re processing it. Very common words like 'in', 'is', and 'an' are often used as stop words since they don’t add a lot of meaning to a text in and of themselves.
"""
download("stopwords")
stop_words = set(stopwords.words("english"))

# disable case sensitive with casefold() method
filtered_list = [word for word in words if word.casefold() not in stop_words]


"""
Stemming:
Stemming is a text processing task in which you reduce words to their root, which is the core part of a word. For example, the words “helping” and “helper” share the root “help.” Stemming allows you to zero in on the basic meaning of a word rather than all the details of how it’s being used. NLTK has more than one stemmer, but you’ll be using the Porter stemmer.
"""
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
# print('stemmed_words')
# pp.pprint(stemmed_words)


"""
Lemmatizing:
Now that you’re up to speed on parts of speech, you can circle back to lemmatizing. Like stemming, lemmatizing reduces words to their core meaning, but it will give you a complete English word that makes sense on its own instead of just a fragment of a word like 'discoveri'.
"""
download('wordnet')
lemmatizer = WordNetLemmatizer()
lemantize_words = [lemmatizer.lemmatize(word) for word in words]
# print('lemmatize words')
# lemmatizer.lemmatize("worst");
# pp.pprint(words)
# pp.pprint(lemantize_words)

"""
You got the result 'worst' because lemmatizer.lemmatize() assumed that "worst" was a noun. 
You can make it clear that you want "worst" to be an adjective:

The default parameter for pos is 'n' for noun, 
"""
# pp.pprint(lemmatizer.lemmatize("worst", pos="a"))

'''
According to the rule you created, your chunks:
Start with an optional (?) determiner ('DT')
Can have any number (*) of adjectives (JJ)
End with a noun (<NN>)
'''
#  pp.pprint(help.upenn_tagset()) # info for tags


"""
- What is the difference between Stemming and Lemmatization?

Lemmatization and stemming are two different word root extraction methods frequently used in natural language processing (NLP).

Stemming is obtained by cutting word roots according to a certain set of rules. As a result of this process, different conjugations of the same word are reduced to the same root. For example, the words "play", "played", "playing" are reduced to the word "play".

Lemmatization, on the other hand, uses grammatical rules to find the semantically correct root of the word. As a result of this process, the root word is obtained by preserving its true meaning. For example, verbs such as "is", "am", "are" are reduced to the word "be".

The difference between the two is that in stemming, the root of the word cannot always be assigned a meaning, while in the lemmatization process, the semantically correct root of the word is reached.

"""


"""
Tagging Parts of Speech:
Part of speech is a grammatical term that deals with the roles words play when you use them together in sentences. Tagging parts of speech, or POS tagging, is the task of labeling the words in your text according to their part of speech.
"""

download('averaged_perceptron_tagger')
download('tagsets')
tagged_words = pos_tag(words)

# print('tagged_words')
# pp.pprint(tagged_words)


"""
- Chinking
Chinking is used together with chunking, but while chunking is used to include a pattern, chinking is used to exclude a pattern.

- regexp tips:
}<JJ>{ exclude tag pattern 
{<.*>+} include all tags pattern

"""

lotr_quote = "It's a dangerous business, Frodo, going out your door."

grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = RegexpParser(grammar)

words_in_lotr_quote = word_tokenize(lotr_quote)
lotr_pos_tags = pos_tag(words_in_lotr_quote)
tree = chunk_parser.parse(lotr_pos_tags)

# print('Chinking')
# pp.pprint(words_in_lotr_quote)
# tree.pretty_print()


grammartwo = """Chunk: {<.*>+}
}<JJ>{"""
chunk_parsertwo = RegexpParser(grammartwo)
treetwo = chunk_parsertwo.parse(lotr_pos_tags)

# treetwo.pretty_print()

"""
Here, you’ve excluded the adjective 'dangerous' from your chunks and are left with two chunks containing everything else. The first chunk has all the text that appeared before the adjective that was excluded. The second chunk contains everything after the adjective that was excluded.
"""


"""
Using Named Entity Recognition (NER)
Named entities are noun phrases that refer to specific locations, people, organizations, and so on. With named entity recognition, you can find the named entities in your texts and also determine what kind of named entity they are.
"""
download("maxent_ne_chunker")
download("words")
tree = ne_chunk(lotr_pos_tags)
# tree.pretty_print()

"""
See how Frodo has been tagged as a PERSON? You also have the option to use the parameter binary=True if you just want to know what the named entities are but not what kind of named entity they are:
"""
tree = ne_chunk(lotr_pos_tags, binary=True)
# tree.pretty_print()

"""
That’s how you can identify named entities! But you can take this one step further and extract named entities directly from your text. 
"""

quote = """
    Men like Schiaparelli watched the red planet—it is odd, by-the-bye, that
    for countless centuries Mars has been the star of war—but failed to
    interpret the fluctuating appearances of the markings they mapped so well.
    All that time the Martians must have been getting ready.

    During the opposition of 1894 a great light was seen on the illuminated
    part of the disk, first at the Lick Observatory, then by Perrotin of Nice,
    and then by other observers. English readers heard of it first in the
    issue of Nature dated August 2."""


def extract_ne(quote):
    words = word_tokenize(quote, language='english')
    tags = pos_tag(words)
    tree = ne_chunk(tags, binary=True)
    return set(
        " ".join(i[0] for i in t)
        for t in tree
        if hasattr(t, "label") and t.label() == "NE"
    )


"""
With this function, you gather all named entities, with no repeats. In order to do that, you tokenize by word, apply part of speech tags to those words, and then extract named entities based on those tags. Because you included binary=True, the named entities you’ll get won’t be labeled more specifically. You’ll just know that they’re named entities.
"""
# Take a look at the information you extracted: (they’re named entities)
"""
like this:

An institution: 'Lick Observatory'
A planet: 'Mars'
A publication: 'Nature'
People: 'Perrotin', 'Schiaparelli'
"""
extracted = extract_ne(quote)
pp.pprint(extracted)

"""
Getting Text to Analyze:
Now that you’ve done some text processing tasks with small example texts, you’re ready to analyze a bunch of texts at once. A group of texts is called a corpus. NLTK provides several corpora covering everything from novels hosted by Project Gutenberg to inaugural speeches by presidents of the United States.

This corpus is a collection of personals ads, which were an early version of online dating. If you wanted to meet someone, then you could place an ad in a newspaper and wait for other readers to respond to you.

In order to analyze texts in NLTK, you first need to import them. This requires nltk.download("book"), which is a pretty big download:

"""
download("book")


"""
Using a Concordance:

When you use a concordance, you can see each time a word is used, along with its immediate context. This can give you a peek into how a word is being used at the sentence level and what words are used with it.

Let’s see what these good people looking for love have to say! The personals corpus is called text8, so we’re going to call .concordance() on it with the parameter "man":

"""

# text8.concordance("man")

"""
Interestingly, the last three of those fourteen matches have to do with seeking an honest man, specifically:

1. SEEKING HONEST MAN
2. Seeks 35 - 45 , honest man with good SOH & similar interests
3. genuine , caring , honest and normal man for fship , poss rship

Let’s see if there’s a similar pattern with the word "woman":
"""
# text8.concordance("woman")

# The issue of honesty came up in the first match only:
# Dipping into a corpus with a concordance won’t give you the full picture, but it can still be interesting to take a peek and see if anything stands out.

"""
Making a Dispersion Plot:
You can use a dispersion plot to see how much a particular word appears and where it appears. So far, we’ve looked for "man" and "woman", but it would be interesting to see how much those words are used compared to their synonyms:
"""
# text8.dispersion_plot(["woman", "lady", "girl", "gal", "man", "gentleman", "boy", "guy"])

"""
Each vertical blue line represents one instance of a word. Each horizontal row of blue lines represents the corpus as a whole. This plot shows that:

- "lady" was used a lot more than "woman" or "girl". There were no instances of "gal".
- "man" and "guy" were used a similar number of times and were more common than "gentleman" or "boy".

"""


# text2.dispersion_plot(["Allenham", "Whitwell", "Cleveland", "Combe"])

"""
Allenham is the home of Willoughby’s benefactress and comes up a lot when Marianne is first interested in him.
Cleveland is a home that Marianne stays at after she goes to see Willoughby in London and things go wrong.
"""


"""
Making a Frequency Distribution:

With a frequency distribution, you can check which words show up most frequently in your text. You’ll need to get started with an import:

"""
frequency_distribution = FreqDist(text8)
# print(frequency_distribution)

# output : <FreqDist with 1108 samples and 4867 outcomes>
# Since 1108 samples and 4867 outcomes is a lot of information, start by narrowing that down.

# most_common_20 = frequency_distribution.most_common(20)
# pp.pprint(most_common_20)

# You have a lot of stop words in your frequency distribution, but you can remove them just as you did earlier.
# Create a list of all of the words in text8 that aren’t stop words:
meaningful_words = [word for word in text8 if word.casefold() not in stop_words]

# Now that you have a list of all of the words in your corpus that aren’t stop words, make a frequency distribution:

frequency_distribution = FreqDist(meaningful_words)
most_common_20 = frequency_distribution.most_common(20)
# pp.pprint(most_common_20)

# You can turn this list into a graph:

#frequency_distribution.plot(20, cumulative=True)


"""
Finding Collocations:

A collocation is a sequence of words that shows up often. If you’re interested in common collocations in English, then you can check out The BBI Dictionary of English Word Combinations.
- Here are some examples of collocations that use the word “tree”:
    - Syntax tree
    - Family tree
    - Decision tree
"""
# text8.collocations()
lemmatized_words = [lemmatizer.lemmatize(word) for word in text8]
new_text = Text(lemmatized_words)
new_text.collocations()

"""
Compared to your previous list of collocations, this new one is missing a few:

- weekends away
- poss rship

The idea of quiet nights still shows up in the lemmatized version, quiet night. Your latest search for collocations also brought up a few news ones:

- year old suggests that users often mention ages.
- photo pls suggests that users often request one or more photos.

That’s how you can find common word combinations to see what people are talking about and how they’re talking about it!

"""