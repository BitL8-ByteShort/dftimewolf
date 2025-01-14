"""Generic error wrapper"""

class DFTimewolfError(Exception):
  """Class to represent a DFTimewolfError."""

  def __init__(self, message=None):
    """Initializes the DFTimewolfError with provided or default message."""
    super(DFTimewolfError, self).__init__(message)
    self.message = message or 'An error occurred.'


class RecipeParseError(DFTimewolfError):
  """Error when parsing a recipe."""
