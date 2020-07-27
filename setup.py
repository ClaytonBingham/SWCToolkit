from distutils.core import setup

DESCRIPTION = "Provides a toolkit to manipulate SWC formatted neural morphologies."
LONG_DESCRIPTION = "Provides tools for spatial manipulation and input/output of SWC formatted neural morphologies."
NAME = "swcToolkit"
AUTHOR = "Clayton Bingham"
AUTHOR_EMAIL = "clayton.bingham@gmail.com"
MAINTAINER = "Clayton Bingham"
MAINTAINER_EMAIL = "clayton.bingham@gmail.com"
LICENSE = 'BSD'
REQUIREMENTS = [
		'numpy',
		'pandas',
		'pickle',
		'copy',
		'scipy',
		]
VERSION = '0.1'

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      download_url=DOWNLOAD_URL,
      license=LICENSE,
      packages=['swcToolkit'],
      install_requires=REQUIREMENTS,
      package_data={}
     )
