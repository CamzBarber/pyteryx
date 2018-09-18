# Pyteryx

A reverse engineered RESTful Alteryx Server API for Python. It adds the following functionality over their official API:
- Run workflow as user (inherits all your access to data connections and files).
- Run workflows from anywhere (not just your private studio).
- Run without having access to the API credentials (e.g. in a corporate environment).

## Getting Started

### Requirements

- Alteryx Server
- Windows Authentication (NTLM) on Alteryx Server

### Prerequisites

- Python 3
- Requests_NTLM
- Pandas

### Installing

Using pip (Coming soon)

```
$ pip install pyteryx
```

Using git 
```
git clone (coming soon...)
```

### How to use 

Where to get URL, domain etc

Import the Pyteryx Object:
```
>>> from pyteryx import Pyteryx
```
Initialise the Pyteryx Object:
```
>>> px = Pyteryx("http(s)://domain-servername1", "username", "password")
```
Below are examples of the funcitonality of 
the Pyteryx object with their respective outputs:
```
>>> px.get_all_collection_workflows()
output example

>>> px.get_all_private_workflows()
output example

>>> px.get_workflow_info()
output example

>>> px.get_workflow_questions()
output example

>>> px.get_workflow_status()
output example

>>> px.run_workflow_get_result()
output example
```

## Authors

* **Cameron Barber**  - *Initial work* - [CamzBarber](https://github.com/camzbarber)
* **Jack Marsh**      - *Initial work* - [JackMarsh](https://github.com/jackmarsh)

See also the list of [contributors](https://github.com/CamzBarber/Pyteryx/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
