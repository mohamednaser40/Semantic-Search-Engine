import re
from flask import Flask
from flask import request
from app import *

app = Flask(__name__)


@app.route("/")
def hello():
    try:
        search = request.args.get("search")
        html = main(search)
        if html == 0:
            html = "[-] The data set is quite small I couldn't find anything, try fetching some more using the crawler."
        else:
            print(html)
            html = html.replace("$", "\n <br> \n")
            html = re.sub(r'(.*?),\s(.*?),\s(https?.*\n)', r"<a href='\3' target='_blank'> \1, \2 </a>", html)
    except:
        html = '''
        <html>
            <head>
                <title> Semantic Search Engine </title>
                <style>
                    .form {margin: 100px auto;width: 70%;padding: 50px;text-align: center;}
                    input {padding: 10px;border-radius: 5px;border: 1px solid #ccc;width: 80%;display: block;margin: 20px auto;}
                    button {width: 200px; padding: 10px;margin: 20px auto;display: block;}
                </style>
            </head>
            <body>
                <div class="form">
                    <input required id="search" type="text" placeholder="e.g United States" name="search">
                    <button onclick="search()">Search</button>
                    <div type="submit" id="output"></div>
                </div>
            </body>
            <script>
                function search(){
                    var xhttp = new XMLHttpRequest();
                    var out = document.getElementById("output");
                    xhttp.open("GET", "/", true);
                    para = document.getElementById("search").value;
                    xhttp.onreadystatechange = function() {
                        if (this.readyState == 4 && this.status == 200) {
                            out.innerHTML = this.responseText;
                        }
                    };
                    xhttp.open("GET", "/?search="+para, true);
                    xhttp.send();
                    out.innerHTML = "Loading ...";
                }
            </script>
        </html>'''
    return html


if __name__ == "__main__":
    app.run()
