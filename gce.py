#!/bin/env python3
import httpx
from string import Template
from argparse import ArgumentParser

user_uri = Template("https://api.github.com/users/$username/repos")
commits_uri = Template("https://api.github.com/repos/$username/$repo/commits")


def make_request(uri):
    response = httpx.get(uri)
    if response.status_code == 200:
        return response.json()
    print("Error in making request!")
    exit(0)


def get_repos(**kwargs) -> list:
    username = kwargs["username"]

    target = user_uri.substitute({"username": username})
    response = make_request(target)
    repos = [repo["name"] for repo in response]
    return repos


def get_commits(**kwargs) -> list:
    username = kwargs["username"]
    repo_name = kwargs["repo_name"]

    target = commits_uri.substitute({"username": username, "repo": repo_name})
    response = make_request(target)
    commits = response
    return commits


def parse_commits(**kwargs) -> tuple:
    commits = kwargs["commits"]

    commit_info = [
        {
            "name": commit["commit"]["author"]["name"],
            "email": commit["commit"]["author"]["email"],
        }
        for commit in commits
    ]

    commit_info = [dict(t) for t in {tuple(i.items()) for i in commit_info}]
    return commit_info


def main():
    repos = list()
    commits = list()

    parser = ArgumentParser(description="Extract author emails from git repo")
    parser.add_argument(
        "-u",
        "--user",
        dest="username",
        type=str,
        required=True,
        help="Specify the username",
    )

    parser.add_argument(
        "-r",
        "--repo",
        type=str,
        help="Specify the repo",
    )

    args = parser.parse_args()

    if args.username and args.repo is None:
        username = args.username
        repos = get_repos(username=username)
        for repo in repos:
            repo_commits = get_commits(username=username, repo_name=repo)
            print(parse_commits(commits=repo_commits))

    if args.repo:
        username = args.username
        repo = args.repo
        repo_commits = get_commits(username=username, repo_name=repo)
        print(parse_commits(commits=repo_commits))


if __name__ == "__main__":
    main()
