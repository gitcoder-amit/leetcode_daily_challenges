class StringModifier:
  def __init__(self):
    self.n = 0

  def modify_str(self, original_string, n = 0):
    length = len(original_string)
    out = []
    # for i in range(0, n):
      
    for i in range(length):
      if i < n:
        out.append(original_string[i])
      else:
        new_i = ord(original_string[i]) - ord('a')
        new_chr = chr(ord('z') - new_i)
        out.append(new_chr)
    return ''.join(out)

str_m = StringModifier()
print(str_m.modify_str('rAjkumar', 0))