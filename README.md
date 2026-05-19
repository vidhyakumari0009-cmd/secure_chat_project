# Secure Chat Application with End-to-End Encryption

## Project Overview

Secure Chat is a real-time private messaging web application that implements **End-to-End Encryption (E2EE)** using client-side cryptography.

The application allows multiple users to communicate securely while ensuring that **messages remain unreadable to the server**. Only the sender and receiver can decrypt messages.

---

## Objective

To design and implement a secure chat system that:

- Provides real-time communication
- Uses public-key based secure key exchange
- Encrypts messages on the client side
- Prevents the server from reading chat content
- Simulates modern messaging applications

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend server |
| Flask | Web framework |
| Flask-SocketIO | Real-time communication |
| HTML/CSS | User Interface |
| JavaScript | Client-side logic |
| CryptoJS | AES Encryption |
| Diffie-Hellman | Secure key exchange |
| WebSockets | Live messaging |

---

## Security Architecture

### Key Exchange (Diffie-Hellman)

Each user generates:

- A **Private Key** (kept secret on client)
- A **Public Key** (shared with other users)

Public Key generation:
PublicKey = g^PrivateKey mod p

Shared Secret computation:
SharedSecret = OtherUserPublicKey^PrivateKey mod p


Both users independently generate the **same shared secret key** without transmitting it over the network.

---

### Message Encryption (AES)

After establishing the shared secret:

1. Messages are encrypted using AES encryption.
2. Encryption happens on the sender's device.
3. The server only forwards encrypted data.
4. The receiver decrypts messages locally.

Communication Flow:
Sender → Encrypt → Server → Receiver → Decrypt


---

## Application Features

- Real-time messaging using WebSockets
- End-to-End Encryption
- Secure key exchange mechanism
- Multiple users and contact list
- Private user-to-user chats
- Typing indicator
- Message timestamps
- Auto-scroll chat window
- Username-based login

---

## Project Structure
secure_chat/
│
├── app.py
├── templates/
│ └── chat.html
├── requirements.txt
└── README.md


### Install Dependencies
pip install flask flask-socketio eventlet


### Run Application
python app.py


### Open Browser
http://localhost:5000


Open multiple browser tabs to simulate multiple users.

---

## How the System Works

1. User enters a username.
2. Server maintains list of active users.
3. Users select contacts to start chatting.
4. Diffie-Hellman generates a shared secret key.
5. Messages are encrypted using AES before sending.
6. Server routes encrypted messages.
7. Receiver decrypts messages locally.

---

## Security Properties

| Property | Implementation |
|----------|---------------|
| Confidentiality | AES Encryption |
| Secure Key Exchange | Diffie-Hellman |
| Real-Time Messaging | Flask-SocketIO |
| Server Trust | Server cannot read messages |

---

## Future Enhancements

- RSA-based key exchange
- Group chat support
- Media and file sharing
- Progressive Web App installation
- Cloud deployment
- Message delivery and read receipts

---

## Author

Yadav Vidhya Kumari
Secure Chat Application Project

---

## License

This project is developed for educational and academic purposes.
