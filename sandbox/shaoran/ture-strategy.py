        (+grab_corn("c0") | ( black_corn("c0") )) >> [ +grab_corn("c3") ]

        (+white_corn_got() | ( for_corn("c0"))) >> [ -target_got(),
                                                     forward(-150),
                                                     wait_target(),
                                                     increase_corn(),
                                                     -white_corn_got(),
                                                     -for_corn("c0"),
                                                     +grab_corn("c3") ]

      (+white_corn_got(_("X"),_("Y"))  | ( for_corn(_("Z")) & (lambda W: (X<"ciao") and (Y==io) or (Z<34) and (W>21) )   )) >> [ -target_got(),
                                                     forward(-150),
                                                     wait_target(),
                                                     increase_corn(),
                                                     -white_corn_got(),
                                                     -for_corn("c0"),
                                                     +grab_corn("c3") ]

       (+target_got() | (for_corn("c0")) ) >> [ -target_got(),
                                                 forward(-150),
                                                 wait_target(),
                                                 -white_corn_got(),
                                                 -for_corn("c0"),
                                                 +grab_corn("c3") ]

#        (+grab_corn("c3") | ( black_corn("c3") )) >> [ do_path(["a0", "a1"]),
#                                                       +take_tomatoes() ]

        (+white_corn_got() | ( for_corn("c3"))) >> [ -target_got(),
                                                     increase_corn(),
                                                     -white_corn_got(),
                                                     -for_corn("c3"),
                                                     prepare_ball_picking(),
#                                                     do_path(["t2"]),
                                                     +take_tomatoes() ]

        (+target_got() | ( for_corn("c3"))) >> [ -target_got(),
                                                 -white_corn_got(),
                                                 -for_corn("c3"),
                                                 prepare_ball_picking(),
                                                 #do_path(["t2"]),
                                                 +take_tomatoes() ]
        (+target_got() | (for_tomato(_("T")) & (lambda : (T == "f0") 
        or (T == "f3") or (T == "t6") or (T == "t8") or (T == "a19") or (T == "a21") )
        )) >>
         [ show(_("T")),
           -target_got(),
           -for_tomato(_("T")),
           +for_tomato("a23"),
           activate_ball_picking(),
           activate_opponent_detector(),
           forward(-30),
           do_ball_path("a23") ]
