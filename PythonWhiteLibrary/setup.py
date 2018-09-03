import distutils.sysconfig
from distutils.core import setup
from distutils.extension import Extension
setup(name         = 'robotframework-whitelibrary',
      version      = '0.0.19',
      description  = 'Windows GUI testing library for Robot Framework',
      author       = 'SALabs',
      author_email = 'to.be.added@noexist89a887.org',
      url          = 'https://github.com/Omenia/robotframework-whitelibrary',
      install_requires     = ['pythonnet'],
      packages     = ['WhiteLibrary'],
      package_dir  = {'WhiteLibrary' : ''},
      package_data = {'WhiteLibrary' : ['bin/CSWhiteLibrary.dll',
                                        'bin/Castle.Core.dll',
                                        'bin/TestStack.White.dll',
                                        'bin/TestStack.White.Reporting.dll',
                                        'bin/TestStack.White.ScreenObjects.dll']},
      )
