def get_words_count(text):
  num_words = len(text.split())
  return num_words

def get_chars_num(text):
  dict = {}
  for letter in text:
    lowercase_l = letter.lower()
    if lowercase_l in dict:
      dict[lowercase_l] += 1
    else:
      dict[lowercase_l] = 1
  return dict