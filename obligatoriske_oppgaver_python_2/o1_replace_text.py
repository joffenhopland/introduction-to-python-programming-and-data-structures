def replace_text():

    file = input("Enter a filename: ").strip()

    output_file = open(file, "w")
    old_string = input("Enter the old string to be replaced: ")
    output_file.write(old_string)
    output_file.close()

    new_string = input("Enter the new string to replace the old string: ")
    output_file = open(file, "w")
    output_file.write(new_string)
    output_file.close()


replace_text()
