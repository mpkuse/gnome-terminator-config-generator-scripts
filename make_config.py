grid_horizontal = 3
grid_vertical = 3

# global
print '[global_config]'
print '[keybindings]'


# layouts
print '[layouts]'
print "[[default]]"

if False:
    print '''
        [[[child0]]]
          fullscreen = False
          last_active_term = 747c46ed-f5e3-4d35-adb3-58a984d90337
          last_active_window = True
          maximised = False
          order = 0
          parent = ""
          position = 461:145
          size = 1130, 723
          title = /bin/bash
          type = Window
        [[[child1]]]
          order = 0
          parent = child0
          position = 685
          ratio = 0.608849557522
          type = HPaned
        [[[terminal2]]]
          order = 0
          parent = child1
          profile = default
          type = Terminal
          uuid = 747c46ed-f5e3-4d35-adb3-58a984d90337
        [[[terminal3]]]
          order = 1
          parent = child1
          profile = default
          type = Terminal
          uuid = d0057554-0f4d-41ff-aa75-2930301d6d1f
    '''
    exit(1)

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


    # 
    # for j in range(grid_horizontal-1):
    #     print '''[[[hsplit%d_of_vsplit%d]]]
    #         parent = vsplit%d
    #         ratio = 0.5
    #         type = HPaned
    #     ''' %( j, i, i )


# need to assign terminals for each of these
if True:
    for i in range(grid_vertical):
        if( i == 0 ): #special handling for first one
            print '''[[[terminal%d]]]
                command = \'\'\'echo "HI-last"; bash\'\'\'
                order = 0
                parent = vsplit%d
                profile = default
                type = Terminal
            ''' %(i, grid_vertical-2)
            continue

        print '''[[[terminal%d]]]
            command = \'\'\'echo "HI"; bash\'\'\'
            order = %d
            parent = vsplit%d
            profile = default
            type = Terminal
        ''' %(i, i, i-1)


# c = 0
# for i in range(grid_vertical):
#     for j in range(grid_horizontal):
#         parent = 'hsplit%d_of_vsplit%d' %(j, i)
#
#         print '''[[[terminal_v%d_h%d]]]
#             command = \'\'\'echo "HI"; bash\'\'\'
#             order = %d
#             parent = %s
#             profile = default
#             type = Terminal
#         ''' %(i, j, c, parent )
#         c += 1




exit(1)
print '''[[[vsplit]]]
      parent = window0
      ratio = 0.7
      type = VPaned
'''

print '''[[[vsplitnew]]]
      parent = vsplit
      ratio = 0.7
      type = VPaned
'''


print '''[[[terminal2]]]
    command = \'\'\'echo "HI"; bash\'\'\'
    order = 0
    parent = vsplit
    profile = default
    type = Terminal
'''

# print '''[[[terminal3]]]
#     command = \'\'\'echo "HI 2"; bash\'\'\'
#     order = 1
#     parent = vsplit
#     type = Terminal
#     profile = default
#
# '''


print '''[[[terminal4]]]
    command = \'\'\'echo "HI 3"; bash\'\'\'
    order = 0
    parent = vsplitnew
    type = Terminal
    profile = default

'''

print '''[[[terminal5]]]
    command = \'\'\'echo "HI 3"; bash\'\'\'
    order = 1
    parent = vsplitnew
    type = Terminal
    profile = default

'''



# print '[plugins]'
