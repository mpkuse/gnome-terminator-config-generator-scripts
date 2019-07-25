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

if False: #2x2
    print '''
        [[[child0]]]
          fullscreen = False
          last_active_term = d0057554-0f4d-41ff-aa75-2930301d6d1f
          last_active_window = True
          maximised = False
          order = 0
          parent = ""
          position = 65:87
          size = 1130, 723
          title = /bin/bash
          type = Window
        [[[child1]]]
          order = 0
          parent = child0
          position = 358
          ratio = 0.499308437068
          type = VPaned
        [[[child2]]]
          order = 0
          parent = child1
          position = 562
          ratio = 0.5
          type = HPaned
        [[[child5]]]
          order = 1
          parent = child1
          position = 562
          ratio = 0.5
          type = HPaned
        [[[terminal3]]]
          order = 0
          parent = child2
          profile = default
          type = Terminal
          uuid = d0057554-0f4d-41ff-aa75-2930301d6d1f
        [[[terminal4]]]
          order = 1
          parent = child2
          profile = default
          type = Terminal
          uuid = 42ff2f5f-3263-4358-9238-1157bc9230bc
        [[[terminal6]]]
          order = 0
          parent = child5
          profile = default
          type = Terminal
          uuid = 0b03ffed-ad6c-4ead-b0d1-4de45cba5e90
        [[[terminal7]]]
          order = 1
          parent = child5
          profile = default
          type = Terminal
          uuid = db2a043f-5f2b-4934-b4c7-9a85b96b48a2
         '''

if False: #3x3
    print '''
    [[[child0]]]
      fullscreen = False
      last_active_term = 3b4f11b4-88cd-4d8e-8586-fd9d14539576
      last_active_window = True
      maximised = False
      order = 0
      parent = ""
      position = 128:125
      size = 1130, 723
      title = /bin/bash
      type = Window
    [[[child1]]]
      order = 0
      parent = child0
      position = 358
      ratio = 0.499308437068
      type = VPaned
    [[[child10]]]
      order = 1
      parent = child8
      position = 278
      ratio = 0.5
      type = HPaned
    [[[child13]]]
      order = 1
      parent = child7
      position = 562
      ratio = 0.5
      type = HPaned
    [[[child15]]]
      order = 1
      parent = child13
      position = 278
      ratio = 0.5
      type = HPaned
    [[[child2]]]
      order = 0
      parent = child1
      position = 562
      ratio = 0.5
      type = HPaned
    [[[child4]]]
      order = 1
      parent = child2
      position = 278
      ratio = 0.5
      type = HPaned
    [[[child7]]]
      order = 1
      parent = child1
      position = 176
      ratio = 0.49860724234
      type = VPaned
    [[[child8]]]
      order = 0
      parent = child7
      position = 562
      ratio = 0.5
      type = HPaned
    [[[terminal11]]]
      order = 0
      parent = child10
      profile = default
      type = Terminal
      uuid = 3da0d7b1-ee5b-4ad2-b17a-56a4f7275d55
    [[[terminal12]]]
      order = 1
      parent = child10
      profile = default
      type = Terminal
      uuid = 98775b60-066c-436f-ab66-f40700bd71eb
    [[[terminal14]]]
      order = 0
      parent = child13
      profile = default
      type = Terminal
      uuid = e3634e34-20bc-43c5-8586-f565301f69e5
    [[[terminal16]]]
      order = 0
      parent = child15
      profile = default
      type = Terminal
      uuid = 381b2061-2c3c-453b-be29-7de6d5d1b7b6
    [[[terminal17]]]
      order = 1
      parent = child15
      profile = default
      type = Terminal
      uuid = 6dc0802b-af34-4971-af5d-c7630a5ed205
    [[[terminal3]]]
      order = 0
      parent = child2
      profile = default
      type = Terminal
      uuid = 3b4f11b4-88cd-4d8e-8586-fd9d14539576
    [[[terminal5]]]
      order = 0
      parent = child4
      profile = default
      type = Terminal
      uuid = b3f8ba36-3afc-4b29-a68f-5c2a55468ba7
    [[[terminal6]]]
      order = 1
      parent = child4
      profile = default
      type = Terminal
      uuid = 077d30d2-2460-4eb5-9309-60ab2352615a
    [[[terminal9]]]
      order = 0
      parent = child8
      profile = default
      type = Terminal
      uuid = 750f3806-6862-4e99-bee1-6b1e704894d5
      '''


