import cmd
import base64

def process_input(line, valid_modes):
	args = line.split()
	if len(args) < 2: return None
	mode = args[0]
	if len(args) >= 2 and mode in valid_modes:
		return (mode, " ".join(args[1:]))
	return None

throw_error = lambda e: print("Something went wrong! Here's an error: ", e)
class HelloWorld(cmd.Cmd):
	def do_base64(self, line):
		temp = process_input(line, ["d", "e"])
		if temp:
			mode, string = temp
			if mode == "d":
				try:
					print(base64.b64decode(string).decode("utf8"))
					return
				except Exception as e:
					throw_error(e); return
			if mode == "e":
				try:
					print(base64.b64encode(string.encode()).decode("utf8"))
					return
				except Exception as e:
					throw_error(e); return
		print("Invalid syntax!")
		return
	def do_EOF(self, line):
		return True
if __name__ == '__main__':
	HelloWorld().cmdloop()


