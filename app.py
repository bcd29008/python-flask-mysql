# http://flask.pocoo.org/docs/1.0/tutorial/
# g  is a special object that is unique for each request.
# It is used to store data that might be accessed by multiple functions during the request.

from flask import (
    flash, g, redirect, render_template, request, session, url_for, Flask
)

# https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html
from mysql.connector import MySQLConnection, Error

db_config = {
  'user': 'root',
  'password': 'senha',
  'host': '127.0.0.1',
  'database': 'agenda',
  'raise_on_warnings': True,
}

SECRET_KEY = 'aula de BCD - string aleatória'

app = Flask(__name__)

app.secret_key = SECRET_KEY

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/inserir', methods=('GET', 'POST'))
def inserir():

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        g.db = MySQLConnection(**db_config)
        cursor = g.db.cursor()
        query = "INSERT INTO Contato (nome, email) VALUES (%s, %s)"
        dados = (nome, email)
        cursor.execute(query, dados)
        g.db.commit()
        cursor.close()
        g.db.close()
        return redirect(url_for('listar'))

        # exemplo estático
        # contatos = [{'id': 2, 'nome': nome, 'email' : email}]
        # return render_template('listar.html', title='Listar', contatos=contatos)

    return render_template('inserir.html', title='Adicionar contato')

@app.route('/listar')
def listar():
    # exemplo de uma lista estática - sem consultar DB
    # contatos = [
    #     {
    #         'id' : '1',
    #         'nome' : 'Juca',
    #         'email' : 'j@ifsc'
    #     }
    # ]

    contatos = []

    g.db = MySQLConnection(**db_config)
    cursor = g.db.cursor()

    query = "SELECT * FROM Contato"

    cursor.execute(query)
    for (cId, nome, email) in cursor:
        contatos.append({'id':  cId,'nome':nome, 'email': email})

    cursor.close()
    g.db.close()


    return render_template('listar.html', title='Listar', contatos=contatos)


@app.route('/editar', methods=('GET', 'POST'))
def editar():
    if request.method == 'GET':
        cid = str(request.args.get('id'))
        g.db = MySQLConnection(**db_config)
        cursor = g.db.cursor(prepared=True)
        consulta = ("SELECT * FROM Contato WHERE cID = %s")
        cursor.execute(consulta, (cid))
        linha = cursor.fetchone()
        contato = [
            {
                'id' : linha[0],
                'nome' : linha[1],
                'email' : linha[2]
            }
        ]
        cursor.close()
        g.db.close()

        session['cid'] = cid;
        return render_template('editar.html', title='Editar contato', contato=contato)

    else:
        cid = session['cid']
        nome = request.form['nome']
        email = request.form['email']
        session.pop('cId', None)

        g.db = MySQLConnection(**db_config)
        cursor = g.db.cursor(prepared=True)
        consulta = "UPDATE Contato SET nome = %s, email = %s WHERE cId = %s"
        dados = (nome, email, str(cid))
        cursor.execute(consulta, dados)
        g.db.commit()
        cursor.close()
        g.db.close()

        return redirect(url_for('listar'))



if __name__ == '__main__':
    app.run()
