# generate_contributors_md.py
import requests

REPO = "4TUResearchData-Carpentries/GitCoDev"
GITHUB_API = f"https://api.github.com/repos/{REPO}/contributors"
OUTPUT = "gitcodev/contributors.md"
HEADERS = {"Accept": "application/vnd.github+json"}  # optionally add token


def fetch_contributors():
    res = requests.get(GITHUB_API, headers=HEADERS)
    res.raise_for_status()
    return res.json()


def write_markdown(contributors):
    with open(OUTPUT, "w") as f:
        for user in contributors:
            login = user["login"]
            url = user["html_url"]
            contributions = user.get("contributions", "?")

            # Try to get the real name (requires user API call)
            user_info = requests.get(
                f"https://api.github.com/users/{login}", headers=HEADERS
            ).json()
            name = user_info.get("name") or login

            f.write(
                f"{{bdg-link-dark}}`{name} <{url}>`{{octicon}}`commit`{{bdg-dark-line}}`{contributions}`\n"
            )


if __name__ == "__main__":
    contributors = fetch_contributors()
    write_markdown(contributors)
    print(f"✅ Wrote {len(contributors)} contributors to {OUTPUT}")
