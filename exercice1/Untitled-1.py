def count_and_replace():
    input_file = "file_to_read.txt"
    output_file = "result.txt"
    word_to_count = "terrible"

    with open(input_file, "r") as file:
        content = file.read()

    count = content.count(word_to_count)

    replaced_content = content.split(word_to_count)
    for i in range(1, count + 1):
        if i % 2 == 0:
            replaced_content[i] = "pathetic" + replaced_content[i]
        else:
            replaced_content[i] = "marvellous" + replaced_content[i]

    new_content = "".join(replaced_content)

    # Remove the remaining occurrences of "terrible"
    new_content = new_content.replace(word_to_count, "")

    with open(output_file, "w") as file:
        file.write(new_content)

    return count

total_count = count_and_replace()
print("Total occurrences of 'terrible':", total_count)