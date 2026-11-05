
import subprocess
import json


def get_github_repositories(org="github", limit=5):

    command = [
        "cmd.exe",
        "/c",
        "swytchcode",
        "exec",
        "github.repo.get",
        "--input", f"org={org}",
        "--param", f"per_page={limit}",
        "--json"
    ]

    try:
        result = subprocess.run(
	command,
    	capture_output=True,
    	text=True,
    	encoding="utf-8",
    	errors="replace",
    	check=True
	)

        data = json.loads(result.stdout.strip())
        return data.get("data", [])

    except subprocess.CalledProcessError as error:
        print("Swytchcode execution failed:")
        print(error.stderr)
        print(error.stdout)
        return []

    except json.JSONDecodeError:
        print("Could not parse API response.")
        print(result.stdout)
        return []


if __name__ == "__main__":

    organization = input("Enter GitHub organization: ").strip()

    repositories = get_github_repositories(organization)

    print("\n========== GITHUB REPOSITORY EXPLORER ==========\n")

    if repositories:
        for index, repo in enumerate(repositories, start=1):
            print(f"Repository {index}: {repo.get('full_name')}")
            print(f"Description: {repo.get('description')}")
            print(f"Language: {repo.get('language')}")
            print(f"Stars: {repo.get('stargazers_count')}")
            print(f"Forks: {repo.get('forks_count')}")
            print(f"URL: {repo.get('html_url')}")
            print("-" * 50)
    else:
        print("No repositories found or API request failed.")
