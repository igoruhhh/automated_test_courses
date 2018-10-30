example = []
with open("example_for_task3.txt") as f:
    for line in f:
        example.append(line.split())

alphabet = []
for list in example:
    for item in list:
        alphabet.append(item.strip("""~`!@#$%^&*()_+-=[]{};':"/?.,><""").lower())

alphabet.sort()

with open("example_result_task3", "w") as f:
    while alphabet:
        word = alphabet[0]
        print(alphabet.count(word), word, file=f)
        for i in range(alphabet.count(word)):
           alphabet.remove(word)