🧠 Copilot Q&A Archiver
Recover and reuse your Copilot conversations — extract clean Q&A pairs from saved chats.

✨ Why Use This?
This tool helps you preserve long, rich Copilot chats and re-enter them later for tagging, summarizing, or continuing the conversation.

This is especially useful when you’ve had a long, rich conversation and want to preserve or build on it outside the chat interface.

🚀 Features
Extracts user + Copilot messages from saved HTML

Splits into chunked .txt files

Captures only the first paragraph of Copilot’s response

Outputs a clean Q&A archive

🛠 Requirements
Python 3.9+

beautifulsoup4 (install with pip install beautifulsoup4)

💾 How to Save Your Conversation
Instead of copying text manually, use Developer Tools:

Open your Copilot conversation in a browser

Press F12 to open Developer Tools

In the Elements tab, scroll to the top

Right-click the <html> tag → Copy → Copy outerHTML

Paste into a text editor and save as:

Code
copilot_conversation.html
✂️ Step 1: Chunker Script
Create chunker.py:

python
from bs4 import BeautifulSoup
import os

INPUT_FILE = "copilot_conversation.html"
CHUNK_FOLDER = "copilot_chunks_html"

os.makedirs(CHUNK_FOLDER, exist_ok=True)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

user_blocks = soup.find_all("div", attrs={"data-content": "user-message"})
ai_blocks = soup.find_all("div", attrs={"data-content": "ai-message"})

chunks = []
for user, ai in zip(user_blocks, ai_blocks):
    user_name = user.find_previous("div", class_="text-foreground-600").get_text(strip=True)
    user_text = user.get_text(separator="\n", strip=True)
    ai_text = ai.get_text(separator="\n", strip=True)
    chunk = f"🧑 {user_name}:\n{user_text}\n\n🤖 Copilot:\n{ai_text}"
    chunks.append(chunk)

for i, chunk in enumerate(chunks, 1):
    with open(f"{CHUNK_FOLDER}/chunk_{i:04}.txt", "w", encoding="utf-8") as f:
        f.write(chunk)

print(f"✅ Saved {len(chunks)} chunks to '{CHUNK_FOLDER}' folder.")
Run it:

bash
python chunker.py
🧠 Step 2: Q&A Extractor Script
Create extract_qa.py:

python
import os
import re

CHUNK_FOLDER = "copilot_chunks_html"
OUTPUT_FILE = "copilot_qa_archive.txt"

qa_entries = []

emoji_section_starters = (
    "🔑", "💡", "🚀", "✅", "📌", "📈", "📊", "📋", "📝", "🔍", "🔧", "🛠️", "🧠", "📦", "🎯", "🎨", "🧪", "🔬",
    "🧭", "🔥", "🧵", "🏠", "✨", "🏗️", "⚙", "🧾", "🟢", "🧱", "📁", "✍️", "🧶", "🛎️", "🧰", "🧩", "🧼", "🧴",
    "🧨", "🧃", "🧊", "🧸", "🧳", "🧺", "🧽", "🧯", "🧿", "🔒", "🔓", "🔔", "🔕", "🔗", "🔄", "🔁", "🔂", "🔃",
    "🔙", "🔚", "🔛", "🔜", "🔝"
)

def extract_first_paragraph(lines, start_index):
    paragraph = []
    for i, line in enumerate(lines[start_index:]):
        stripped = line.strip()
        if i == 0:
            if stripped.lower() == "copilot said":
                continue
            paragraph.append(stripped)
            continue
        if (
            stripped == "" or
            stripped.startswith("🧑") or
            stripped.startswith("🤖") or
            re.match(r"^[-•*#]+", stripped) or
            re.match(r"^\d+\.", stripped) or
            any(stripped.startswith(icon) for icon in emoji_section_starters)
        ):
            break
        paragraph.append(stripped)
    return paragraph

for filename in sorted(os.listdir(CHUNK_FOLDER)):
    if filename.endswith(".txt"):
        with open(os.path.join(CHUNK_FOLDER, filename), "r", encoding="utf-8") as f:
            lines = f.readlines()
            user_line = None
            user_text = []
            copilot_line = None
            copilot_text = []

            for i, line in enumerate(lines):
                if line.startswith("🧑"):
                    user_line = line.strip()
                    for follow_line in lines[i+1:]:
                        if follow_line.startswith("🤖"):
                            break
                        user_text.append(follow_line.strip())
                    break

            for i, line in enumerate(lines):
                if line.startswith("🤖"):
                    copilot_line = line.strip()
                    copilot_text = extract_first_paragraph(lines, i + 1)
                    break

            if user_line and copilot_line:
                qa_entries.append(
                    f"--- {filename} ---\n{user_line}\n" +
                    "\n".join(user_text) + "\n\n" +
                    f"{copilot_line}\n" +
                    "\n".join(copilot_text) + "\n"
                )

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(qa_entries))

print(f"✅ Q&A archive saved to '{OUTPUT_FILE}'")
Run it:

bash
python extract_qa.py
✅ Step 3: Verify the Output
Open copilot_qa_archive.txt and confirm:

txt
--- chunk_0001.txt ---
🧑 Alex:
How can I improve my productivity when working from home?

🤖 Copilot:
One of the most effective ways to boost productivity at home is to establish a consistent routine and dedicated workspace.
🔄 Getting Back to That Conversation We Had
This entire workflow is designed to help you recover and reuse your Copilot conversations in a structured, portable format. By extracting clean Q&A pairs, you can:

Revisit important insights or answers Copilot gave you

Re-enter questions into a new chat to continue the discussion

Tag, summarize, or organize your archive for future reference

Share your conversation with collaborators or publish it as documentation

📤 Share or Paste Back for Review
Split the archive into parts if needed (e.g., “Part 1 of 5”)

Paste into a new Copilot chat to continue the conversation or tag responses

Use the archive as a searchable reference, documentation, or training material

🧠 Quick Reference
Conversation Save Method: F12 → Elements tab → Right-click <html> → Copy outerHTML

Saved File: copilot_conversation.html

Chunk Output Folder: copilot_chunks_html/

Chunk Files: chunk_0001.txt, chunk_0002.txt, etc.

Final Output: copilot_qa_archive.txt

Python Packages: beautifulsoup4

Scripts: chunker.py and extract_qa.py

Stop Rules: blank lines, bullets, emoji headers, role markers

Emoji Headers: 🔑 💡 🚀 ✅ 📌 📈 📊 📋 📝 🔍 🔧 🛠️ 🧠 📦 🎯 🎨 🧪 🔬 🧭 🔥 🧵 🏠 ✨ 🏗️ ⚙ 🧾 🟢 🧱 📁 ✍️ 🧶 🛎️ 🧰 🧩 🧼 🧴 🧨 🧃 🧊 🧸 🧳 🧺 🧽 🧯 🧿 🔒 🔓 🔔 🔕 🔗 🔄 🔁 🔂 🔃 🔙 🔚 🔛 🔜 🔝

