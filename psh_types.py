class Token:
  def __init__(self, symbol: int, value: str):
    self.symbol = symbol
    self.value = value

class Job:
  def __init__(self, args: [str], infile: str = "", outfile: str = "",
      next: Token = None):
    self.args = args
    self.infile = infile
    self.outfile = outfile
    self.next = next
    self.error = False
    self.error_msg = ''

class Symbol:
  WORD, SPACE, DOLLAR = 0, 1, 2

class PathCode:
  F, NF, NE, NP = 0, 1, 2, 3
  error_msg = [ '',
      'command not found',
      'no such file or directory',
      'permission denied',
      ]
