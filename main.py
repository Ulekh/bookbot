import sys
from stats import (
  get_words_count,
  get_chars_num,
  get_sorted_list
 )

def get_boot_text(path_to_file):
  with open(path_to_file) as f:
    return f.read()

def print_report(book_path, num_words, chars_sorted_list):
  print("============ BOOKBOT ============\n"
  f"Analyzing book found at {book_path}")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print('--------- Character Count -------')
  for item in chars_sorted_list:
    if item['char'].isalpha():
      print(f"{item['char']}: {item['num']}")
  print('============= END ===============')


def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  path_to_file = sys.argv[1]
  text = get_boot_text(path_to_file)
  num_words = get_words_count(text)
  char_dict = get_chars_num(text)
  sorted_data = get_sorted_list(char_dict)
  print_report(path_to_file, num_words, sorted_data)
main()
