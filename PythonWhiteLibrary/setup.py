import distutils.sysconfig
from distutils.core import setup
setup(name         = 'robotframework-whitelibrary',
      version      = '0.0.1',
      description  = 'Windows GUI testing library for Robot Framework',
      author       = 'Omenia Ltd',
      author_email = 'ismo.aro@omenia.fi',
      url          = 'https://github.com/Omenia/robotframework-whitelibrary',
      package_dir  = {'' : 'src'},
      py_modules = ['WhiteLibrary'],
      data_files = [(distutils.sysconfig.get_python_lib(), ["../WhiteLibrary/bin/WhiteLibrary.dll"])]
      )