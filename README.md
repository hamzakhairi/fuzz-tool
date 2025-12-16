# ☠️ FUZZBR00T – FTP / SSH Bruteforce Tool

> **Fast. Silent. Brutal.**  
> A hybrid bruteforce tool using **Python as frontend** and **C++ as backend** for maximum performance.

---

## 🔥 Overview

**FUZZBR00T** is a command-line bruteforce tool designed for **FTP and SSH services**.  
It uses a **Python frontend** for flexibility and CLI parsing, while the **core bruteforce engine is written in C++** to achieve high speed and low-level control.

This architecture gives you:
- 🧠 Easy scripting (Python)
- ⚡ Extreme speed (C++)
- ☠️ Clean separation between logic & performance

---

## 🧠 Architecture

```text
┌──────────────┐
│   Python     │
│  Frontend    │  → CLI / Parsing / UX / Config
└──────┬───────┘
       │ JSON 
┌──────▼───────┐
│    C++       │
│  Backend     │  → Bruteforce Engine / Threads / Network
└──────────────┘
```

how to use 

```
python3 main.py FTP admin:FUZZ@10.10.10.12:21 -w /usr/share/wordlists/rockyou.txt

    ███████╗██╗   ██╗███████╗███████╗
    ██╔════╝██║   ██║╚══███╔╝╚══███╔╝
    █████╗  ██║   ██║  ███╔╝   ███╔╝ 
    ██╔══╝  ██║   ██║ ███╔╝   ███╔╝  
    ██║     ╚██████╔╝███████╗███████╗
    ╚═╝      ╚═════╝ ╚══════╝╚══════╝

    ☠️  FTP / SSH BRUTE FORCE TOOL
    👁️  NO MERCY FOR WEAK PASSWORDS
    🔥  USE RESPONSIBLY

    [+] Loading dark modules......

    [☠️] SERVICE  : FTP
    [☠️] USER     : admin
    [☠️] TARGET   : 10.10.10.12:21
    [☠️] WORDLIST : /usr/share/wordlists/rockyou.txt
    [😈] Bruteforce initializing...
```
