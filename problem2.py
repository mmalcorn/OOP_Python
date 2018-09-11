from problem1 import magic

def magic_list(num):
  magic_list = []
  magic_range = range(2, num + 1)

  for i in magic_range:
    if magic(i):
      magic_list.append(i)
  print(magic_list)
  return magic_list

#### For testing, call the function ####
magic_list(100)