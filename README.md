# Pyteryx

An Alteryx REST API Python wrapper for... a reason

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Requirements

Alteryx Server, windows auth etc.

### Prerequisites

Python 3.x. Uses requests_NTLM, etc.

### Installing

Using pip (Not working yet)

```
pip install pyteryx
```

Using git 
```
git clone something
```

### How to use 

Import the Pyteryx Object
```
from pyteryx import Pyteryx

```
Initialise the Pyteryx Object
```
px = Pyteryx("http(s)://domain-servername1", "username", "password")

```
Listing workflows
```
px.get_all_collection_workflows()
px.get_all_private_workflows()

```

## Authors

* **Cameron Barber**  - *Initial work* - [PwC](https://github.com/camzbarber)
* **Jack Marsh**      - *Initial work* - [HI](https://github.com/jackmarsh)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration = Donald Knuth
* etc
