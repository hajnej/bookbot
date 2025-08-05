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
  """
  Counts the occurrences of each character in a given text string.

  The function converts the text to lowercase before counting.

  Args:
    text (str): The input string to count characters from.

  Returns:
    dict: A dictionary where keys are characters and values are their counts.
  """
  characters_stats = dict()
  for c in text.lower():
    if c in characters_stats:
      characters_stats[c] += 1
    else:
      characters_stats[c] = 1
  return characters_stats

def sort_on(items):
  """
  Helper function for sorting a list of dictionaries.

  Returns the value of the "num" key from a dictionary.

  Args:
    items (dict): The dictionary item to get the sort key from.

  Returns:
    int: The value of the "num" key.
  """
  return items["num"]

def sort_characters_by_frequency(characters_stats):
  """
  Sorts a dictionary of character counts by frequency in descending order.

  Args:
    characters_stats (dict): A dictionary of character counts.

  Returns:
    list: A list of dictionaries, each containing a "char" and its "num" (count),
          sorted from most frequent to least frequent.
  """
  characters_stats_list = []
  for k, v in characters_stats.items():
    characters_stats_list.append({"char": k, "num": v})
  characters_stats_list.sort(reverse=True, key=sort_on)
  return characters_stats_list
