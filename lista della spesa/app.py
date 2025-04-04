from flask import Flask, render_template, request, redirect, url_for #importiamo la classe flask
app = Flask(__name__) #inizializza app flask
lista=["ciao", "ciao1", "ciao2"]

@app.route('/') #visitiamo (`/`), la funzione home() viene eseguita.
def home():
    return render_template("index.html", lista=lista)


@app.route('/aggiungi', methods=['POST'])  #aggiungi
def aggiungi():
    #ottiene elemento dal form
    elemento = request.form['elemento']
    
    if elemento:
        lista.append(elemento)
    return redirect(url_for('home'))

@app.route('/rimuovi/<int:indice>', methods=['POST']) #rimuovi
def rimuovi(indice):
    if 0 <= indice < len(lista):
        lista.pop(indice)
    return redirect(url_for('home'))

@app.route('/rimuovi_tutto', methods=['POST'])
def rimuovi_tutto():
    lista.clear()
    return redirect(url_for('home'))


#avvio flask
if __name__ == '__main__':
    app.run(debug=True) #aggiornamenti in tempo reale