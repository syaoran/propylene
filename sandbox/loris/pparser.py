# ------------------------------------------------------------------------------
# plexer.py
#
# A parser for PROFETA
# ------------------------------------------------------------------------------
# e` molto buio quando fuori piove
# ------------------------------------------------------------------------------
# Grammar Rules
#
# Plan ::= Head '>>' ActionList
#
# Head ::= Event
#        | Event '|' Condition
#
# Condition ::= Belief 
#             | Lambda
#             | Belief '&' Condition
#
# Event ::= GoalEvent
#         | BeliefEvent
#
# GoalEvent ::= '+' '~' Belief
#
# BeliefEvent ::= '+' Belief
#               | '-' Belief
#
# ActionList ::= '[' PlanBody ']'
# 
# PlanBody ::= Event
#            | Event ',' PlanBody
#            | Action
#            | Action ',' PlanBody
#
# Belief ::= LITERAL '(' ListOfArguments ')'
# 
# Action ::= LITERAL '(' ListOfArguments ')'
#
# ListOfArguments ::= Argument
#                  | Argument ',' ListOfArguments
#
# Argument ::= '_' '"' CHAR '"'
#            | NUMBER
#
# ------------------------------------------------------------------------------