if False:
    print '''
        [[[child0]]]
          fullscreen = False
          last_active_term = d0057554-0f4d-41ff-aa75-2930301d6d1f
          last_active_window = True
          maximised = False
          order = 0
          parent = ""
          position = 65:87
          size = 1130, 723
          title = /bin/bash
          type = Window
        [[[child1]]]
          order = 0
          parent = child0
          position = 358
          ratio = 0.499308437068
          type = VPaned
        [[[child10]]]
          order = 0
          parent = child9
          position = 562
          ratio = 0.5
          type = HPaned
        [[[child12]]]
          order = 1
          parent = child10
          position = 278
          ratio = 0.5
          type = HPaned
        [[[child14]]]
          order = 1
          parent = child12
          position = 136
          ratio = 0.5
          type = HPaned
        [[[child17]]]
          order = 1
          parent = child9
          position = 85
          ratio = 0.497175141243
          type = VPaned
        [[[child18]]]
          order = 0
          parent = child17
          position = 562
          ratio = 0.5
          type = HPaned
        [[[child2]]]
          order = 0
          parent = child1
          position = 562
          ratio = 0.5
          type = HPaned
        [[[child20]]]
          order = 1
          parent = child18
          position = 278
          ratio = 0.5
          type = HPaned
        [[[child22]]]
          order = 1
          parent = child20
          position = 136
          ratio = 0.5
          type = HPaned
        [[[child25]]]
          order = 1
          parent = child17
          position = 562
          ratio = 0.5
          type = HPaned
        [[[child27]]]
          order = 1
          parent = child25
          position = 278
          ratio = 0.5
          type = HPaned
        [[[child29]]]
          order = 1
          parent = child27
          position = 136
          ratio = 0.5
          type = HPaned
        [[[child4]]]
          order = 1
          parent = child2
          position = 278
          ratio = 0.5
          type = HPaned
        [[[child6]]]
          order = 1
          parent = child4
          position = 136
          ratio = 0.5
          type = HPaned
        [[[child9]]]
          order = 1
          parent = child1
          position = 176
          ratio = 0.49860724234
          type = VPaned
        [[[terminal11]]]
          order = 0
          parent = child10
          profile = default
          type = Terminal
          uuid = d41d08af-ed3a-4a78-941f-efc32f0e7c69
        [[[terminal13]]]
          order = 0
          parent = child12
          profile = default
          type = Terminal
          uuid = 58646a01-1598-4527-bf29-5d260c01939f
        [[[terminal15]]]
          order = 0
          parent = child14
          profile = default
          type = Terminal
          uuid = d23b0a77-463e-4812-a92d-850923a5abf6
        [[[terminal16]]]
          order = 1
          parent = child14
          profile = default
          type = Terminal
          uuid = 25a626b6-db83-4045-9c4a-db59120dcea1
        [[[terminal19]]]
          order = 0
          parent = child18
          profile = default
          type = Terminal
          uuid = 8e68986a-8348-44b9-b329-1bbf6a30f937
        [[[terminal21]]]
          order = 0
          parent = child20
          profile = default
          type = Terminal
          uuid = 6d247222-c090-41da-883c-eecf12b62d86
        [[[terminal23]]]
          order = 0
          parent = child22
          profile = default
          type = Terminal
          uuid = a30fa6eb-2cf5-4478-87b5-842fb067adf9
        [[[terminal24]]]
          order = 1
          parent = child22
          profile = default
          type = Terminal
          uuid = 09e360aa-14e1-4481-98b3-d599a7579699
        [[[terminal26]]]
          order = 0
          parent = child25
          profile = default
          type = Terminal
          uuid = 8aca84ee-9add-4198-b11f-e82d7bb6b532
        [[[terminal28]]]
          order = 0
          parent = child27
          profile = default
          type = Terminal
          uuid = 53257ac8-cc28-452d-9273-ffe6532d6a9f
        [[[terminal3]]]
          order = 0
          parent = child2
          profile = default
          type = Terminal
          uuid = d0057554-0f4d-41ff-aa75-2930301d6d1f
        [[[terminal30]]]
          order = 0
          parent = child29
          profile = default
          type = Terminal
          uuid = 2773a40c-dcef-421f-9967-0c308a036129
        [[[terminal31]]]
          order = 1
          parent = child29
          profile = default
          type = Terminal
          uuid = b347a32a-cc7f-4182-8c76-bfb5dba49939
        [[[terminal5]]]
          order = 0
          parent = child4
          profile = default
          type = Terminal
          uuid = f9a208d7-4ced-4a8c-9d17-699b673da541
        [[[terminal7]]]
          order = 0
          parent = child6
          profile = default
          type = Terminal
          uuid = e1cb777a-1718-4d51-bdd8-764b1f90659e
        [[[terminal8]]]
          order = 1
          parent = child6
          profile = default
          type = Terminal
          uuid = 10e99a33-6974-4487-a70f-95b8ffcef95b
        '''
    exit(1)

#---------------------------------------------------------------------------#

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


    e = grid_horizontal
    for j in range(e):
        if j==0:
            hparent = 'vsplit%d' %(i)
        else:
            hparent = 'h%d_v%d' %(j-1,i)
        # hparent = 'vsplit%d' %(i)


        print '''[[[h%d_v%d]]]
            parent = %s
            ratio = 0.5
            type = HPaned
        ''' %(j, i, hparent )

exit(1)


# terminals
for j in range(grid_horizontal):
    for i in range(grid_vertical):
        if i == grid_vertical-1:
            parent = "hsplit%d_of_vsplit%d" %( j, 0 )
        else:
            parent = "hsplit%d_of_vsplit%d" %( j, i )


        print '''[[[terminal%d]]]
            command = \'\'\' echo hi ; bash\'\'\'
            order = %d
            parent = %s
            profile = default
            type = Terminal
            ''' %( i*grid_vertical + j, i, parent )
