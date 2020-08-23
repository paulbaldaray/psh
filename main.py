from os import fork, execv, wait
from psh_parse import parse
from psh_builtins import builtins
from psh_types import Job

def run(job):
  pid = fork()
  if pid == 0:
    execv(job.args[0], job.args)
  wait()

def main():
  while True:
    head: Job = parse(input(": "))
    has_error: bool = False
    tail: Job = head
    while tail:
      if tail.error:
        has_error = True
        print(tail.error_msg)
      tail = tail.next
    if not len(head.args) or has_error:
      continue
    cmd_name: str = head.args[0]
    if cmd_name in builtins:
      builtins[cmd_name](head.args)
    else:
      run(head)

if __name__ == '__main__':
  main()
