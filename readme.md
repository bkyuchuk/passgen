# Command Line Password Generator

Python command line app to generate random passwords.
It's a very small and simple app inspired by 
[bradtraversy's](https://github.com/bradtraversy) 
[passgen](https://github.com/bradtraversy/passgen) project.


## Usage

Install dependencies:
```
pipenv install
```

Run file:
```
python passgen.py [options]
```

Run tests:
```
python -m unittest test_utils.py
```

## Options

| Short | Long              | Description                     |
| ----- | ----------------- | ------------------------------- |
| -l    | --length <number> | length of password (default: 8) |
| -s    | --save            | save password to passwords.txt  |
| -nn   | --no-numbers      | remove numbers                  |
| -ns   | --no-symbols      | remove symbols                  |
| -h    | --help            | display help for command        |
| -V    | --version         | show the version                |