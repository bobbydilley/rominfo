import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name='rominfo',  
	version='0.3',
	scripts=['rominfo'] ,
	author="Bobby Dilley",
	author_email="bobby@dilley.uk",
	description="A command line utility to read SEGA arcade rom info",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/bobbydilley/rominfo",
	packages=setuptools.find_packages(),
)
