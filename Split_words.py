text = "This is a text that should be split up by words"

text_split = text.split(" ")
text_reverse = text_split[::-1]

output = ""
for i in text_reverse:
    output += i.strip() + " "

print(output)