import distutils.sysconfig
from distutils.core import setup
setup(name         = 'robotframework-whitelibrary',
      version      = '0.0.2',
      description  = 'Windows GUI testing library for Robot Framework',
      author       = 'SALabs',
      author_email = 'to.be.added@noexist89a887.org',
      url          = 'https://github.com/Omenia/robotframework-whitelibrary',
      package_dir  = {'' : 'src'},
      py_modules   = ['WhiteLibrary'],
      package_data = {'robotframework-whitelibrary': ["WhiteLibrary/bin/CSWhiteLibrary.dll"]},
      )
