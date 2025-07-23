period = int(input())
word = input()
stavane = "abcdefghijklmnopqrstuvwxyz"
decode_word = ""
for stav in word:
    stav_index = stavane.find(stav)
    decode_stav = stav_index - period
    decode_word += stavane[decode_stav]
print(decode_word)