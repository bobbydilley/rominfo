[![Actions Status](https://github.com/bobbydilley/rominfo/workflows/build/badge.svg)](https://github.com/bobbydilley/rominfo/actions)

# SEGA Rom Info Utility

Shows information about various SEGA arcade roms, including:

- Sega Naomi
- Sega Naomi 2
- Sega Chihiro
- Sega Triforce
- Sega Lindbergh

## Usage

Simply pass a file path to the `rominfo` command and you will see all of the information about the rom:

```
$ rominfo FZeroAx.bin 
System:       Triforce
Game ID:      SBGG
Manufacturer: SEGA CORPORATION
Date:         2003-06-28
Name:         F-ZERO AX
```

For Lindbergh pass the file path to the installation ISO:

```
$ rominfo "DVP-0015A - OUTRUN 2 SP SDX.img"
System:       Lindbergh
Game ID:      SBMB
Date:         2007-03-15
Name:         OUTRUN2 SP SDX(A)
```

## Installation

Using pip3, you can install straight from the git repo.

```
$ sudo pip3 install git+https://github.com/bobbydilley/rominfo
```

Alternatively you can download the single python file [here](https://github.com/bobbydilley/rominfo/raw/master/rominfo) and run it using python3:

```
$ python3 rominfo FZeroAx.bin
```
