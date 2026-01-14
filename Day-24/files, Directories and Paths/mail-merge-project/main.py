STARTING_LETTER = open("Input/Letters/starting_letter.txt", "r").readlines()
NAMES = open("Input/Names/Invited_names.txt").readlines()

for name in NAMES:
    name = name.rstrip("\n")
    for line in STARTING_LETTER:
        if("[Name]" in line):
            open(f"./Output/ReadyToSend/letter_for_{name}.txt","a").write(f"Dear {name},\n")
        else:
            open(f"./Output/ReadyToSend/letter_for_{name}.txt","a").write(line)
