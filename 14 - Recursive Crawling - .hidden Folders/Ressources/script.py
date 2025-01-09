import os
import requests
from bs4 import BeautifulSoup

BASE_URL = "http://192.168.122.121/.hidden"

OUTPUT_FILE = "readme_contents.txt"


def fetch_page(url):
    """Télécharge le contenu d'une URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'accès à {url}: {e}")
        return None


def parse_directory(url):
    """Analyse un répertoire pour trouver des sous-dossiers et des fichiers README."""
    page_content = fetch_page(url)
    if not page_content:
        return [], []

    soup = BeautifulSoup(page_content, 'html.parser')
    links = soup.find_all('a')

    subdirs = []
    readmes = []

    for link in links:
        href = link.get('href')
        if href and not href.startswith("../"):
            if href.endswith("/"):
                subdirs.append(href)
            elif href.lower() == "readme":
                readmes.append(href)

    return subdirs, readmes


def collect_readmes(base_url, current_path=""):
    """Récupère les contenus des README dans le répertoire courant et ses sous-dossiers."""
    full_url = f"{base_url}/{current_path}"
    subdirs, readmes = parse_directory(full_url)

    readme_contents = []

    for readme in readmes:
        readme_url = f"{full_url}/{readme}"
        content = fetch_page(readme_url)
        if content:
            readme_contents.append(content)

    for subdir in subdirs:
        subdir_path = f"{current_path}/{subdir}".strip("/")
        readme_contents.extend(collect_readmes(base_url, subdir_path))

    return readme_contents


def main():
    print(f"Exploration du site {BASE_URL} pour collecter les contenus des fichiers README...")
    readme_contents = collect_readmes(BASE_URL)

    if readme_contents:
        print(f"{len(readme_contents)} README trouvés. Écriture dans {OUTPUT_FILE}...")
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            for content in readme_contents:
                f.write(content + "\n\n")
        print(f"Terminé. Contenus des README enregistrés dans {OUTPUT_FILE}.")
    else:
        print("Aucun README trouvé.")


if __name__ == "__main__":
    main()

