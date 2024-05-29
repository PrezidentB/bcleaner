# Requirements
To install Bcleaner's requirements start by cloning the repository : 
`git clone https://github.com/PrezidentB/bcleaner.git`

Then you might want to install python requirements if you don't have them already :
 `pip install -r requirements.txt`
# Installation
To install the service simply run : 
`python3 install.py <*your option here*>`
`install.py` has a help option if you want to check possible options.

```
usage: install.py [-h] [-a] [-c] [-bh] [-ph]

A mini CCleaner by BSI team.

options:
  -h, --help          show this help message and exit
  -a, --apps          Delete all app caches in ~/.cache/
  -c, --cookies       Delete your browser cookies.
  -bh, --bash_hist    Clear up bash_history file.
  -ph, --python_hist  Clear up python_history file (Might not work on all systems).
```
# Usage
Bcleaner installs itself as a service in `~/.config/systemd/user`it's name is `bcleaner.service` 
The service simply run verification script on startup and a cleanup a script when shutting down.
It doesn't need sudo to be run. 
All actions are (*normally*) logged in the log directory (`[...]/bcleaner/logs`) the file is `bcleaner.log`.

For the moment, it only has been tested on :
- a freshly installed debian 12.

# Directories
```.
├── bsi_linux
│   ├── bcleaner
│   │   ├── apps.py
│   │   ├── cookies.py
│   │   ├── history.py
│   │   ├── __init__.py
│   │   ├── run.py
│   │   ├── sudo.py
│   │   └── utils.py
│   ├── install.py
│   ├── main.py
│   ├── pyproject.toml
│   ├── requirements.txt
│   └── verif_main.py
├── LICENSE
└── README.md
```


