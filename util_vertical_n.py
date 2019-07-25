# This script can create vertical splits of equal size and custom commands in each terminal
#   ```
#       python vertical_n.py  > config ; cat ./config ; terminator -g ./config
#   ```

# Specify the number of splits
# grid_horizontal = 3 #not in use
# grid_vertical = 4 #the number of verticals u need
#
# # Specify the commands for each, we will echo the command and then execute it
# cmd_list = {}
# cmd_list[0] = "ls /"
# cmd_list[1] = "ls /home"
# cmd_list[2] = "ls /"
# cmd_list[3] = "ls /"

import argparse

parser = argparse.ArgumentParser(description='Generate gnome-terminator config file')
parser.add_argument('--commands', metavar='N', type=str, nargs='+',
                    help='an integer for the accumulator')


args = parser.parse_args()
print args.commands

grid_vertical = len( args.commands )

cmd_list = {}
for i, xcmd in enumerate(args.commands):
    cmd_list[i] = xcmd


# global
print '[global_config]'
print '[keybindings]'


# layouts
print '[layouts]'
print "[[default]]"

# -- window
print "[[[window0]]]"
print "parent = \"\""
print "type = Window"


# we need `grid_vertical`-1 VPaned
for i in range(grid_vertical-1):
    if i == 0:
        parent = "window0"
    else:
        parent = "vsplit%d" %(i-1)

    if i == grid_vertical-2:
        ratio = 0.5
    else:
        ratio = 1.0/ float(grid_vertical - i)

    print '''[[[vsplit%d]]]
          parent = %s
          ratio = %f
          type = VPaned
    ''' %(i, parent, ratio )


# need to assign terminals for each of these
for i in range(grid_vertical):
    # cmd = "custom_command%d" %(i)
    if i not in cmd_list.keys():
        print 'ERROR:::::::::::::::::::::: cannot find cmd#%d in cmd_list. make sure you specify command for each of the request %d terminals' %(i, grid_vertical)
        print 'currently specified keys: ', cmd_list.keys()

    # cmd = cmd_list[i]
    cmd = 'echo "==== %s ===="; %s; bash' %( cmd_list[i] , cmd_list[i] )
    if i==0:
        parent = "vsplit%d" %(grid_vertical-2)
    else:
        parent = "vsplit%d" %(i-1)


    print '''[[[terminal%d]]]
        command = \'\'\' %s \'\'\'
        order = %d
        parent = %s
        profile = default
        type = Terminal
    ''' %(i, cmd, i, parent )
    continue
