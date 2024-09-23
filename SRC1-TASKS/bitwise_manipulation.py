# | is or
# ^ is xor
# & is and
def toggle_string(s:str) -> str:
    return_s = ""
    for _ in s:
        return_s += chr((ord(_) ^ 0x20))
    #next _
    return return_s
        
print(toggle_string("some"))