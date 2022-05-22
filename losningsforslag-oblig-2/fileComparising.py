def replace_punctuation(words):
    for ch in words:
        if ch in "~@#$%^&()_~?/,.;!{}[]|'\"\n ":
            words = words.replace(ch, "")
    return words

def words_from_file_set(from_file):
    output_list = set()
    for words in from_file:
        for word in words.split():
            word = replace_punctuation(word.lower())
            output_list.add(word)
    return output_list

def main(): #Test texts: Python/Kap 13-15/Kap 13/teamSorted.txt / Oblig1/test.txt / Python/Kap 13-15/Kap 13/team.txt 

    filename_1 =  input("Enter filename of the first file: ") 
    filename_2 =  input("Enter filename of the second file: ")

    try:
        input_file_1 = open(filename_1, "r")
        input_file_2 = open(filename_2, "r")

        unique_words_file1 = words_from_file_set(input_file_1)
        unique_words_file2 = words_from_file_set(input_file_2)
        
        input_file_1.close()
        input_file_2.close()

        uniques_list = unique_words_file1 | unique_words_file2        #Union
        common_words = unique_words_file1 & unique_words_file2        #Intersection
        file1_words_only = unique_words_file1 - unique_words_file2    #Difference
        file2_words_only = unique_words_file2 - unique_words_file1    #Difference
        words_not_in_common = unique_words_file1 ^ unique_words_file2 #Symmetric difference

        print("\n---------------------------------------------")

        print("Number of uniques in:")
        print(format("File 1", "<15"),
            format("File 2", "<15"), 
            format("Total",  "<15"), "\n")

        print(format(len(unique_words_file1),"<15"),
            format(len(unique_words_file2),"<15"), 
            format(len(uniques_list),      "<15"))

        print("\n---------------------------------------------")

        print("All unique words:")
        print(format("File 1", "<15"),
            format("File 2", "<15"), "\n")

        for i in range(max(len(unique_words_file1), len(unique_words_file2))):
            try:
                print(format(list(unique_words_file1)[i], "<15"), end = "")
            except IndexError:
                print(format("", "<15"), end = "")
            try:
                print(format(list(unique_words_file2)[i], "<15"))
            except IndexError:
                print(format("", "<15"))

        print("\n-------------------------------------------------------------------------------------------")

        print("Unique words:")
        print(format("Words in common   |",  "<20"),
            format("Words in file 1 only  |", "<20"), 
            format("Words in file 2 only  |", "<20"), 
            format("Words not in common   |", "<20"), "\n")

        for i in range(max(len(common_words), len(file1_words_only), len(file2_words_only), len(words_not_in_common))):
            try:
                print(format(list(common_words)[i], "<25"), end = "")
            except IndexError:
                print(format("", "<25"), end = "")
            try:
                print(format(list(file1_words_only)[i], "<25"), end = "")
            except IndexError:
                print(format("", "<25"), end = "")
            try:
                print(format(list(file2_words_only)[i], "<25"), end = "")
            except IndexError:
                print(format("", "<25"), end = "")
            try:
                print(format(list(words_not_in_common)[i], "<25"))
            except IndexError:
                print(format("", "<25"))

    except FileNotFoundError as ex:
        print(f'\n{ex}')

if __name__ == '__main__':
    main()