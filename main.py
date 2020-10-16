import cmd
import base64
import binascii


def process_input(line, valid_modes):
	args = line.split()
	if len(args) < 2: return None
	mode = args[0]
	if len(args) >= 2 and mode in valid_modes:
		return (mode, " ".join(args[1:]))
	return None

def base58_encode(bytes_in):
	N = bytes_to_int(bytes_in)
	chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
	out = ""
	while N > 0:
		N, remainder = divmod(N, 58)
		out += chars[remainder]
	return out[::-1]

def base58_decode(s_in):
	s_in = s_in[::-1]
	chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
	return int_to_bytes(sum([chars.index(s_in[i])*58**i for i in range(len(s_in))]))

def bytes_to_int(b):
	return int(base64.b16encode(b).decode(),16)
def int_to_bytes(N):
	return bytes.fromhex(hex(N)[2:])

throw_error = lambda e: print("Something went wrong! Here's an error: ", e)
class HelloWorld(cmd.Cmd):
	def do_base8(self, line):
		temp = process_input(line, ["d", "e"])
		if temp:
			mode, string = temp
			if mode == "d":
				try:
					print(int_to_bytes(int(string,8)))
					return
				except Exception as e:
					throw_error(e); return
			if mode == "e":
				try:
					print(oct(bytes_to_int(string.encode()))[2:])
					return
				except Exception as e:
					throw_error(e); return
		print("Invalid syntax!")
		return
	def do_base16(self, line):
		temp = process_input(line, ["d", "e"])
		if temp:
			mode, string = temp
			if mode == "d":
				try:
					print(base64.b16decode(string))
					return
				except Exception as e:
					throw_error(e); return
			if mode == "e":
				try:
					print(base64.b16encode(string.encode()).decode("utf8"))
					return
				except Exception as e:
					throw_error(e); return
		print("Invalid syntax!")
		return
	def do_base32(self, line):
		temp = process_input(line, ["d", "e"])
		if temp:
			mode, string = temp
			if mode == "d":
				try:
					print(base64.b32decode(string))
					return
				except Exception as e:
					throw_error(e); return
			if mode == "e":
				try:
					print(base64.b32encode(string.encode()).decode("utf8"))
					return
				except Exception as e:
					throw_error(e); return
		print("Invalid syntax!")
		return
	def do_base58(self, line):
		temp = process_input(line, ["d", "e"])
		if temp:
			mode, string = temp
			if mode == "d":
				try:
					print(base58_decode(string))
					return
				except Exception as e:
					throw_error(e); return
			if mode == "e":
				try:
					print(base58_encode(string.encode()))
					return
				except Exception as e:
					throw_error(e); return
		print("Invalid syntax!")
		return
	def do_base64(self, line):
		temp = process_input(line, ["d", "e"])
		if temp:
			mode, string = temp
			if mode == "d":
				try:
					print(base64.b64decode(string))
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
	def do_base85(self, line):
		temp = process_input(line, ["d", "e"])
		if temp:
			mode, string = temp
			if mode == "d":
				try:
					print(base64.b85decode(string))
					return
				except Exception as e:
					throw_error(e); return
			if mode == "e":
				try:
					print(base64.b85encode(string.encode()).decode("utf8"))
					return
				except Exception as e:
					throw_error(e); return
		print("Invalid syntax!")
		return
	def do_EOF(self, line):
		return True

if __name__ == '__main__':
	HelloWorld().cmdloop()


