import os
import distutils.sysconfig
from distutils.core import setup
from distutils.extension import Extension

version_data = {}
with open(os.path.join('src', 'WhiteLibrary', 'version.py')) as f:
    exec(f.read(), version_data)

def __path(filename):
    return os.path.join(os.path.dirname(__file__),
                        filename)

build = 0

if os.path.exists(__path('build.info')):
    build = open(__path('build.info')).read().strip()

if version_data['STABLE']:
    version= '{}'.format(version_data['VERSION'])
else: 
    version= '{}.{}.pre'.format(version_data['VERSION'], build) 

setup(name         = 'robotframework-whitelibrary',
      version      = version,
      description  = 'Windows GUI testing library for Robot Framework',
      author       = 'SALabs',
      author_email = 'to.be.added@noexist89a887.org',
      url          = 'https://github.com/Omenia/robotframework-whitelibrary',
      install_requires = ['pythonnet', 'robotframework'],
      packages     = ['WhiteLibrary', 'WhiteLibrary.keywords', 'WhiteLibrary.keywords.items'],
      package_dir  = {'WhiteLibrary' : 'src\WhiteLibrary'},
      package_data = {'WhiteLibrary' : ['bin\*.dll']},
      classifiers = [Programming Language :: Python :: 2,
                     Programming Language :: Python :: 2.7,
                     Programming Language :: Python :: 3,
                     Programming Language :: Python :: 3.5,
                     Programming Language :: Python :: 3.6],
      )
