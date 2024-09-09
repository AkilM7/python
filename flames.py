def remove_common_letters(name1, name2):
    list1 = list(name1)
    list2 = list(name2)
    
    for letter in list1[:]:
        if letter in list2:
            list1.remove(letter)
            list2.remove(letter)
    
    return list1 + list2

def flames_result(count):
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]
    
    return flames[0]

def flames_game(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()
    
    # Remove common letters
    remaining_letters = remove_common_letters(name1, name2)
    
    # Count remaining letters
    count = len(remaining_letters)
    
    # Get FLAMES result
    result = flames_result(count)
    
    # Mapping the result to the relationship
    flames_mapping = {
        'F': "Friends",
        'L': "Love",
        'A': "Affection",
        'M': "Marriage",
        'E': "Enemies",
        'S': "Siblings"
    }
    
    return flames_mapping[result]

# Example usage
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

relationship = flames_game(name1, name2)
print(f"The relationship between {name1} and {name2} is: {relationship}")

