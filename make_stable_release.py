from robot.libdoc import libdoc
from src.WhiteLibrary.version import VERSION
import git
import sys

VERSION_FILE = './src/WhiteLibrary/version.py'


def change_stable(from_stable, to_stable):
    with open(VERSION_FILE, 'r') as file:
        filedata = file.read()

    filedata = filedata.replace('STABLE = {0}'.format(from_stable), 'STABLE = {0}'.format(to_stable))

    with open(VERSION_FILE, 'w') as file:
        file.write(filedata)


def change_version_number(ver):
    with open(VERSION_FILE, 'r') as file:
        filedata = file.read()

    filedata = filedata.replace('VERSION = "{0}"'.format(VERSION), 'VERSION = "{0}"'.format(ver))

    with open(VERSION_FILE, 'w') as file:
        file.write(filedata)


repo = git.Repo('.')

change_stable("False", "True")
new_version = sys.argv[1]
change_version_number(new_version)
libdoc("./src/WhiteLibrary", "./docs/keywords.html", version=new_version)

ver = "v{}".format(new_version)
repo.git.add(VERSION_FILE)
repo.git.add('./docs/keywords.html')
repo.git.commit(m='Making stable release: {0}'.format(ver))
tag = repo.create_tag(ver, message='New stable version: "{0}"'.format(ver))
repo.remotes.origin.push(tag)
repo.git.push()

change_stable("True", "False")

repo.git.add(VERSION_FILE)
repo.git.commit(m='Back to unstable release')
repo.git.push()
