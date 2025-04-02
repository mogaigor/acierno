from flask import Flask #importiamo la classe flask
app = Flask(__name__) #inizializza app flask
#avvio flask
if __name__ == '__main__':
    app.run(debug=True) #aggiornamenti in tempo reale
@app.route('/') #visitiamo (`/`), la funzione home() viene eseguita.
def home():
return "per ora funziona tutto"