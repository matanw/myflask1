# OCI Migration-Agent Repository

Migration-Agent is a VM migration service agent that will be installed in the user's datacenter as a service. It will expose a web REST interface for the CLI and UI and will be responsible for integrating with local VM repositories (e.g. ESX, vCenter, Folder) and manage VM upload processes  to OCI triggered by the user.

### Prerequisites

These packages should to be installed:

```
python3.6
python3-pip
```

On Mac you can install it using brew:
```
brew install python3
```


### Installing (for development environment)

Clone this repository
```
git clone <url>/migration_agent.git
cd migration_agent
```


### Setup environment

```
make venv
```

make will set up the virtual environment, but if you wish to run the commands
manually, you can do that by:
```
python3 -m venv venv
source venv/bin/activate
pip install -e .[test]
pip install -e .
```
venv will be your virtual environment.

### Run tests

```
make test
```

### Run server

```
make run
```
