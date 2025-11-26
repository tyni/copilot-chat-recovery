import os

CHUNK_FOLDER = "copilot_chunks_html"
OUTPUT_FILE = "Copilot_QA_Archive_v0.txt"

qa_entries = []

import re

def extract_first_paragraph(lines, start_index):
    paragraph = []
    emoji_section_starters = (
        "🔑", "💡", "🚀", "✅", "📌", "📈", "📊", "📋", "📝", "🔍", "🔧", "🛠️", "🧠", "📦", "🎯", "🎨", "🧪", "🔬",
        "🧭", "🔥", "🧵", "🏠", "✨", "🏗️", "⚙", "🧾", "🟢", "🧱", "📁", "✍️", "🧶", "🛎️", "🧰", "🧩", "🧼", "🧴",
        "🧨", "🧃", "🧊", "🧸", "🧳", "🧺", "🧽", "🧯", "🧿", "🔒", "🔓", "🔔", "🔕", "🔗", "🔄", "🔁", "🔂", "🔃",
        "🔙", "🔚", "🔛", "🔜", "🔝"
    )

    for i, line in enumerate(lines[start_index:]):
        stripped = line.strip()

        # Always allow the first line
        if i == 0:
            if stripped.lower() == "copilot said":
                continue  # skip "Copilot said" if it's the only thing
            paragraph.append(stripped)
            continue

        # Stop if line is empty or starts with a new section marker
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

            # Find user message
            for i, line in enumerate(lines):
                if line.startswith("🧑"):
                    user_line = line.strip()
                    for follow_line in lines[i+1:]:
                        if follow_line.startswith("🤖"):
                            break
                        user_text.append(follow_line.strip())
                    break

            # Find Copilot response (first paragraph only)
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

# Save the archive
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(qa_entries))

print(f"✅ Q&A archive (first paragraph only) saved to '{OUTPUT_FILE}'")
