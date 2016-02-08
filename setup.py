import os
from setuptools import setup


__version__ = "v0.0.1-alpha"


version = tfatool._version.__version__
url = "https://github.com/TadLeonard/bewth"
download = "{}/archive/{}.tar.gz".format(url, version)

# NOTE: pandoc doesn't convert Markdown's in-word-emphasis,
# so I have to upload a different hand-tuned README to PyPI
# PyPI might also just be terrible at rendering RST 

#try:
#    import pypandoc
#    long_description = pypandoc.convert('README.md', 'rst')
#except ImportError:
#    long_description = ("Tools for syncing files with the Toshiba FlashAir "
#                        "wireless SD card")

long_description= "See {} for documentation".format(url)
description = "A photo booth"

classifiers = [
  'Intended Audience :: End Users/Desktop',
  'Operating System :: OS Independent',
  'Programming Language :: Python :: 3',
  'Programming Language :: Python :: 3 :: Only',
]

setup(name="bewth",
      version=tfatool._version.__version__,
      scripts=["bewth"],
      licence="MIT",
      description=description,
      long_description=long_description,
      classifiers=classifiers,
      include_package_data=True,
      package_data={"": ["README.md"]},
      author="Tad Leonard",
      author_email="tadfleonard@gmail.com",
      keywords="photo booth photobooth", 
      url=url,
      download_url=download,
      zip_safe=True,
)

