# -*- coding: utf-8 -*-
import os
import wikipedia
import sqlite3
import hashlib
from modules import *

conn = sqlite3.connect('data.db')
c = conn.cursor()


def main(sentence):
    if sentence == '':
        return 'Empty!'
    global conn
    # Fetching random  99 html pages from wikipedia, But you don't have to go through this again, I already did
    # crawler.fetch_n(9)

    # Check if result is cached
    conn = sqlite3.connect('cache.db')
    test = conn.execute("select result from results where hash=? and query=?", (get_hash("data.db"), sentence))
    result = test.fetchone()
    if result is not None:
        results = ''.join(result)
        return results
    else:
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
    all_words = sorted(set(sentence.lower().split()))
    all_synonyms = semantic.all_synonyms_list(all_words)

    results = {}
    # loop into records
    for row in conn.execute("select name, html from wikipedia"):
        # Getting content and classifying it into "titles" and "plain"
        plain = [item for item in extractor.text(row[1]).split(" ") if item != ""]
        titles = [item for item in extractor.titles(row[1]).split(" ") if item != ""]
        # Searching content, and return list of pages in best order
        results[row[0]] = semantic.search(all_words, all_synonyms, titles, plain)
    results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1])}
    sorted_results = []
    for x in list(results)[-10:]:
        sorted_results.append(x)
    found = False
    str_results = ""
    sorted_results = reversed(sorted_results)
    for x in sorted_results:
        score = results[x]
        if score == 0:
            continue
        found = True
        current = f"Score {score}, {x}, {wikipedia.page(x).url}"
        str_results += current + "$"
    if not found:
        return 0
    else:
        # caching
        c.close()
        conn = sqlite3.connect('cache.db')
        r_hash = get_hash("data.db")
        conn.execute("insert into results('hash', 'query', 'result') values (?, ?, ?)", (r_hash, sentence, str_results))
        conn.commit()
        return str_results


def get_hash(file):
    f_hash = hashlib.md5()
    with open(file, 'rb') as file_h:
        buffer = file_h.read()
    f_hash.update(buffer)
    return f_hash.hexdigest()


if __name__ == '__main__':
    # Getting input and classifying it
    sentence = input("[?] What are you looking for? (suggestion: William) ")
    results = main(sentence).split('$')
    for result in results:
        print(result)
    print("[i] Coded By Nour.")