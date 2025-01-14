# -*- coding: utf-8 -*-
"""Class definition for DFTimewolf modules."""

import abc


class BaseModule(object):
  """Base class for modules.

  Attributes:
    critical: Boolean indicating whether the execution of this module is
        critical to the execution of the recipe. If set to True, and the module
        fails to properly run, the recipe will be aborted.
    input: variable containing elements to be processed by a module.
    output: variable containing the output of a module's execution.
  """

  def __init__(self, state, critical=False):
    """Initialize a module.

    Args:
      state (DFTimewolfState): a state.
      critical (Optional[bool]): True if the module is critical, which causes
          the entire recipe to fail if the module encounters an error.
    """
    super(BaseModule, self).__init__()
    self.critical = critical
    self.state = state

  def CleanUp(self):
    """Cleans up module output to prepare it for the next module."""
    # No clean up is required.
    return

  @abc.abstractmethod
  def Process(self):
    """Processes input and builds the module's output attribute.

    Modules take input information and process it into output information,
    which can in turn be ingested as input information by other modules.
    """

  @abc.abstractmethod
  def SetUp(self, *args, **kwargs):
    """Sets up necessary module configuration options."""
