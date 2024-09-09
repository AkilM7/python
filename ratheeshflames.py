def flames_game(name1, name2):
    # Convert names to lowercase and remove spaces
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    # Find common letters and remove them from both names
    for char in name1[:]:
        if char in name2:
            name1 = name1.replace(char, '', 1)
            name2 = name2.replace(char, '', 1)

    # Calculate the remaining letters count
    count = len(name1) + len(name2)

    # FLAMES acronym
    flames = ['Friends', 'Lovers', 'Affectionate', 'Marriage', 'Enemies', 'Siblings']

    # Find the relationship
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            flames = flames[split_index+1:] + flames[:split_index]
        else:
            flames = flames[:len(flames)-1]
    
    return flames[0]

# Example usage:
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

relationship = flames_game(name1, name2)
print(f"The relationship is: {relationship}")
