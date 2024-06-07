from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit
from models import Auction
import hashlib
app = Flask(__name__)
app.config.from_object('config')
socketio = SocketIO(app, async_mode='eventlet')

auction = Auction()
users = {
    'admin@cricket.ipl': hashlib.sha256('admin123'.encode('utf-8')).hexdigest()#PASSWORD FOR AYUSH IPL WEBAPP
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password'].encode('utf-8')  # Encode password for hashing

    if email in users:
        hashed_password = users[email]
        if hashlib.sha256(password).hexdigest() == hashed_password:
            session['logged_in'] = True
            return render_template('auction.html')  # Redirect to homepage after login
        else:
            error_message = "Invalid email or password."
    else:
        error_message = "Invalid email or password."

    return render_template('index.html', error_message=error_message)


@app.route('/auction')
def auction_page():
    return render_template('auction.html', item=auction.item, highest_bid=auction.highest_bid)

@socketio.on('new_bid')
def handle_new_bid(data):
    username = data['username']
    bid = data['bid']

    if auction.place_bid(username, bid):
        emit('update_auction', {'username': username, 'bid': bid}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
