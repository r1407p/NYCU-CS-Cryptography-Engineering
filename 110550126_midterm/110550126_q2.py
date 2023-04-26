def str_to_int(str):
    return int(str.encode().hex(), 16)

text = "attack at dawn"
int_of_text = str_to_int(text)
key = int_of_text ^ 0x09e1c5f70a65ac519458e7e53f36

target = "attack at dusk"
int_of_target = str_to_int(target)
ans = int_of_target ^ key
print( hex(ans))