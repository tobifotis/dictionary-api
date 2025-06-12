from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("./dictionary.csv")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def dest(word):

    definition = df.loc[df["word"] == word]["definition"].squeeze()

    dictionary_output = {"Word": str(word).capitalize(),
            "Definition": str(definition)
            }
    return dictionary_output

if __name__ == "__main__":
    app.run(debug=True, port=5001)
