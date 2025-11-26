# 🧠 Copilot Q&A Archiver

Recover and reuse your Copilot conversations — extract clean Q&A pairs from saved chats.

## ✨ Why Use This?

This tool helps you preserve long, rich Copilot chats and re-enter them later for tagging, summarizing, or continuing the conversation.

## 🚀 Features

- Extracts user + Copilot messages from saved HTML
- Splits into chunked `.txt` files
- Captures only the first paragraph of Copilot’s response
- Outputs a clean Q&A archive

## 🛠 Requirements

- Python 3.9+
- `beautifulsoup4` (install with `pip install beautifulsoup4`)

## 📖 Setup Guide

See the full step-by-step guide:  
👉 [`copilot_qa_guide.html`](copilot_qa_guide.html)

## 📂 Sample Files

- `copilot_conversation.html` — raw HTML from DevTools
- `chunk_0001.txt` — formatted chunk
- `copilot_qa_archive.txt` — final output

## 🧪 Try It

1. Save your Copilot chat via DevTools → Copy outerHTML
2. Run `chunker.py` to create chunks
3. Run `extract_qa.py` to build your archive
