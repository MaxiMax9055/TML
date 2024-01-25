import git
import os
import argparse
import requests
import config.py
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--install', type=int, default=0, help="install")
args = parser.parse_args()
if args.install == 1:
    repo = git.Repo.clone_from(config.repos, config.localrepos)
else:
    f = open('version.txt', 'r')
    response = requests.get(config.verrepos)
    remote_version = response.text.strip()
    if int(f.read()) > int(remote_version):
        repo = git.Repo()
        repo.remotes.origin.pull()


os.system("python3 main.py")
