import re
import requests
import os
import sys
from dotenv import load_dotenv
load_dotenv()

# Token desde env var
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = os.getenv("REPO")
API = f"https://api.github.com/repos/{REPO}"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

# Paleta para las labels de épica (se asignan en orden de aparición)
EPIC_COLORS = [
    "1d76db", "5319e7", "0e8a16", "b60205", "fbca04", "006b75",
    "d93f0b", "c5def5", "bfd4f2", "d4c5f9", "f9d0c4", "c2e0c6",
]

FIXED_LABELS = {
    "user-story": ("ededed", "Historia de usuario"),
    "etapa-1": ("0052cc", "Etapa 1 del MVP"),
    "etapa-2": ("5319e7", "Etapa 2 del MVP"),
    "opcional": ("cccccc", "Opcional / sujeto a tiempo disponible"),
    "prioridad: no negociable": ("b60205", "Imprescindible para el MVP"),
    "prioridad: recomendable": ("fbca04", "Recomendable para el MVP"),
    "prioridad: valor agregado": ("0e8a16", "Fuera de los 15 requisitos mínimos"),
}

PRIORITY_SECTIONS = {
    "No negociables": "prioridad: no negociable",
    "Recomendables": "prioridad: recomendable",
    "Fuera de los 15 requisitos mínimos": "prioridad: valor agregado",
}


def clean_epic(name):
    # "Jerarquía documental (nuevo)" -> "Jerarquía documental"
    # "Análisis con IA — Opcional (...)" -> "Análisis con IA"
    name = re.split(r"\s+—\s+", name)[0]
    return re.sub(r"\s*\(.*?\)\s*$", "", name).strip()


def status_label(status):
    if not status:
        return None
    etapa = re.match(r"etapa\s*(\d+)", status, re.I)
    if etapa:
        return f"etapa-{etapa.group(1)}"
    if status.lower().startswith("opcional"):
        return "opcional"
    return status.lower()


def parse_priorities(content):
    priorities = {}
    current = None
    for line in content.split("\n"):
        heading = re.match(r"## (.*)", line)
        if heading:
            current = next((label for key, label in PRIORITY_SECTIONS.items()
                            if heading.group(1).startswith(key)), None)
            continue
        item = re.match(r"- (MVP-\d+)", line)
        if current and item:
            priorities[item.group(1)] = current
    return priorities


def parse_dudas(content):
    match = re.search(r"Dudas abiertas.*?:\n(.*?)-->", content, re.S)
    if not match:
        return []
    return [line[2:].strip() for line in match.group(1).split("\n") if line.startswith("- ")]


