def solve(word):
  return len(word)==len(set(word.lower()))
  print(solve("Minakshi"))
  print(solve("Education"))
  print(solve("village"))
  print(solve("market"))