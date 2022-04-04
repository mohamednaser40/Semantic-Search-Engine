import nltk
from nltk.corpus import wordnet


def synonyms_list(query):
    synonyms = []
    for syn in wordnet.synsets(query):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return synonyms


def all_synonyms_list(all_words):
    all_synonyms = []
    for word in all_words:
        for synonym in synonyms_list(word):
            all_synonyms.append(synonym)
    return all_synonyms


def counter(q_list, w_list):
    count = 0
    for word in q_list:
        count += w_list.count(word)
    return count


def search(all_words, all_synonyms, titles, plain):
    word_occ = counter(all_words, plain) + counter(all_words, titles)
    syn_occ = counter(all_synonyms, plain) + counter(all_synonyms, titles)
    total_occ = word_occ + syn_occ
    return total_occ
