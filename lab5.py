# this is the main function that initalizes with
# asking the user for info this also calls the
# print_banner function with the word and direction as the args


def main():
    word_to_print = input("Enter a word to print!\n")
    direction_to_print = input("Type 'h' for horizonal or 'v' for vertical\n")
    print_banner(word_to_print.upper(), direction_to_print)

# This is a dictionary that stores the ascii art for each letter


letters = {
            "A": ["###", "# #", "###", "# #", "# #"],
            "B": ["#  ", "#  ", "###", "# #", "###"],
            "C": ["###", "#  ", "#  ", "#  ", "###"],
            "D": ["  #", "  #", "###", "# #", "###"],
            "E": ["###", "#  ", "## ", "#  ", "###"],
            "F": ["###", "#  ", "## ", "#  ", "#  "],
            "G": ["###", "# #", "###", "  #", "###"],
            "H": ["# #", "# #", "###", "# #", "# #"],
            "I": ["###", " # ", " # ", " # ", "###"],
            "J": ["####", "  # ", "  # ", "# # ", "### "],
            "K": ["#  #", "# # ", "##  ", "# # ", "#  #"],
            "L": ["#  ", "#  ", "#  ", "#  ", "###"],
            "M": ["#  #", "## ##", "# # #", "#    #", "#    "],
            "N": ["#   #", "##  #", "# # #", "#  ##", "#   #"],
            "O": ["###", "# #", "# #", "# #", "###"],
            "P": ["###", "# #", "###", "#  ", "#  "],
            "Q": ["###", "# #", "###", "  #", "  #"],
            "R": ["### ", "#  #", "### ", "# # ", "#  #"],
            "S": ["###", "#  ", "###", "  #", "###"],
            "T": ["###", " # ", " # ", " # ", " # "],
            "U": ["# #", "# #", "# #", "# #", "###"],
            "V": ["# #", "# #", "# #", "# #", " # "],
            "W": ["#   #", "#   #", "# # #", "## ##", "#   #"],
            "X": ["#   #", " # # ", "  #  ", " # # ", "#   #"],
            "Y": ["#   #", " # # ", "  #  ", "  #  ", "  #  "],
            "Z": ["#####", "   # ", "  #  ", " #   ", "#####"]}

# This is the function that takes in two strings, one being the word
# and the other being the direction the banner should print.
# this function loops through the word and uses the dictionary to
# manipulate each string.


def print_banner(wrd, dir):
    if dir == 'v':
        for letter in wrd:
            print("\n".join(letters[letter]) + "\n")
    elif dir == 'h':
        for row in range(len(letters['A'])):
            for letter in wrd:
                print(letters[letter][row], end="  ")
            print()
    else:
        print("Sorry that character is invalid")


# VOODOO MAGIC
if __name__ == "__main__":
    main()
