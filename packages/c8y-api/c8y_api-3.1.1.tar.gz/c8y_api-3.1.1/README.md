
![GitHub](https://img.shields.io/github/license/SoftwareAG/cumulocity-python-api)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/SoftwareAG/cumulocity-python-api)
![GitHub Release Date](https://img.shields.io/github/release-date/SoftwareAG/cumulocity-python-api)
![ReadTheDocs](https://img.shields.io/readthedocs/cumulocity-python-api)

# cumulocity-python-api

This project is a Python client for the Cumulocity REST API to make it easier to develop programs, scripts, device agents or microservices in Python.

See also the [documentation on _Read the Docs_](https://cumulocity-python-api.readthedocs.io/).


## Installation

### Prerequisites

Before installing the module (or any module for that matter) consider creating
a virtual environment for your project. This is generally preferred over 
installing modules and dependencies globally:

```shell
cd <project-root>
python3 -m venv venv
source venv/bin/activate
``` 

### Installation from PyPI

The recommended way is to install the lastest distribution package directly from the Python Package Index (PyPI).
You can either add _c8y_api_ as a dependency to your project using _setup.cfg_, or install it manually:

```shell
pip install c8y_api
```

### Installation using pip

Releases are also archived within the GitHub releases page. The module is released as standard Python wheel (_.whl_ file).
It can be downloaded and installed using pip using the following command:

```shell
pip install <release wheel file>
```

Like installing from PyPI, this will install all necessary dependencies automatically.  For your
reference, the module's dependencies are also listed in file _requirements.txt_.
 
### Manual installation

Alternatively, you can clone the repository. The module sources can be used directly within your Python 3 project.
Simply copy the _c8y_api_ folder to your sources root and install the requirements by running the following command:

```shell
pip3 install -r requirements.txt
```

The _requirements.txt_ file is part of the sources.

If the _c8y_api_ folder is in your sources root folder all imports should
work right away. Alternatively you can add _c8y_api_ to your _PYHTONPATH_:

```shell
export PYTHONPATH=<project-root>/c8y_api; $PYTHONPATH
```

## Licensing

This project is licensed under the Apache 2.0 license - see <https://www.apache.org/licenses/LICENSE-2.0>

______________________

These tools are provided as-is and without warranty or support. They do not constitute part of the Software AG product suite. Users are free to use, fork and modify them, subject to the license agreement. While Software AG welcomes contributions, we cannot guarantee to include every contribution in the master project.

______________________

You can find additional information in the [Software AG TECHcommunity](https://tech.forums.softwareag.com/tag/Cumulocity-IoT). There is also an introductory article ([Getting started with the Cumulocity Python API](https://tech.forums.softwareag.com/t/getting-started-with-the-cumulocity-python-api/264700)) available.

Contact us at [TECHcommunity](mailto:technologycommunity@softwareag.com?subject=Github/SoftwareAG) if you have any questions.

