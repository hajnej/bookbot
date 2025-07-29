from stats import get_num_words, get_characters_count

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
  text = get_book_text("books/frankenstein.txt")
  num_words = get_num_words(text)
  characters_stats = get_characters_count(text)
  print(f"{num_words} words found in the document")
  print(f"{characters_stats}")
main()
