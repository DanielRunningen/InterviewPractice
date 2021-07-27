# This solution was developed in November of 2020
# I left this problem open for longer than I was likely working on it
#   and don't have an accurate time estimate

def isCryptSolution(crypt, solution):
   numbers = []
   solution = { item[0]: item[1] for item in solution }
   for word in crypt:
      if len(word) > 1 and solution[word[0]] == '0':
         return False
      num = ""
      for c in word:
         num = f"{num}{solution[c]}"
      numbers.append(int(num))
   return numbers[0] + numbers[1] == numbers[2]
