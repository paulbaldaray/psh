from os import environ, path, access, getenv
from os import F_OK, X_OK
from psh_types import PathCode

def get_path(cmd: str) -> (int, str):
  if (path.basename(cmd) != cmd):
    if not access(cmd, F_OK):
      return (PathCode.NE, cmd)
    elif not access(cmd, X_OK):
      return (PathCode.NP, cmd)
    else:
      return (PathCode.F, cmd)
  else:
    paths = getenv('PATH').split(':')
    for p in paths:
      abs_path: str = p+'/'+cmd
      if access(abs_path, X_OK):
        return (PathCode.F, abs_path)
    return (PathCode.NF, cmd)
