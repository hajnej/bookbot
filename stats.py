def get_num_words(text):
  """
  Counts the number of words in a given text string.

  Args:
    text (str): The input string to count words from.

  Returns:
    int: The number of words in the input text.
  """
  return len(text.split())

def get_characters_count(text):
  characters_stats = dict()
  for c in text.lower():
    if c in characters_stats:
      characters_stats[c] += 1
    else:
      characters_stats[c] = 1
  return characters_stats
