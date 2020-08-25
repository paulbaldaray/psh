from os import getenv
from psh_types import Token, Job, Symbol, PathCode
from psh_lex import lex
from psh_path import get_path
from psh_builtins import builtins

def add_word_str(args: [str], word: [str]):
	word_str: str = "".join(word)
	if len(word_str):
		args.append(word_str)
	word.clear()

def process(tokens: [Token]) -> [Job]:
	tlen: int = len(tokens)
	word: [str] = []
	args: [str] = []
	for i in range(tlen):
		token: Token = tokens[i]
		if token.symbol == Symbol.WORD:
			word.append(token.value)
		elif token.symbol == Symbol.SPACE:
			add_word_str(args, word)
		elif token.symbol == Symbol.DOLLAR:
			word.append(getenv(token.value, ""))
	add_word_str(args, word)
	return Job(args)

def parse(command: str) -> [Job]:
	head: Job = process(lex(command))
	tail: Job = head
	while tail:
		if len(tail.args) == 0 and tail is not head:
			head.error = True
			head.error_msg = "psh: parse error near `|'"
			head.next = None
			break
		elif len(tail.args) and tail.args[0] not in builtins:
			err, cmd = get_path(tail.args[0])
			if err == PathCode.F:
				tail.args[0] = cmd
			else:
				tail.error = True
				tail.error_msg = f'psh: {PathCode.error_msg[err]}: {cmd}'
		tail = tail.next
	return head
