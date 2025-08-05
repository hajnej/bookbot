from stats import get_num_words, get_characters_count, sort_characters_by_frequency
import sys

def check_args():
  """
  Checks for the correct number of command-line arguments.

  Exits the program if the argument count is not 2.

  Returns:
    str: The file path provided as a command-line argument.
  """
  if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    return sys.argv[1]

def get_book_text(file_path):
  """
  Reads the contents of a text file and returns it as a string.

  Args:
    file_path (str): The path to the text file to be read.

  Returns:
    str: The full contents of the file as a single string.
  """
  with open(file_path) as f:
    file_contents = f.read()
  return file_contents

def main():
  """
  The main function to run the book analysis.

  It gets the book path from command-line arguments, reads the book,
  and prints a report of word and character counts.
  """
  file_name = check_args()
  text = get_book_text(file_name)
  num_words = get_num_words(text)
  characters_stats = get_characters_count(text)
  print(f"""============ BOOKBOT ============
Analyzing book found at ${file_name}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
""")
  for char_stat in sort_characters_by_frequency(characters_stats):
    if char_stat['char'].isalpha():
      print(f"{char_stat['char']}: {char_stat['num']}")
  print("""============= END ===============""")

main()
