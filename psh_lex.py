from string import ascii_letters as letters, digits
from psh_types import Token, Job, Symbol

# These maps are shorthand for a char[256] table in C
special = {' ', '$',}
dollar_allowed = { *(c for c in (letters+digits+'_')) }
dollar_start = { *(c for c in (letters+'_')) }
dollar_special = {}

def add_word(tokens: Token, word: [str]):
  if len(word):
    word_str: Token = Token(Symbol.WORD,  "".join(word))
    tokens.append(word_str)
    word.clear()

def add_space(tokens: Token, cmd: str, clen: int, i: int, word: [str]) -> int:
  space: Token = Token(Symbol.SPACE, "")
  tokens.append(space)
  while i+1 < clen and cmd[i+1] == ' ':
    i += 1
  return i

def add_dollar(tokens: Token, cmd: str, clen: int, i: int, word: [str]) -> int:
  dword: [str] = []
  if i+1 < clen and cmd[i+1] in dollar_start:
    while i+1 < clen and cmd[i+1] in dollar_allowed:
      dword += [cmd[i+1]]
      i += 1
    symbol: int = Symbol.DOLLAR
    value: str = "".join(dword)
  elif i+1 == clen or cmd[i+1] not in dollar_special:
    symbol: int = Symbol.WORD
    value: str = "$"
  else:
    symbol, value = dollar_special[cmd[i+1]]()
    i += 1
  dollar: Token = Token(symbol, value)
  tokens.append(dollar)
  return i

add_symbol = { ' ' : add_space, '$' : add_dollar, }

def lex(cmd: str) -> [Token]:
  clen: int = len(cmd)
  tokens: [Token] = []
  word: [str] = []

  i = 0
  while i < clen:
    if cmd[i] in special:
      add_word(tokens, word)
      i = add_symbol[cmd[i]](tokens, cmd, clen, i, word)
    else:
      word.append(cmd[i])
    i += 1
  add_word(tokens, word)
  return tokens
