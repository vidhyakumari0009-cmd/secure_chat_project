from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

users = {}      # username -> socket id
typing_users = {}

@app.route("/")
def index():
    return render_template("chat.html")


# USER JOIN
@socketio.on("join")
def join(data):
    username = data["username"]

    users[username] = request.sid

    print(username, "joined")

    emit("user_list", list(users.keys()), broadcast=True)


# MESSAGE ROUTING (SERVER CAN'T READ MESSAGE)
@socketio.on("send_message")
def send_message(data):

    receiver = data["to"]

    if receiver in users:
        emit(
            "receive_message",
            data,
            to=users[receiver]
        )


# TYPING INDICATOR
@socketio.on("typing")
def typing(data):

    receiver = data["to"]

    if receiver in users:
        emit(
            "typing",
            {"from": data["from"]},
            to=users[receiver]
        )


# DISCONNECT
@socketio.on("disconnect")
def disconnect():

    disconnected_user = None

    for u, sid in users.items():
        if sid == request.sid:
            disconnected_user = u

    if disconnected_user:
        users.pop(disconnected_user)

    emit("user_list", list(users.keys()), broadcast=True)


if __name__ == "__main__":
    socketio.run(app, debug=True)
