from os import _exit as exit
from psh_path import get_path

def b_exit(args: [str]) -> None:
	exit_code: int = int(args[1]) if len(args) > 1 else 0
	exit(exit_code)

def b_which(args: [str]):
	i: int = 1
	while i < len(args):
		err, cmd = get_path(args[i])
		if args[i] in builtins:
			print(f'{args[i]}: shell built-in command')
		elif err:
			print(cmd, 'not found')
		else:
			print(cmd)
		i += 1

builtins = {
	'exit' : b_exit,
	'which' : b_which,
}
