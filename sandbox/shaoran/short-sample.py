(+~go("X",_("X")) | ( prova() )  ) >> 
    [   
        detect_configuration(),
#        +~grab_corn("c0"), 
#        +~grab_corn("c3"),
#        +~grab_corn("c6"), 
        +~deposit_corns()
    ]
#
#
(+~grab_corn(_("X")) | ( white_corn(_("X")) )) >>   
    [ 
#        reach_corn(_("X")), 
#        pick_corn() 
    ]
#
#
(+~grab_corn(_("X")) | ( black_corn(_("X")) )) >> [  ]
(+~grab_corn(3E-2,1,1.0,-1,-1.0,2.34e-10,3.54E21) | ( black_corn(_("X")) )) >> [  ]
#
#
#(+~deposit_corns() | ( corns_in_robot(_("X")) & (lambda : X > 1)) ) >>
#    [
#        reach_deposit_zone(), 
#        open_tank(), 
#        +~deposit_corns() 
#    ]
#
#
#(+~deposit_corns() | ( corns_in_robot(_("X")) & (lambda : X <= 1) & no_more_corns() )) >>
#    [ 
#        # second part of the game ... 
#    ]
#
#
#(+~deposit_corns() | ( corns_in_robot(_("X")) & (lambda : X <= 1)) ) >>
#    [   +~grab_corn("c11"), 
#        +~grab_corn("c12"),
#        +~grab_corn("c13"), 
#        +no_more_corns(), 
#        +~deposit_corns() 
#    ]
#
