# SEGA Rom Identifier

Shows information about various SEGA arcade roms, including:

- Sega Naomi
- Sega Naomi 2
- Sega Chihiro
- Sega Triforce

## Usage

Simply pass a file path to the `romident` command and you will see all of the information about the rom:

```
$ romident FZeroAx.bin 
System:       Triforce
Game ID:      SBGG
Manufacturer: SEGA CORPORATION
Date:         28-06-2003
Name:         F-ZERO AX
```

## Installation

Using pip3, you can install straight form the git repo.

```
$ python -m pip3 install git+https://github.com/bobbydilley/romident
```
