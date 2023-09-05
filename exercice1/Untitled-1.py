def count_and_replace(file_path):
    # Read the input file
    with open(file_path, 'r') as file:
        text = file.read()

    # Calculate the total occurrences of "terrible"
    count = text.count('terrible')

    # Replace even occurrences of "terrible" with "pathetic" and odd occurrences with "marvellous"
    new_text = text.replace('terrible', 'pathetic', count % 2 == 0)
    new_text = new_text.replace('terrible', 'marvellous', count % 2 != 0)

    # Write the modified text to a new file
    with open('result.txt', 'w') as file:
        file.write(new_text)

    return count

file_path = 'file_to_read.txt'
occurrences = count_and_replace(file_path)
print(f'Total occurrences of "terrible": {occurrences}')