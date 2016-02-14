import os
from setuptools import setup


version = "v0.0.1-alpha"
url = "https://github.com/TadLeonard/bewth"
download = "{}/archive/{}.tar.gz".format(url, version)
long_description= """A photo booth for use with the Toshiba FlashAir
wireless SD card. See {} for documentation""".format(url)
description = "A photo booth for use with the Toshiba FlashAir wireless SD card"

classifiers = [
  'Intended Audience :: End Users/Desktop',
  'Operating System :: OS Independent',
  'Programming Language :: Python :: 3',
  'Programming Language :: Python :: 3 :: Only',
]

setup(name="bewth",
      version=version,
      packages=["bewthware"],
      scripts=["bewth"],
      licence="MIT",
      description=description,
      long_description=long_description,
      classifiers=classifiers,
      include_package_data=True,
      package_data={"": ["README.md"]},
      author="Tad Leonard",
      author_email="tadfleonard@gmail.com",
      keywords="photo booth photobooth toshiba flashair wireless sd card",
      url=url,
      download_url=download,
      zip_safe=True,
)

