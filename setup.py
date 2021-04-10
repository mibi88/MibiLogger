from setuptools import setup

def longdesc():
	with open("README.md") as readme:
		return readme.read()

setup(name = "MibiLogger", version = "0.03", description = "Create logs easier", long_description = longdesc(), long_description_content_type = "text/markdown", classifiers=["Programming Language :: Python :: 3", "Operating System :: Linux"], python_requires = ">=3.7.9", url = "https://github.com/mibi88/MibiLogger", author = "Mibi88", License = "Unlicense", install_requires = ["colorama"])
