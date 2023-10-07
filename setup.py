from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_atzn/__init__.py
from custom_atzn import __version__ as version

setup(
	name="custom_atzn",
	version=version,
	description="An app to customize",
	author="Gabi",
	author_email="gnb2151@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
