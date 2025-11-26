# 🧠 Copilot Q&A Archiver

Recover and reuse your Copilot conversations — extract clean Q&A pairs from saved chats.

---

## ✨ Why Use This?

This tool helps you preserve long, rich Copilot chats and re-enter them later for tagging, summarizing, or continuing the conversation.

> This is especially useful when you’ve had a long, rich conversation and want to preserve or build on it outside the chat interface.

---

## 🚀 Features

- Extracts user + Copilot messages from saved HTML
- Splits into chunked `.txt` files
- Captures only the first paragraph of Copilot’s response
- Outputs a clean Q&A archive

---

## 🛠 Requirements

- Python 3.9+
- `beautifulsoup4` (install with `pip install beautifulsoup4`)

---

## 📖 Setup Guide

See the full step-by-step guide:  
👉 [`copilot_qa_guide.html`](copilot_qa_guide.html)

---

## 📂 Sample Files

- `copilot_conversation.html` — raw HTML from DevTools
- `chunk_0001.txt` — formatted chunk
- `copilot_qa_archive.txt` — final output

---

## 🧪 Try It

1. Save your Copilot chat via DevTools → Copy outerHTML
2. Run `chunker.py` to create chunks
3. Run `extract_qa.py` to build your archive

---

## 📤 Step 8: Share or Paste Back for Review

- Split the archive into parts if needed (e.g., “Part 1 of 5”)
- Paste into a new Copilot chat to continue the conversation or tag responses
- Use the archive as a searchable reference, documentation, or training material

---

## 🔄 Step 9: Getting Back to That Conversation We Had

This entire workflow is designed to help you **recover and reuse** your Copilot conversations in a structured, portable format. By extracting clean Q&A pairs, you can:

- Revisit important insights or answers Copilot gave you
- Re-enter questions into a new chat to continue the discussion
- Tag, summarize, or organize your archive for future reference
- Share your conversation with collaborators or publish it as documentation

---

## 🧠 Quick Reference

- **Conversation Save Method:** F12 → Elements tab → Right-click `<html>` → Copy outerHTML
- **Saved File:** `copilot_conversation.html`
- **Chunk Output Folder:** `copilot_chunks_html/`
- **Chunk Files:** `chunk_0001.txt`, `chunk_0002.txt`, etc.
- **Final Output:** `copilot_qa_archive.txt`
- **Python Packages:** `beautifulsoup4`
- **Scripts:** `chunker.py` and `extract_qa.py`
- **Stop Rules:** blank lines, bullets, emoji headers, role markers
- **Emoji Headers:** 🔑 💡 🚀 ✅ 📌 📈 📊 📋 📝 🔍 🔧 🛠️ 🧠 📦 🎯 🎨 🧪 🔬 🧭 🔥 🧵 🏠 ✨ 🏗️ ⚙ 🧾 🟢 🧱 📁 ✍️ 🧶 🛎️ 🧰 🧩 🧼 🧴 🧨 🧃 🧊 🧸 🧳 🧺 🧽 🧯 🧿 🔒 🔓 🔔 🔕 🔗 🔄 🔁 🔂 🔃 🔙 🔚 🔛 🔜 🔝

---

## 🧪 Sample Conversation (for Testing)

```txt
🧑 Alex:
How can I improve my productivity when working from home?

🤖 Copilot:
One of the most effective ways to boost productivity at home is to establish a consistent routine and dedicated workspace. This helps signal to your brain that it's time to focus.

🧑 Alex:
What are some tools that can help with time management?

🤖 Copilot:
Time-blocking apps like Google Calendar, task managers like Todoist, and focus timers such as Pomofocus can help you structure your day and stay on track.

🧑 Alex:
How do I avoid burnout?

🤖 Copilot:
Burnout can be prevented by setting clear work-life boundaries, taking regular breaks, and prioritizing rest and recovery as much as productivity.
