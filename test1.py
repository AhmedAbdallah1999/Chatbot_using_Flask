from flask import Flask
from chatterbot import  ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
app = Flask(__name__)
english_bot = ChatBot("chaterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("data/data.yml")

@app.route("/")
def index():
    return 
if __name__ == "__main__" :
    app.run(debug=True)