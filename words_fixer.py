split_lines = []

with open("raw_words.txt", "r") as f:
    lines = list(f)
    print(lines)
    
    split_lines = [word.lower().split() for word in lines]
    split_lines = [word for lst in split_lines for word in lst]

print(split_lines)
    
        
with open("fixed_words.txt", "w") as f:
    f.write("\n".join(split_lines))
    