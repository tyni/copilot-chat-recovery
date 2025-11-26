from bs4 import BeautifulSoup
import os

INPUT_FILE = "copilot_conversation.html"
CHUNK_FOLDER = "copilot_chunks_html"

# Create output folder
os.makedirs(CHUNK_FOLDER, exist_ok=True)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Find all user and AI messages
user_blocks = soup.find_all("div", attrs={"data-content": "user-message"})
ai_blocks = soup.find_all("div", attrs={"data-content": "ai-message"})

chunks = []
for user, ai in zip(user_blocks, ai_blocks):
    # Extract user name and message
    user_name = user.find_previous("div", class_="text-foreground-600").get_text(strip=True)
    user_text = user.get_text(separator="\n", strip=True)

    # Extract AI response
    ai_text = ai.get_text(separator="\n", strip=True)

    # Format chunk
    chunk = f"🧑 {user_name}:\n{user_text}\n\n🤖 Copilot:\n{ai_text}"
    chunks.append(chunk)

# Save each chunk
for i, chunk in enumerate(chunks, 1):
    with open(f"{CHUNK_FOLDER}/chunk_{i:04}.txt", "w", encoding="utf-8") as f:
        f.write(chunk)

print(f"✅ Saved {len(chunks)} chunks to '{CHUNK_FOLDER}' folder.")
