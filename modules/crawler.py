import wikipedia
import random
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()
i = 0


def fetch_n(n):
    global i
    try:
        rand = wikipedia.random(pages=n)
        try:
            wikipedia.page(rand)
        except wikipedia.DisambiguationError as e:
            s = random.choice(e.options)
            rand = wikipedia.page(s)
        for page in rand:
            conn.execute("insert into wikipedia('name', 'html') values (?, ?)", (page, wikipedia.page(page).html()))
            conn.commit()
            i += 1
        conn.close()
    except:
        pass
    else:
        print("[+] Fetched " + str(i) + " files")
        i += 1
    if i < n:
        print("[i] I countered some issues, but I will handle this")
        fetch_n(n-i)
    else:
        print("[+] Finished fetching")


# If you countered warnings because of html parser with beautiful soup in line 389 in wikipedia edit it to:
# lis = BeautifulSoup(html, "html.parser").find_all('li')
# instead of
# lis = BeautifulSoup(html).find_all('li')
