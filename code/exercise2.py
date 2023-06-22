# WRITE YOUR CODE HERE
def move_to_bottom(dict, key):
  if key not in dict:
    return 'The key is not in the dictionary'
  else:
    value = dict.pop(key)
    dict[key] = value
  return dict 
# test code below

if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
}

#move_to_bottom(example_dict, 4)
#print(example_dict)