def parse_readme(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    priorities = parse_priorities(content)
    issues = []
    current_epic = None

    lines = content.split("\n")
    buffer = []
    title = None

    def flush():
        if title:
            issues.append(process_issue(title, buffer, current_epic, priorities))

    for line in lines:
        # Cualquier "## " cierra la historia en curso
        if line.startswith("## "):
            flush()
            title = None
            buffer = []
            epic_match = re.match(r"## Épica: (.*)", line)
            current_epic = clean_epic(epic_match.group(1)) if epic_match else None
            continue

        # Detectar historia
        if line.startswith("### "):
            flush()
            title = re.sub(r"\s*\(nuevo\)\s*$", "", line.replace("### ", "")).strip()
            buffer = []
        elif title:
            buffer.append(line)

    # última historia
    flush()

    return issues, parse_dudas(content)


def format_body(content, epic, status, priority):
    # Sacar comentarios HTML (Status, notas internas)
    content = re.sub(r"<!--.*?-->", "", content, flags=re.S)
    # Normalizar "**Campo:**" -> "**Campo**:"
    content = re.sub(r"\*\*([^*\n]+?):\*\*", r"**\1**:", content)

    # Separar la línea de trazabilidad en sus partes
    points = matriz = trazabilidad = None
    traz_match = re.search(r"^\*\*Trazabilidad\*\*:(.*)$", content, re.M)
    if traz_match:
        for part in traz_match.group(1).split("|"):
            part = part.strip()
            if part.lower().startswith("story points"):
                points = part.split(":", 1)[1].strip()
            elif part.lower().startswith("matriz v1"):
                matriz = part.split(":", 1)[1].strip()
            elif part:
                trazabilidad = part
        content = content.replace(traz_match.group(0), "")

    content = re.sub(r"^\*\*Criterios de aceptación\*\*:?\s*$",
                     "### ✅ Criterios de aceptación", content, flags=re.M)
    # "- CA 1: Título" -> checkbox
    content = re.sub(r"^- (CA \w+):\s*(.*)$", r"- [ ] **\1** — \2", content, flags=re.M)
    # Resaltar Dado / Cuando / Entonces
    content = re.sub(r"^(\s+- )(Dado|Cuando|Entonces)\b", r"\1**\2**", content, flags=re.M)
    content = re.sub(r"\n{3,}", "\n\n", content).strip()

    table = (
        "| Épica | Etapa | Prioridad | Story points |\n"
        "|---|---|---|---|\n"
        f"| {epic or '—'} | {status or '—'} | {priority or '—'} | {points or '—'} |"
    )
    refs = []
    if trazabilidad:
        refs.append(f"**Trazabilidad**: {trazabilidad}")
    if matriz:
        refs.append(f"**Matriz v1**: {matriz}")

    return "\n\n".join(filter(None, [table, " · ".join(refs), "---", content]))


def process_issue(title, buffer, epic, priorities):
    content = "\n".join(buffer)

    # Status
    status_match = re.search(r"<!-- Status: (.*?) -->", content)
    status = status_match.group(1).strip() if status_match else None

    code_match = re.match(r"(MVP-\d+)", title)
    code = code_match.group(1) if code_match else None
    priority = priorities.get(code)

    labels = ["user-story"]
    if status_label(status):
        labels.append(status_label(status))
    if priority:
        labels.append(priority)
    if epic:
        labels.append(f"épica: {epic}")

    body = format_body(content, epic, status,
                       priority.split(": ", 1)[1].capitalize() if priority else None)

    points_match = re.search(r"Story points:\s*(\d+)", content)

    return {
        "code": code,
        "points": points_match.group(1) if points_match else None,
        "title": title,
        "body": body,
        "labels": labels
    }


def ensure_labels(issues):
    existing = set()
    page = 1
    while True:
        response = requests.get(f"{API}/labels", headers=headers,
                                params={"per_page": 100, "page": page})
        response.raise_for_status()
        if not response.json():
            break
        existing |= {label["name"].lower() for label in response.json()}
        page += 1

    epics = list(dict.fromkeys(l for i in issues for l in i["labels"] if l.startswith("épica: ")))
    wanted = dict(FIXED_LABELS)
    for n, epic in enumerate(epics):
        wanted[epic] = (EPIC_COLORS[n % len(EPIC_COLORS)], "")

    used = {l for i in issues for l in i["labels"]}
    for name, (color, description) in wanted.items():
        if name in used and name.lower() not in existing:
            response = requests.post(f"{API}/labels", headers=headers,
                                     json={"name": name, "color": color, "description": description})
            if response.status_code == 201:
                print(f"🏷️  Label creada: {name}")
            else:
                print(f"❌ Error creando label {name}: {response.json()}")


def existing_issues():
    titles = {}
    page = 1
    while True:
        response = requests.get(f"{API}/issues", headers=headers,
                                params={"state": "all", "per_page": 100, "page": page})
        response.raise_for_status()
        if not response.json():
            break
        for item in response.json():
            if "pull_request" not in item:
                titles[item["title"]] = item["number"]
        page += 1
    return titles


def create_issue(issue):
    url = f"{API}/issues"

    data = {
        "title": issue["title"],
        "body": issue["body"],
        "labels": issue["labels"]
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"✅ Creada: #{response.json()['number']} {issue['title']}")
        return response.json()["number"]
    print(f"❌ Error: {response.json()}")
    return None


def post_dudas(dudas, numbers):
    for duda in dudas:
        for code in dict.fromkeys(re.findall(r"MVP-\d+", duda)):
            if code not in numbers:
                continue
            body = f"❓ **Duda abierta**\n\n{duda}"
            response = requests.post(f"{API}/issues/{numbers[code]}/comments",
                                     headers=headers, json={"body": body})
            if response.status_code == 201:
                print(f"💬 Comentario en #{numbers[code]} ({code})")
            else:
                print(f"❌ Error comentando {code}: {response.json()}")


def graphql(query, **variables):
    response = requests.post("https://api.github.com/graphql", headers=headers,
                             json={"query": query, "variables": variables})
    data = response.json()
    if "errors" in data:
        raise RuntimeError(data["errors"])
    return data["data"]


PROJECT_COLORS = ["BLUE", "GREEN", "YELLOW", "ORANGE", "RED", "PINK", "PURPLE", "GRAY"]


def project_fields(project_id):
    data = graphql("""
        query($id: ID!) { node(id: $id) { ... on ProjectV2 { fields(first: 50) { nodes {
            ... on ProjectV2FieldCommon { id name dataType }
            ... on ProjectV2SingleSelectField { options { id name } }
        } } } } }""", id=project_id)
    return {f["name"]: f for f in data["node"]["fields"]["nodes"]}


def ensure_project_field(project_id, fields, name, options=None):
    if name in fields:
        return
    if options:
        select = [{"name": o, "color": PROJECT_COLORS[n % len(PROJECT_COLORS)], "description": ""}
                  for n, o in enumerate(options)]
        graphql("""mutation($p: ID!, $n: String!, $o: [ProjectV2SingleSelectFieldOptionInput!]) {
            createProjectV2Field(input: {projectId: $p, dataType: SINGLE_SELECT, name: $n,
                                         singleSelectOptions: $o}) { clientMutationId } }""",
                p=project_id, n=name, o=select)
    else:
        graphql("""mutation($p: ID!, $n: String!) {
            createProjectV2Field(input: {projectId: $p, dataType: NUMBER, name: $n}) { clientMutationId } }""",
                p=project_id, n=name)
    print(f"🧩 Campo creado en el proyecto: {name}")


def set_project_field(project_id, item_id, field, value):
    if value is None:
        return
    if field["dataType"] == "NUMBER":
        value_input = {"number": float(value)}
    else:
        option = next(o["id"] for o in field["options"] if o["name"] == value)
        value_input = {"singleSelectOptionId": option}
    graphql("""mutation($p: ID!, $i: ID!, $f: ID!, $v: ProjectV2FieldValue!) {
        updateProjectV2ItemFieldValue(input: {projectId: $p, itemId: $i, fieldId: $f, value: $v}) {
            clientMutationId } }""", p=project_id, i=item_id, f=field["id"], v=value_input)


def add_to_project(issues, project_number):
    owner = REPO.split("/")[0]
    project = graphql("""query($o: String!, $n: Int!) {
        organization(login: $o) { projectV2(number: $n) { id title } } }""",
                      o=owner, n=project_number)["organization"]["projectV2"]
    print(f"📋 Proyecto: {project['title']}")

    def label_value(issue, prefix):
        return next((l.split(": ", 1)[1] for l in issue["labels"] if l.startswith(prefix)), None)

    def etapa(issue):
        return next((l.replace("etapa-", "Etapa ").capitalize() for l in issue["labels"]
                     if l.startswith("etapa-") or l == "opcional"), None)

    values = {
        "Épica": lambda i: label_value(i, "épica: "),
        "Etapa": etapa,
        "Prioridad": lambda i: (label_value(i, "prioridad: ") or "").capitalize() or None,
    }
    for name, get in values.items():
        ensure_project_field(project["id"], project_fields(project["id"]), name,
                             list(dict.fromkeys(filter(None, map(get, issues)))))
    ensure_project_field(project["id"], project_fields(project["id"]), "Story points")
    fields = project_fields(project["id"])

    node_ids = {}
    page = 1
    while True:
        response = requests.get(f"{API}/issues", headers=headers,
                                params={"state": "all", "per_page": 100, "page": page})
        response.raise_for_status()
        if not response.json():
            break
        node_ids.update({i["title"]: i["node_id"] for i in response.json()})
        page += 1

    for issue in issues:
        if issue["title"] not in node_ids:
            continue
        item_id = graphql("""mutation($p: ID!, $c: ID!) {
            addProjectV2ItemById(input: {projectId: $p, contentId: $c}) { item { id } } }""",
                          p=project["id"], c=node_ids[issue["title"]])["addProjectV2ItemById"]["item"]["id"]
        set_project_field(project["id"], item_id, fields["Status"],
                          fields["Status"]["options"][0]["name"] if "Status" in fields else None)
        for name, get in values.items():
            set_project_field(project["id"], item_id, fields[name], get(issue))
        set_project_field(project["id"], item_id, fields["Story points"], issue["points"])
        print(f"📌 En el proyecto: {issue['title']}")


def main():
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry_run = "--dry-run" in sys.argv
    # Archivo de historias por argumento; por defecto issues_GeDoC_mvp.md
    file_path = args[0] if args else "issues_GeDoC_mvp.md"
    issues, dudas = parse_readme(file_path)

    if dry_run:
        for issue in issues:
            print(f"===== {issue['title']}  {issue['labels']}\n{issue['body']}\n")
        print(f"Dudas: {dudas}")
        return

    ensure_labels(issues)
    already = existing_issues()

    numbers = {}
    for issue in issues:
        if issue["title"] in already:
            print(f"⏭️  Ya existe: #{already[issue['title']]} {issue['title']}")
            continue
        number = create_issue(issue)
        if number:
            numbers[issue["code"]] = number

    # Solo se comenta en las issues recién creadas, para no duplicar comentarios
    post_dudas(dudas, numbers)

    # Número del proyecto de la organización (opcional), ej. PROJECT_NUMBER=1
    if os.getenv("PROJECT_NUMBER"):
        add_to_project(issues, int(os.getenv("PROJECT_NUMBER")))


if __name__ == "__main__":
    main()
