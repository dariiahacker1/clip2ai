# 📋 clip2ai — Your Silent AI Clipboard Assistant

Send prompts from your clipboard to OpenAI, and get the response instantly back — copied to your clipboard.  
A silent, local AI assistant powered by GPT.

---

## 🚀 What is clip2ai?

**clip2ai** is a simple yet powerful tool that connects your clipboard to OpenAI’s GPT API.  
Just copy any text, trigger the script, and the AI response is instantly placed back on your clipboard — ready to paste anywhere.

> Ideal for quick lookups, rewriting text, solving code or math problems — all without leaving your workflow.

---

## ⌨️ Full Automation with Keyboard Shortcut

You can bind the script to a custom keyboard shortcut through your system settings for instant, one-key AI responses.

---

## 🎓 Perfect for Students

- Quickly summarize, solve, or explain questions with GPT during study sessions or assignments.
- Bind the script to a **keyboard shortcut** using automation tools (like AutoHotKey, Task Scheduler, or equivalent).
- Stay focused — no browser tabs or UI distractions.

---

## 🧠 How It Works

1. A `Flask` server receives prompts and queries the GPT-4o model.
2. A script reads from your clipboard, sends the prompt to the server, and copies the result back.
3. Optionally, a desktop notification confirms the result.

---

## 📄 Installation

1. **Clone the repo:**

```bash
git clone https://github.com/dariiahacker1/clip2ai.git
cd clip2ai
