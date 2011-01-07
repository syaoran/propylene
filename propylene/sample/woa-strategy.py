# This is the strategy described in the woa-2010 paper

(+~go()) >> 
    [   
        detect_configuration(), 
        +~grab_corn("c0"), 
        +~grab_corn("c3"),
        +~grab_corn("c6"), 
        +~deposit_corns()
    ]


(+~grab_corn(_("X")) | ( white_corn(_("X")) )) >>   
    [ 
        reach_corn(_("X")), 
        pick_corn() 
    ]


(+~grab_corn(_("X")) | ( black_corn(_("X")) )) >> [  ]


(+~deposit_corns() | ( corns_in_robot(_("X")) & (lambda : X > 1)) ) >>
    [
        reach_deposit_zone(), 
        open_tank(), 
        +~deposit_corns() 
    ]


(+~deposit_corns() | ( corns_in_robot(_("X")) & (lambda : X <= 1) & no_more_corns() )) >>
    [ 
        # second part of the game ... 
    ]


(+~deposit_corns() | ( corns_in_robot(_("X")) & (lambda : X <= 1)) ) >>
    [   +~grab_corn("c11"), 
        +~grab_corn("c12"),
        +~grab_corn("c13"), 
        +no_more_corns(), 
        +~deposit_corns() 
    ]

