# Programatically Generate Config files for Gnome Terminator

A collection of scripts to open multiple splits in the terminator
with specified commands in each of the splits.

## Scripts

### vertical_n.py

```
python util_vertical_n.py --commands 'ls a' 'ls b' 'ls c' > /tmp/config ; terminator -g /tmp/config
```

![](pics/vertical_n.png)


### horizontal_n.py

```
python util_horizontal_n.py --commands 'ls a' 'ls b' 'ls c' > /tmp/config ; terminator -g /tmp/config
```

![](pics/horizontal_n.png)

### grid_nxm.py
todo

## TODO
Use arg_parse to make all ready scripts more user friendly.

PR welcome!

## Contributors
Manohar Kuse <mpkuse@connect.ust.hk> <https://github.com/mpkuse/>
