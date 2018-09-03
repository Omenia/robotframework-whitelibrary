import os
import distutils.sysconfig
from distutils.core import setup
from distutils.extension import Extension

def __path(filename):
    return os.path.join(os.path.dirname(__file__),
                        filename)

build = 0

if os.path.exists(__path('build.info')):
    build = open(__path('build.info')).read().strip()

version= '0.0.dev{}'.format(build)

setup(name         = 'robotframework-whitelibrary',
      version      = version,
      description  = 'Windows GUI testing library for Robot Framework',
      author       = 'SALabs',
      author_email = 'to.be.added@noexist89a887.org',
      url          = 'https://github.com/Omenia/robotframework-whitelibrary',
      install_requires     = ['pythonnet'],
      packages     = ['WhiteLibrary'],
      package_dir  = {'WhiteLibrary' : ''},
      package_data = {'WhiteLibrary' : ['CSWhiteLibrary.dll',
                                        'Castle.Core.dll',
                                        'TestStack.White.dll',
                                        'TestStack.White.Reporting.dll',
                                        'TestStack.White.ScreenObjects.dll']},
      )
