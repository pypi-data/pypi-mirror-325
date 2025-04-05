from setuptools import setup

__version__ = "0.2.2"

with open("README.md", "r") as f:
    description = f.read()

setup(
    # Basic package information.
    name = "mondialrelay_pyt",
    version = __version__,

    # Packaging options.
    include_package_data = True,

    # Package dependencies.
   install_requires = [
        "requests >= 2.32.3",
        "xmltodict >= 0.14.2",
    ], 

    # Metadata for PyPI.
    author = "Aymeric Lecomte, Sebastien Beau, Henri Dewilde",
    author_email = "aymeric.lecomte@akretion.com, sebastien.beau@akretion.com, henri.dewilde@gmail.com",
    license = "GNU AGPL-3",
    url = "http://github.com/Bvr4/mondialrelay_pyt",
    packages=["mondialrelay_pyt"],
    keywords = "mondial relay api client",
    description = "A library to access Mondial Relay Web Service from Python.",
    long_description = description,
    long_description_content_type="text/markdown",
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Internet"
    ]
)
