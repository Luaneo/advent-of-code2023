digits = list(range(10))
numbers = {string: index for index, string in enumerate([
  'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
], start=1)}

def first_number(s: str) -> int:
  digres = (float('inf'), None)
  for digit in digits:
    if (loc := s.find(str(digit))) != -1 and loc < digres[0]:
      digres = loc, digit
  numres = (float('inf'), None)
  for number in numbers:
    if (loc := s.find(number)) != -1 and loc < numres[0]:
      numres = loc, number
  if digres[0] < numres[0]:
    return digres[1]
  else:
    return numbers[numres[1]]

def last_number(s: str) -> int:
  digres = (-1, None)
  for digit in digits:
    if (loc := s.rfind(str(digit))) != -1 and loc > digres[0]:
      digres = loc, digit
  numres = (-1, None)
  for number in numbers:
    if (loc := s.rfind(number)) != -1 and loc > numres[0]:
      numres = loc, number
  if digres[0] > numres[0]:
    return digres[1]
  else:
    return numbers[numres[1]]


count = 0
for line in open('./data/1.txt'):
  first, last = first_number(line), last_number(line)
  count += 10 * first + last
print(count)
