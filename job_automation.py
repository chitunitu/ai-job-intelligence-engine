import os
from dotenv import load_dotenv
from groq import Groq

def read_job(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def generate_proposal(text: str, client: Groq) -> str:
    prompt = f"""
You write Upwork proposals that are short, specific, and conversion-focused.

JOB DESCRIPTION:
{text[:2000]}

Return EXACTLY this format (no extra lines, no markdown, no bold):

TITLE: <7-10 word title>

PROPOSAL:
<90-120 words total, max 2 short paragraphs.>
Mention 2 very likely issues from the job (concrete).
Offer a 2-step plan.
Ask 2 clarifying questions.
End with a 1-line CTA.

CHECKLIST:
- <deliverable 1>
- <deliverable 2>
- <deliverable 3>

STRICT RULES:
- Output only TITLE/PROPOSAL/CHECKLIST sections.
- No headings like "Proposal for..." and no extra commentary.
- CHECKLIST must be exactly 3 bullets.
""".strip()

    chat = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=260,
    )
    return chat.choices[0].message.content.strip()

def main():
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key or not api_key.startswith("gsk_"):
        raise RuntimeError("Missing GROQ_API_KEY in .env")

    client = Groq(api_key=api_key)

    path = input("Paste job text file path (or press Enter to paste manually): ").strip()

    if path:
        text = read_job(path)
    else:
        print("Paste the job description. End with an empty line:")
        lines = []
        while True:
            line = input()
            if not line.strip():
                break
            lines.append(line)
        text = "\n".join(lines).strip()

    if not text:
        print("No job description provided. Exiting.")
        return

    proposal = generate_proposal(text, client)
    print("\n=== GENERATED PROPOSAL ===\n")
    print(proposal)

if __name__ == "__main__":
    main()
