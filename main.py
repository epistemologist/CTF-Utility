import cmd
import base64
import binascii
from string import ascii_lowercase as lower, ascii_uppercase as upper
from math import sqrt

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

def shift_char(char, shift):
	if char in upper:
		return upper[(upper.index(char) + shift)%26]
	if char in lower:
		return lower[(lower.index(char) + shift)%26]
	return char

def caesar(string, shift):
	return "".join([shift_char(i, shift) for i in string])
throw_error = lambda e: print("Something went wrong! Here's an error: ", e)

def prob_english(string):
	letter_freqs = [8.55, 1.60, 3.16, 3.87, 12.10, 2.18, 2.09, 4.96, 7.33, 0.22, 0.81, 4.21, 2.53, 7.17, 7.47, 2.07, 0.10, 6.33, 6.73, 8.94, 2.68, 1.06, 1.83, 0.19, 1.72, 0.11] # from http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/
	letter_counts = [string.lower().count(i) for i in lower]
	norm = lambda v: sqrt(sum([i*i for i in v])) # Function to return norm of vector
	dot = lambda u,v: sum([u[i]*v[i] for i in range(len(u))]) # Function to return the dot product of two vectors
	cosine = lambda u,v: dot(u,v) / (norm(u) * norm(v))
	return cosine(letter_counts, letter_freqs)
class Cmd(cmd.Cmd):
	def do_base2(self, line):
		temp = process_input(line, ["d", "e"])
		if temp:
			mode, string = temp
			if mode == "d":
				try:
					print(int_to_bytes(int(string,2)))
					return
				except Exception as e:
					throw_error(e); return
			if mode == "e":
				try:
					print(bin(bytes_to_int(string.encode()))[2:])
					return
				except Exception as e:
					throw_error(e); return
		print("Invalid syntax!")
		return
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
	def do_caesar(self, line):
		temp = process_input(line, ["r"+str(i) for i in range(26)] + ["b","g"])
		if temp:
			mode, string = temp
			if "r" in mode:
				shift = ["r"+str(i) for i in range(26)].index(mode)
				try:
					print(caesar(string, shift))
					return
				except Exception as e:
					throw_error(e); return
			if mode == "b":
				try:
					for i in range(26):
						print("{}: ".format(i), caesar(string, i))
					return
				except Exception as e:
					throw_error(e); return
			if mode == "g":
				try:
					potential_ciphers = sorted([(i, caesar(string,i)) for i in range(26)], key = lambda x: -prob_english(x[1]))
					for i in potential_ciphers[:10]:
						print("{}: {}".format(*i))
					return
				except Exception as e:
					throw_error(e); return
		print("Invalid syntax!")
		return
	def do_EOF(self, line):
		return True


if __name__ == '__main__':
	Cmd().cmdloop()


