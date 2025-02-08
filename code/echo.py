def echo(text, repetitions = 3):
    starting_index = -repetitions
    output = ""
    for i in range(repetitions):
        for k in range(starting_index, 0):
            output += text[k]
        if starting_index == -1:
            output += "\n."
        else:
            output += "\n"
        starting_index += 1
        
    return output
        
text = "echo123"
print(echo(text))
