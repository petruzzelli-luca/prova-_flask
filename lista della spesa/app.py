from flask import Flask, render_template #importiamo la classe flask
app = Flask(__name__) #inizializza app flask

x=100
lista=["ciao", "ciao1", "ciao2"]
@app.route('/') #visitiamo (`/`), la funzione home() viene eseguita.
def home():
    return render_template("index.html", lista=lista)




#avvio flask
if __name__ == '__main__':
    app.run(debug=True) #aggiornamenti in tempo reale