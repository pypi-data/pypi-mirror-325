import requests
import subprocess
import os

token = os.environ.get("CODEBERG_TOKEN")

owner = "bovine"
repo = "cattle_grid"

repo_base_url = f"https://codeberg.org/api/v1/repos/{owner}/{repo}"
milestone_url = f"{repo_base_url}/milestones"
release_url = f"{repo_base_url}/releases"

if not token:
    raise ValueError("CODEBERG_TOKEN not set")

print(f"Repo base url: {repo_base_url}")


def determine_version():
    result = subprocess.run(["hatch", "version"], capture_output=True)
    return result.stdout.decode().strip()


def get_milestone_information(milestone: str):
    response = requests.get(
        f"{milestone_url}?state=open", headers={"Authorization": f"Bearer {token}"}
    )

    data = response.json()

    for x in data:
        if x.get("title") == milestone:
            return x

    raise ValueError("Milestone not found")


def close_milestone(milestone: str):
    info = get_milestone_information(milestone)

    if info.get("open_issues") > 0:
        raise ValueError("Milestone has open issues")

    milestone_id = info.get("id")

    requests.patch(
        f"{milestone_url}/{milestone_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={"state": "closed"},
    )

    print("milestone closed")


def create_release(milestone: str):
    response = requests.post(
        release_url,
        headers={"Authorization": f"Bearer {token}"},
        json={"tag_name": milestone, "name": milestone},
    )

    print(response)
    print(response.text)

    print("Created release")


milestone = determine_version()

print(f"Running for milestone {milestone}")

close_milestone(milestone)
create_release(milestone)
