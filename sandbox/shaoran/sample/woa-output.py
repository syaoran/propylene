# Beliefs section
class white_corn(Belief):
  pass

class black_corn(Belief):
  pass

class corns_in_robot(Belief):
  pass

class no_more_corns(Belief):
  pass


# Goals section
class go(Goal):
  pass

class grab_corn(Goal):
  pass

class deposit_corn(Goal):
  pass


# Actions section
class detect_configuration(Action):
  def execute(self):
    ## ...

class reach_corn(Action):
  def execute(self):
    ## ...

class pick_corn(Action):
  def execute(self):
    ## ...

class reach_deposit_zone(Action):
  def execute(self):
    ## ...

class open_tank(Action):
  def execute(self):
    ## ...
