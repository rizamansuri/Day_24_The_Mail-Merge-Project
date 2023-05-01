# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt

# Created a list of names from the invited_names file.
with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

# Removed \n from each list element
for i in range(len(names_list)):
    names_list[i] = names_list[i].strip("\n")

# Created separate invitation mails for each name.
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    content = letter.read()
    for i in range(len(names_list)):
        name = names_list[i]
        new_content = content.replace("[name]", name)
        with open(f"./ReadyToSend/{name}.txt", "w") as output:
            output.write(new_content)
