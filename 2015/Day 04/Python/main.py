import hashlib

def main():
  input = "ckczppom"
  zeros = [5,6]
  for zero in zeros:
    hex_num, num = find_hex(input, zero)
    if hex_num != "None":
      print(f"{input} + {num:,} produces hex output {hex_num}!")
    else:
      print("No appropriate hash found in that range!")
  
def find_hex(raw: str, initial_zeros: int)->tuple[str, int]:
  leading_zeros = "0" * initial_zeros
  for i in range(100000,10000000):
    test = bytes((raw+str(i)), 'utf-8')
    result = str(hashlib.md5(test).hexdigest())
    if result.startswith(leading_zeros):
      return result, i
  return "None", -1

if __name__ == "__main__":
  main()
