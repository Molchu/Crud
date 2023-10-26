from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify


app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.config['MONGO_URI'] = 'mongodb://logindb:27017/login'  # Reemplaza con la URI de tu base de datos
logindb = PyMongo(app)
app.config['MONGO_URI'] = 'mongodb://crud-router:27017/data'  # Reemplaza con la URI de tu base de datos
datadb = PyMongo(app)



@app.route('/delete/<string:id>')
def delete(id):
    logindb.db.users.delete_one({'_id': ObjectId(id)})
    flash('Registro eliminado con éxito', 'success')
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST']) 
def register():
    if request.method == 'POST':
        uName = request.form['uName']
        uEmail = request.form['uEmail']
        uDocumento = request.form['uDocument']
        uUser = request.form['uUser']
        uCellphone = request.form['uCellphone']
        uPassword = request.form['uPassword']
        
        hashed_password = generate_password_hash(uPassword, method='sha256')
        
        users = logindb.db.users
        result = users.insert_one({
            'username': uUser,
            'password': hashed_password,
            'uName': uName,
            'uEmail': uEmail,
            'uDocument': uDocumento,
            'uCellphone': uCellphone
        })
        
        flash('Usuario registrado con éxito', 'success')
        return redirect(url_for('home'))
    
    return render_template('register.html')

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    users = logindb.db.users
    users.update_one(
        {'_id': ObjectId(id)},
        {
            "$set": {
                "username": request.form['uUser'],
                "password": request.form['uPassword'],
                "uName": request.form['uName'],
                "uEmail": request.form['uEmail'],
                "uDocument": request.form['uDocument'],
                "uCellphone": request.form['uCellphone'],
                
            }
        }
    )
    return redirect(url_for('home'))

@app.route('/home')
def home():
    if 'username' in session:
        users = logindb.db.users
        all_users_data = list(users.find())
        return render_template('home.html', all_users_data=all_users_data)
    else:
        return redirect(url_for('login'))
    

    




@app.route('/', methods=['GET', 'POST'])
def login():
    users = logindb.db.users

    if users.find_one({"username": "root"}) is None:
        root_password = "root"  # Cambia "your_root_password" por tu contraseña real
        hashed_password = generate_password_hash(root_password, method='sha256')

        user_data = {
            'username': "root",
            'password': hashed_password,
            'uName': "root",
            'uEmail': "root@root.com",
            'uDocument': "root",  
            'uCellphone': "root"
        }
        users.insert_one(user_data)
        
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user_data = users.find_one({'username': username})
        
        if user_data and check_password_hash(user_data['password'], password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Credenciales inválidas. Inténtalo de nuevo.', 'danger')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)