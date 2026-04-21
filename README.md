# 🌐 MPI Client-Server Model (Distributed System Project)

## 📌 Project Overview

The **MPI Client-Server Model** is a distributed computing project implemented using **MPI (Message Passing Interface)** with Python (mpi4py). It demonstrates how multiple clients communicate with a central server in a parallel computing environment.

This project is designed to understand **message passing, process communication, and distributed system architecture**.

---

## 🎯 Objectives

* Implement client-server communication using MPI
* Understand parallel and distributed computing concepts
* Manage multiple processes simultaneously
* Demonstrate message passing between nodes

---

## 🚀 Features

### 🖥️ Server Features

* Receives messages from multiple clients
* Processes and responds to requests
* Coordinates communication between nodes

### 👨‍💻 Client Features

* Sends requests to server
* Receives responses
* Supports multiple concurrent clients

### 🔄 System Features

* Parallel execution of processes
* Efficient message passing
* Synchronized communication

---

## ⚙️ Tech Stack

* 💻 **Language:** Python
* 🌐 **Library:** mpi4py (MPI for Python)
* 🧠 **Concepts Used:**

  * Distributed Computing
  * Message Passing Interface (MPI)
  * Parallel Processing

---

## 📂 Project Structure

```id="mpq7k2"
MPI-Client-Server/
│
├── server.py
├── client.py
├── config.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 🔹 Step 1: Install MPI

Install MPI (if not installed):

```bash id="c2m8qa"
sudo apt-get install mpich
```

### 🔹 Step 2: Install Python MPI Library

```bash id="f9q2ws"
pip install mpi4py
```

---

### 🔹 Step 3: Run Server & Clients

Run using MPI:

```bash id="kq8p1a"
mpiexec -n 1 python server.py
```

Run clients (example: 3 clients):

```bash id="z9m2fd"
mpiexec -n 3 python client.py
```

---

## 📸 Output Example

```id="p3w8xq"
Client 1 → Message sent to server
Server → Processing request
Server → Response sent back to Client 1
```

---

## 🔮 Future Improvements

* 🌍 Add real-time chat system between clients
* 🧠 Implement load balancing on server
* 📊 Add performance monitoring
* 🔐 Secure communication using encryption

---

## 👨‍💻 Author

**Saleha ibrar**

* GitHub: https://github.com/malikzain13

---

⭐ *If you like this project, please star the repository!*
