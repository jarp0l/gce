# gce (git-commit-emails)
> Extract author emails from git repo commits

Automate extracting author emails from git repo commits. Wrote this to help me in my own OSINT investigation.

---

- Still under development
- Works only with GitHub repos using GitHub API

---

Usage:
```bash
./gce.py -h
usage: gce.py [-h] -u USERNAME [-r REPO]

Extract author emails from git repo

options:
  -h, --help            show this help message and exit
  -u USERNAME, --user USERNAME
                        Specify the username
  -r REPO, --repo REPO  Specify the repo
```


Extract emails from every repo of a user:
```bash
./gce.py -u USERNAME
# or
./gce.py --user USERNAME
```

Extract emails from a repo of the user:
```bash
./gce.py -u USERNAME -r REPO
# or
./gce.py --user USERNAME --repo REPO
```

## Dependencies
- `httpx`: For HTTP requests
- `argparse`: To parse CLI args
- `black`: For code formatting