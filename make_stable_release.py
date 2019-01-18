from robot.libdoc import libdoc
from src.WhiteLibrary.version import VERSION
import git
import sys

VERSION_FILE = './src/WhiteLibrary/version.py'

def change_stable(from_stable, to_stable):

    with open(VERSION_FILE, 'r') as file :
        filedata = file.read()

    filedata = filedata.replace('STABLE = ' + from_stable, 'STABLE = ' + to_stable)

    with open(VERSION_FILE, 'w') as file:
        file.write(filedata)

def change_version_number(ver):
    with open(VERSION_FILE, 'r') as file :
        filedata = file.read()

    filedata = filedata.replace('VERSION = ' + VERSION, 'VERSION = ' + ver)

    with open(VERSION_FILE, 'w') as file:
        file.write(filedata)

repo = git.Repo( '.' )

change_stable("False", "True")
change_version_number(sys.argv[0])
libdoc("./src/WhiteLibrary", "./docs/keywords.html", version=VERSION)

repo.git.add(VERSION_FILE)
repo.git.add('./docs/keywords.html')
repo.git.commit( m='Making Stable release' )
repo.git.push()

change_stable("True", "False")

repo.git.add(VERSION_FILE)
repo.git.commit( m='Making Unstable release' )
repo.git.push()
