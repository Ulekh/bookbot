from stats import get_words_count, get_chars_num

def get_boot_text(path_to_file):
  with open(path_to_file) as f:
    return f.read()

def main():
  text = get_boot_text('books/frankenstein.txt')
  num_words = get_words_count(text)
  char_dict = get_chars_num(text)
  print(f"Found {num_words} total words")
  print(char_dict)
  
main()
