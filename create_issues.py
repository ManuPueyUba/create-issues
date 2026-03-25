import re
import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Token desde env var
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = os.getenv("REPO")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}


def parse_readme(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    issues = []
    current_epic = None

    lines = content.split("\n")
    buffer = []
    title = None

    for line in lines:
        # Detectar épica
        epic_match = re.match(r"## Épica: (.*)", line)
        if epic_match:
            current_epic = epic_match.group(1).strip().lower()
            continue

        # Detectar historia
        if line.startswith("### "):
            if title:
                issues.append(process_issue(title, buffer, current_epic))

            title = line.replace("### ", "").strip()
            buffer = []
        else:
            buffer.append(line)

    # última historia
    if title:
        issues.append(process_issue(title, buffer, current_epic))

    return issues


def process_issue(title, buffer, epic):
    content = "\n".join(buffer)

    # Status
    status_match = re.search(r"<!-- Status: (.*?) -->", content)
    status = status_match.group(1).strip().lower() if status_match else None

    labels = []

    if status:
        labels.append(status)

    if epic:
        labels.append(f"epica:{epic}")

    labels.append("user-story")

    body = f"### {title}\n{content.strip()}"

    return {
        "title": title,
        "body": body,
        "labels": labels
    }


def create_issue(issue):
    url = f"https://api.github.com/repos/{REPO}/issues"

    data = {
        "title": issue["title"],
        "body": issue["body"],
        "labels": issue["labels"]
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"✅ Creada: {issue['title']}")
    else:
        print(f"❌ Error: {response.json()}")


def main():
    issues = parse_readme("issues.md")

    for issue in issues:
        create_issue(issue)


if __name__ == "__main__":
    main()