#
#        # we have balls, and we have time to take more corns :-)))
#        (+are_more_corns_worth() | (balls_in_robot(_("X")) & (lambda : X > 0) &
#         elapsed_timer(_("T")) & (lambda : T <= 60)) ) >> [ deploy_carriage(),
#                                                    +prepare_to_grab_corn("a23", "c17") ]
#
#
#
#
#
#
#
##        # ----------------------------------------------------------------------------------
#        (+take_tomatoes()) >> [ retract_belief (take_tomatoes()),
#                                prepare_ball_picking(),
#                                activate_ball_picking(),
#                                do_ball_path("t7"),
#                                activate_opponent_detector(),
#                                assert_belief(for_tomato("t7")) ]
#
#        # ----------------------------------------------------------------------------------
#        (+take_tomatoes_no_prepare()) >> [ retract_belief (take_tomatoes_no_prepare()),
#                                           activate_ball_picking(),
#                                           do_ball_path("t7"),
#                                           activate_opponent_detector(),
#                                           assert_belief(for_tomato("t7")) ]
#
#        # ----------------------------------------------------------------------------------
#        (+ball_got() | for_tomato(_("T")) ) >> [ retract_belief (ball_got()),
#                                                 retract_belief (target_got()),
#                                                 increase_balls(),
#                                                 activate_ball_picking(),
#                                                 activate_opponent_detector(),
#                                                 do_ball_path(_("T")) ]
#
#        # ----------------------------------------------------------------------------------
#        (+opponent_got() | for_tomato(_("T")) ) >> [ -opponent_got(), wait_opponent_over() ]
#        (+opponent_over() | for_tomato(_("T")) ) >> [ -opponent_over(),
#                                                      activate_opponent_detector(),
#                                                      activate_ball_picking(),
#                                                      do_ball_path(_("T")) ]
#        #(+opponent_still_on_the_way() | for_tomato(_("T")) ) >> [ -opponent_still_on_the_way(),
#        #                                                          show("UUUUAAAAHHHHHHHHHH!!!!!!!!!!!") ]
#        (+opponent_still_on_the_way() | for_tomato(_("T")) ) >> [ -opponent_still_on_the_way(),
#                                                                  -for_tomato(_("T")),
#                                                                  change_ball_diagonal(_("T"), "right"),
#                                                                  activate_ball_picking () ]
#
#
#        # ----------------------------------------------------------------------------------
#        (+element_reached(_("T")) | for_tomato(_("T")) ) >> [ +target_got() ]
#        # ----------------------------------------------------------------------------------
#        # Diagonal f0 - f3 - t6 - t8 ---> a23
#        # Vertical a19 - a21 ---> a23
#        # ----------------------------------------------------------------------------------
#        (+target_got() | \
#         (for_tomato(_("T")) & (lambda : (T == "f0") or (T == "f3") or (T == "t6") or (T == "t8") or (T == "a19") or (T == "a21") ))) >> \
#         [ show(_("T")),
#           retract_belief (target_got()),
#           retract_belief (for_tomato(_("T"))),
#           assert_belief (for_tomato("a23")),
#           activate_ball_picking(),
#           activate_opponent_detector(),
#           forward(-30),
#           do_ball_path("a23") ]
#
#        # ----------------------------------------------------------------------------------
#        # Diagonal t7 ---> t8
#        # ----------------------------------------------------------------------------------
#        (+target_got() | (for_tomato(_("T")) & (lambda : (T == "t7")  ) )) >> \
#                       [ show("ON t7"),
#                         retract_belief (target_got()),
#                         retract_belief (for_tomato(_("T"))),
#                         assert_belief (for_tomato("t8")),
#                         activate_ball_picking(),
#                         activate_opponent_detector(),
#                         do_ball_path("t8") ]
#
#
#        # ----------------------------------------------------------------------------------
#        # Diagonal t2 ---> f3
#        # ----------------------------------------------------------------------------------
#        (+target_got() | (for_tomato(_("T")) & (lambda : (T == "t2")  ) )) >> \
#                       [ show("ON t2"),
#                         retract_belief (target_got()),
#                         retract_belief (for_tomato(_("T"))),
#                         assert_belief (for_tomato("f3")),
#                         activate_ball_picking(),
#                         activate_opponent_detector(),
#                         do_ball_path("f3") ]
#
#
#        # ----------------------------------------------------------------------------------
#        # Diagonal t4 ---> t6
#        # ----------------------------------------------------------------------------------
#        (+target_got() | (for_tomato(_("T")) & (lambda : (T == "t4")  ) )) >> \
#                                                             [ show(_("T")),
#                                                               retract_belief (target_got()),
#                                                               retract_belief (for_tomato(_("T"))),
#                                                               assert_belief (for_tomato("t6")),
#                                                               activate_ball_picking(),
#                                                               activate_opponent_detector(),
#                                                               do_ball_path("t6") ]
#
#
#        # ----------------------------------------------------------------------------------
#        # Diagonal f6 - f11 ---> a21
#        # ----------------------------------------------------------------------------------
#        (+target_got() | (for_tomato(_("T")) & (lambda : (T == "f6") or (T == "f11") or (T == "f8")) )) >> \
#                                                             [ show(_("T")),
#                                                               retract_belief (target_got()),
#                                                               retract_belief (for_tomato(_("T"))),
#                                                               assert_belief (for_tomato("a21")),
#                                                               activate_ball_picking(),
#                                                               activate_opponent_detector(),
#                                                               do_ball_path("a21") ]
#
#
#        # ----------------------------------------------------------------------------------
#        # Diagonal f13 ---> a19
#        # ----------------------------------------------------------------------------------
#        (+target_got() | (for_tomato(_("T")) & (lambda : (T == "f13") ) )) >> \
#                                                             [ show(_("T")),
#                                                               retract_belief (target_got()),
#                                                               retract_belief (for_tomato(_("T"))),
#                                                               assert_belief (for_tomato("a19")),
#                                                               activate_ball_picking(),
#                                                               activate_opponent_detector(),
#                                                               do_ball_path("a19") ]
#
#
#        # ----------------------------------------------------------------------------------
#        # Diagonal t10 ---> a21
#        # ----------------------------------------------------------------------------------
#        (+target_got() | (for_tomato(_("T")) & (lambda : (T == "t10") ) )) >> \
#                                                             [ show(_("T")),
#                                                               retract_belief (target_got()),
#                                                               retract_belief (for_tomato(_("T"))),
#                                                               assert_belief (for_tomato("a21")),
#                                                               activate_ball_picking(),
#                                                               activate_opponent_detector(),
#                                                               do_ball_path("a21") ]
#
#
#        # ----------------------------------------------------------------------------------
#        (+element_reached("a23") | for_tomato("a23") ) >> [ target_poller_off(),
#                                                            retract_belief (target_got()),
#                                                            retract_belief (for_tomato("a23")),
#                                                            show("Got some objects"),
#                                                            +first_episode_over () ]
#
#        (+target_got() | for_tomato("a23") ) >> [ retract_belief (target_got()),
#                                                  retract_belief (for_tomato("a23")),
#                                                  target_poller_off(),
#                                                  show("Got some objects"),
#                                                  +first_episode_over () ]
#
#        # ----------------------------------------------------------------------------------
#        (+first_episode_over() | (homologation("no") & corns_in_robot(_("X")) & (lambda : X <= 1) )) >> [ deposit_corns(),
#                                                                                                          forward(-110),
#                                                                                                          wait_target(),
#                                                                                                          freeze_timer(),
#                                                                                                          +are_more_corns_worth() ]
#
#                                                                                                          #[ end_ball_picking(),
#                                                                                                          #forward(-50),
#                                                                                                          #reach_point_back ("t11"),
#                                                                                                          #+second_episode_over() ]
#                                                                                                          #forward(-110),
#                                                                                                          #deploy_carriage(),
#                                                                                                          #+prepare_to_grab_corn("a23", "c17") ]
#
#        (+first_episode_over() | (homologation("yes") )) >> [ end_ball_picking(),
#                                                              forward(-50),
#                                                              reach_point_back ("t11"),
#                                                              +second_episode_over() ]
#
#        (+first_episode_over() | (corns_in_robot(_("X")) & (lambda : X > 1))) >> [ deposit_corns(),
#                                                                                   forward(-110),
#                                                                                   wait_target(),
#                                                                                   freeze_timer(),
#                                                                                   +are_more_corns_worth() ]
#                                                                                   #deploy_carriage(),
#                                                                                   #+prepare_to_grab_corn("a23", "c17") ]
#
#        # ----------------------------------------------------------------------------------
#        # we have no balls... :-( OK, it's worth to take more corns
#        #(+are_more_corns_worth() | balls_in_robot(0) ) >> [ deploy_carriage(),
#        #                                                    +prepare_to_grab_corn("a23", "c17") ]
#
#        # we have balls, and we have time to take more corns :-)))
#        #(+are_more_corns_worth() | (balls_in_robot(_("X")) & (lambda : X > 0) &
#        # elapsed_timer(_("T")) & (lambda : T <= 60)) ) >> [ deploy_carriage(),
#        #                                            +prepare_to_grab_corn("a23", "c17") ]
#
#        # we have balls, but we have no time to take more corns :-)
#        #(+are_more_corns_worth() | (balls_in_robot(_("X")) & (lambda : X > 0) &
#        # elapsed_timer(_("T")) & (lambda : T > 60)) ) >> [ reach_point_back ("t11"),
#        #                                                   +second_episode_over() ]
#
#        (+are_more_corns_worth()  ) >> [ reach_point_back ("t11"), +second_episode_over() ]
#
#
#        # ----------------------------------------------------------------------------------
#        (+second_episode_over() | (corns_in_robot(_("X")) & (lambda : X > 0) ) ) >> [ retract_carriage(),
#                                                                                      reach_point("a23"),
#                                                                                      deposit_corns(),
#                                                                                      forward(-110),
#                                                                                      wait_target(),
#                                                                                      reach_point_back ("t11"),
#                                                                                      reach_point ("a22"),
#                                                                                      heading_to (-90),
#                                                                                      forward (-110),
#                                                                                      heading_to (-100),
#                                                                                      forward(-80),
#                                                                                      show("Waiting for discharge"),
#                                                                                      wait_target(),
#                                                                                      show("Starting discharge"),
#                                                                                      deposit_tomatoes() ]
#
#        # ----------------------------------------------------------------------------------
#        (+second_episode_over() | (corns_in_robot (0)) ) >> [ reach_point ("a22"),
#                                                              heading_to (-90),
#                                                              forward (-110),
#                                                              heading_to (-100),
#                                                              forward(-80),
#                                                              show("Waiting for discharge"),
#                                                              wait_target(),
#                                                              show("Starting discharge"),
#                                                              deposit_tomatoes() ]
#
#        # ----------------------------------------------------------------------------------
#
#        ( +prepare_to_grab_corn ("a23", "c17") | (white_corn ("c17")))  >> [ retract_belief (prepare_to_grab_corn ("a23", "c17")),
#                                                                             do_path_back (["t11"]),
#                                                                             orientate_towards ("c17"),
#                                                                             #wait_target(),
#                                                                             assert_belief (for_corn("c17")),
#                                                                             reach_corn ("c17") ]
#
#        # ----------------------------------------------------------------------------------
#        ( +prepare_to_grab_corn ("a23", "c17") | (black_corn ("c17")))  >> [ retract_belief (prepare_to_grab_corn ("a23", "c17")),
#                                                                             reach_point_back ("t11"),
#                                                                             +second_episode_over() ]
#
#        # ----------------------------------------------------------------------------------
#        ( +grab_corn(_("C")) | (white_corn(_("C"))) ) >>  [ +for_corn(_("C")), reach_corn(_("C")) ]
#
#        # ----------------------------------------------------------------------------------
#        ( +white_corn_got() | (for_corn("c17")  ) )   >>  [ increase_corn(),
#                                                            retract_belief (white_corn_got()),
#                                                            retract_belief (for_corn("c17")),
#                                                            retract_carriage(),
#                                                            forward(-100),
#                                                            reach_point("a23"),
#                                                            deposit_corns(),
#                                                            forward(-110),
#                                                            reach_point_back ("t11"),
#                                                            +second_episode_over() ]
#
#        (+target_got() | (for_corn("c17") & (corns_in_robot(0)) ) )>> [ retract_belief (target_got()),
#                                                                        retract_belief (for_corn("c17")),
#                                                                        forward(-120),
#                                                                        +second_episode_over() ]
#
#        (+target_got() | (for_corn("c17") & (corns_in_robot(_("X"))) & (lambda : X > 0)) ) >> [ retract_belief (target_got()),
#                                                                                                retract_belief (for_corn("c17")),
#                                                                                                retract_carriage(),
#                                                                                                forward(-100),
#                                                                                                reach_point("a23"),
#                                                                                                deposit_corns(),
#                                                                                                forward(-110),
#                                                                                                reach_point_back ("t11"),
#                                                                                                +second_episode_over() ]
#
#        # ----------------------------------------------------------------------------------
#
#    else:
#        # BLUE STRATEGY
#        ( +~go() ) >>   [ forward(215),
#                          orientate_towards("c14"),
#                          wait_target(),
#                          second_pass_detection(),
#                          +select_next_strategy() ]
#
#        # ----------------------------------------------------------------------------------
#        (+select_next_strategy() | take_corns_first() ) >> [ deploy_carriage_first_time(),
#                                                             +grab_corn("c15") ]
#
#        (+select_next_strategy() | take_tomatoes_first() ) >> [ retract_carriage_first_time(),
#                                                                orientate_towards("c12"),
#                                                                forward(100),
#                                                                do_path(["a19", "a20"]),
#                                                                prepare_ball_picking(),
#                                                                wait_target(),
#                                                                activate_ball_picking(),
#                                                                do_ball_path("t7"),
#                                                                activate_opponent_detector(),
#                                                                assert_belief(for_tomato("t7")) ]
#
#        # ----------------------------------------------------------------------------------
#        # CORN C15
#        #(+grab_corn("c15") | ( white_corn("c15") )) >> [ assert_belief(for_corn("c15")),
#        #                                                 reach_corn("c15") ]
#        (+grab_corn("c15") | ( black_corn("c15") )) >> [ +grab_corn("c12") ]
#
#        (+white_corn_got() | ( for_corn("c15"))) >> [ retract_belief (target_got()),
#                                                      forward(-200),
#                                                      wait_target(),
#                                                      increase_corn(),
#                                                      retract_belief (white_corn_got()),
#                                                      retract_belief (for_corn("c15")),
#                                                      +grab_corn("c12") ]
#
#        (+target_got() | (for_corn("c15")) ) >> [ retract_belief (target_got()),
#                                                  forward(-200),
#                                                  wait_target(),
#                                                  retract_belief (white_corn_got()),
#                                                  retract_belief (for_corn("c15")),
#                                                  +grab_corn("c12") ]
#
#        # ----------------------------------------------------------------------------------
#        # CORN C12
#        #(+grab_corn("c12") | ( white_corn("c12") )) >> [ assert_belief (for_corn("c12")),
#        #                                                 reach_corn("c12") ]
#        (+grab_corn("c12") | ( black_corn("c12") & corns_in_robot(0) )) >> [ show("BLACK 1"),
#                                                                             orientate_towards("c12"),
#                                                                             forward(100),
#                                                                             do_path(["a19", "a20"]),
#                                                                             +take_tomatoes() ]
#        (+grab_corn("c12") | ( black_corn("c12") & corns_in_robot(_("X")) & (lambda :X > 0) )) >> [ show("BLACK 2"),
#                                                                                                    do_path(["a19", "a20"]),
#                                                                                                    +take_tomatoes() ]
#
#        (+white_corn_got() | ( for_corn("c12"))) >> [ show("HERE GOT"),
#                                                      retract_belief (target_got()),
#                                                      increase_corn(),
#                                                      retract_belief (white_corn_got()),
#                                                      retract_belief (for_corn("c12")),
#                                                      prepare_ball_picking(),
#                                                      do_path(["t10"]),
#                                                      #wait_target(),
#                                                     +take_tomatoes() ]
#        (+target_got() | ( for_corn("c12"))) >> [ show("TARGET GOT"),
#                                                  retract_belief (target_got()),
#                                                  retract_belief (white_corn_got()),
#                                                  retract_belief (for_corn("c12")),
#                                                  prepare_ball_picking(),
#                                                  do_path(["t10"]),
#                                                  #wait_target(),
#                                                  +take_tomatoes() ]
#
#        # ----------------------------------------------------------------------------------
#        (+take_tomatoes()) >> [ retract_belief (take_tomatoes()),
#                                prepare_ball_picking(),
#                                activate_ball_picking(),
#                                do_ball_path("t7"),
#                                activate_opponent_detector(),
#                                assert_belief(for_tomato("t7")) ]
#
#        # ----------------------------------------------------------------------------------
#        (+take_tomatoes_no_prepare()) >> [ retract_belief (take_tomatoes_no_prepare()),
#                                           activate_ball_picking(),
#                                           do_ball_path("t7"),
#                                           activate_opponent_detector(),
#                                           assert_belief(for_tomato("t7")) ]
#
#        # ----------------------------------------------------------------------------------
#        (+ball_got() | for_tomato(_("T")) ) >> [ retract_belief (ball_got()),
#                                                 retract_belief (target_got()),
#                                                 increase_balls(),
#                                                 activate_ball_picking(),
#                                                 activate_opponent_detector(),
#                                                 do_ball_path(_("T")) ]
#
#        # ----------------------------------------------------------------------------------
#        (+opponent_got() | for_tomato(_("T")) ) >> [ -opponent_got(), wait_opponent_over() ]
#        (+opponent_over() | for_tomato(_("T")) ) >> [ -opponent_over(),
#                                                      activate_opponent_detector(),
#                                                      activate_ball_picking(),
#                                                      do_ball_path(_("T")) ]
#        #(+opponent_still_on_the_way() | for_tomato(_("T")) ) >> [ -opponent_still_on_the_way(),
#        #                                                          show("UUUUAAAAHHHHHHHHHH!!!!!!!!!!!") ]
#        (+opponent_still_on_the_way() | for_tomato(_("T")) ) >> [ -opponent_still_on_the_way(),
#                                                                  -for_tomato(_("T")),
#                                                                  change_ball_diagonal(_("T"), "left"),
#                                                                  activate_ball_picking () ]
#
#
#        # ----------------------------------------------------------------------------------
#        (+element_reached(_("T")) | for_tomato(_("T")) ) >> [ +target_got() ]
#        # ----------------------------------------------------------------------------------
#        # Diagonal f13 - f11 - t6 - t4 ---> a4
#        # Vertical a0 - a2 ---> a4
#        # ----------------------------------------------------------------------------------
#        (+target_got() | \
#         (for_tomato(_("T")) & (lambda : (T == "f13") or (T == "f11") or (T == "t6") or (T == "t4") or (T == "a0") or (T == "a2") ))) >> \
#         [ show(_("T")),
#           retract_belief (target_got()),
#           retract_belief (for_tomato(_("T"))),
#           assert_belief (for_tomato("a4")),
#           activate_ball_picking(),
#           activate_opponent_detector(),
#           forward(-30),
#           do_ball_path("a4") ]
#
#        # ----------------------------------------------------------------------------------
#        # Diagonal t10 ---> f11
#        # ----------------------------------------------------------------------------------
#        (+target_got() | (for_tomato(_("T")) & (lambda : (T == "t10")  ) )) >> \
#                       [ show("ON t10"),
#                         retract_belief (target_got()),
#                         retract_belief (for_tomato(_("T"))),
#                         assert_belief (for_tomato("f11")),
#                         activate_ball_picking(),
#                         activate_opponent_detector(),
#                         do_ball_path("f11") ]
#
#
#        # ----------------------------------------------------------------------------------
#        # Diagonal t7 ---> t4
#        # ----------------------------------------------------------------------------------
#        (+target_got() | (for_tomato(_("T")) & (lambda : (T == "t7")  ) )) >> \
#                       [ show("ON t7"),
#                         retract_belief (target_got()),
#                         retract_belief (for_tomato(_("T"))),
#                         assert_belief (for_tomato("t4")),
#                         activate_ball_picking(),
#                         activate_opponent_detector(),
#                         do_ball_path("t4") ]
#
#
#        # ----------------------------------------------------------------------------------
#        # Diagonal t8 ---> t6
#        # ----------------------------------------------------------------------------------
#        (+target_got() | (for_tomato(_("T")) & (lambda : (T == "t8")  ) )) >> \
#                                                             [ show(_("T")),
#                                                               retract_belief (target_got()),
#                                                               retract_belief (for_tomato(_("T"))),
#                                                               assert_belief (for_tomato("t6")),
#                                                               activate_ball_picking(),
#                                                               activate_opponent_detector(),
#                                                               do_ball_path("t6") ]
#
#
#        # ----------------------------------------------------------------------------------
#        # Diagonal f6 - f3 ---> a2
#        # ----------------------------------------------------------------------------------
#        (+target_got() | (for_tomato(_("T")) & (lambda : (T == "f6") or (T == "f3")) )) >> \
#                                                             [ show(_("T")),
#                                                               retract_belief (target_got()),
#                                                               retract_belief (for_tomato(_("T"))),
#                                                               assert_belief (for_tomato("a2")),
#                                                               activate_ball_picking(),
#                                                               activate_opponent_detector(),
#                                                               do_ball_path("a2") ]
#
#
#        # ----------------------------------------------------------------------------------
#        # Diagonal f0 ---> a0
#        # ----------------------------------------------------------------------------------
#        (+target_got() | (for_tomato(_("T")) & (lambda : (T == "f0") ) )) >> \
#                                                             [ show(_("T")),
#                                                               retract_belief (target_got()),
#                                                               retract_belief (for_tomato(_("T"))),
#                                                               assert_belief (for_tomato("a0")),
#                                                               activate_ball_picking(),
#                                                               activate_opponent_detector(),
#                                                               do_ball_path("a0") ]
#
#
#        # ----------------------------------------------------------------------------------
#        # Diagonal t2 ---> a2
#        # ----------------------------------------------------------------------------------
#        (+target_got() | (for_tomato(_("T")) & (lambda : (T == "t2") or (T == "f4") ) )) >> \
#                                                             [ show(_("T")),
#                                                               retract_belief (target_got()),
#                                                               retract_belief (for_tomato(_("T"))),
#                                                               assert_belief (for_tomato("a2")),
#                                                               activate_ball_picking(),
#                                                               activate_opponent_detector(),
#                                                               do_ball_path("a2") ]
#
#
#        # ----------------------------------------------------------------------------------
#        (+element_reached("a4") | for_tomato("a4") ) >> [ target_poller_off(),
#                                                            retract_belief (target_got()),
#                                                            retract_belief (for_tomato("a4")),
#                                                            show("Got some objects"),
#                                                            +first_episode_over () ]
#
#        (+target_got() | for_tomato("a4") ) >> [ retract_belief (target_got()),
#                                                  retract_belief (for_tomato("a4")),
#                                                  target_poller_off(),
#                                                  show("Got some objects"),
#                                                  +first_episode_over () ]
#
#        # ----------------------------------------------------------------------------------
#        (+first_episode_over() | (homologation("no") & corns_in_robot(_("X")) & (lambda : X <= 1) )) >> [ deposit_corns(),
#                                                                                                          forward(-110),
#                                                                                                          wait_target(),
#                                                                                                          freeze_timer(),
#                                                                                                          +are_more_corns_worth() ]
#                                                                                                          #[ end_ball_picking(),
#                                                                                                          #forward(-50),
#                                                                                                          #reach_point_back ("t3"),
#                                                                                                          #+second_episode_over() ]
#                                                                                                          #forward(-60),
#                                                                                                          #deploy_carriage(),
#                                                                                                          #+prepare_to_grab_corn("a4", "c2") ]
#
#        (+first_episode_over() | (homologation("yes") )) >> [ end_ball_picking(),
#                                                              forward(-50),
#                                                              reach_point_back ("t3"),
#                                                              +second_episode_over() ]
#
#        (+first_episode_over() | (corns_in_robot(_("X")) & (lambda : X > 1))) >> [ deposit_corns(),
#                                                                                   forward(-110),
#                                                                                   wait_target(),
#                                                                                   freeze_timer(),
#                                                                                   +are_more_corns_worth() ]
#                                                                                   #deploy_carriage(),
#                                                                                   #+prepare_to_grab_corn("a4", "c2") ]
#
#        # ----------------------------------------------------------------------------------
#        # we have no balls... :-( OK, it's worth to take more corns
#        #(+are_more_corns_worth() | balls_in_robot(0) ) >> [ deploy_carriage(),
#        #                                                    +prepare_to_grab_corn("a4", "c2") ]
#
#        # we have balls, and we have time to take more corns :-)))
#        #(+are_more_corns_worth() | (balls_in_robot(_("X")) & (lambda : X > 0) &
#        # elapsed_timer(_("T")) & (lambda : T <= 60)) ) >> [ deploy_carriage(),
#        #                                                    +prepare_to_grab_corn("a4", "c2") ]
#
#        # we have balls, but we have no time to take more corns :-)
#        #(+are_more_corns_worth() | (balls_in_robot(_("X")) & (lambda : X > 0) &
#        # elapsed_timer(_("T")) & (lambda : T > 60)) ) >> [ reach_point_back ("t3"),
#        #                                                   +second_episode_over() ]
#
#        (+are_more_corns_worth() ) >> [ reach_point_back ("t3"),
#                                        +second_episode_over() ]
#
#
#        # ----------------------------------------------------------------------------------
#        (+second_episode_over() | (corns_in_robot(_("X")) & (lambda : X > 0) ) ) >> [ retract_carriage(),
#                                                                                      reach_point("a4"),
#                                                                                      deposit_corns(),
#                                                                                      forward(-110),
#                                                                                      wait_target(),
#                                                                                      reach_point_back ("t3"),
#                                                                                      reach_point ("a3"),
#                                                                                      heading_to (-90),
#                                                                                      forward (-110),
#                                                                                      heading_to (-70),
#                                                                                      forward(-80),
#                                                                                      show("Waiting for discharge"),
#                                                                                      wait_target(),
#                                                                                      show("Starting discharge"),
#                                                                                      deposit_tomatoes() ]
#
#        # ----------------------------------------------------------------------------------
#        (+second_episode_over() | (corns_in_robot (0)) ) >> [ reach_point ("a3"),
#                                                              heading_to (-90),
#                                                              forward (-110),
#                                                              heading_to (-70),
#                                                              forward(-80),
#                                                              show("Waiting for discharge"),
#                                                              wait_target(),
#                                                              show("Starting discharge"),
#                                                              deposit_tomatoes() ]
#
#        # ----------------------------------------------------------------------------------
#
#        ( +prepare_to_grab_corn ("a4", "c2") | (white_corn ("c2")))  >> [ retract_belief (prepare_to_grab_corn ("a4", "c2")),
#                                                                          do_path_back (["t3"]),
#                                                                          orientate_towards ("c2"),
#                                                                          #wait_target(),
#                                                                          assert_belief (for_corn("c2")),
#                                                                          reach_corn ("c2") ]
#
#        # ----------------------------------------------------------------------------------
#        ( +prepare_to_grab_corn ("a4", "c2") | (black_corn ("c2")))  >> [ retract_belief (prepare_to_grab_corn ("a4", "c2")),
#                                                                          reach_point_back ("t3"),
#                                                                          +second_episode_over() ]
#
#        # ----------------------------------------------------------------------------------
#        ( +grab_corn(_("C")) | (white_corn(_("C"))) ) >>  [ +for_corn(_("C")), reach_corn(_("C")) ]
#
#        # ----------------------------------------------------------------------------------
#        ( +white_corn_got() | (for_corn("c2")  ) )   >>  [ increase_corn(),
#                                                           retract_belief (white_corn_got()),
#                                                           retract_belief (for_corn("c2")),
#                                                           retract_carriage(),
#                                                           forward(-100),
#                                                           reach_point("a4"),
#                                                           deposit_corns(),
#                                                           forward(-110),
#                                                           reach_point_back ("t3"),
#                                                           +second_episode_over() ]
#
#        (+target_got() | (for_corn("c2") & corns_in_robot(0) ) ) >> [ retract_belief (target_got()),
#                                                                      retract_belief (for_corn("c2")),
#                                                                      forward(-120),
#                                                                      +second_episode_over() ]
#
#        # TO BLUE
#        (+target_got() | (for_corn("c2") & (corns_in_robot(_("X"))) & (lambda : X > 0)) ) >> [ retract_belief (white_corn_got()),
#                                                                                               retract_belief (for_corn("c2")),
#                                                                                               retract_carriage(),
#                                                                                               forward(-100),
#                                                                                               reach_point("a4"),
#                                                                                               deposit_corns(),
#                                                                                               forward(-110),
#                                                                                               reach_point_back ("t3"),
#                                                                                               +second_episode_over()  ]
#
#        # ----------------------------------------------------------------------------------
#
#
#
#
## }}} END Game Strategies
