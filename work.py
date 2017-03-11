import sys
def main():
  for arg in sys.argv[1:]:
    print("We get file at",arg)
    filehandle = open(arg, 'r')
    
    for line in filehandle:
    
      try:
        try:
          print(line)
          text = line
        expect NameError:
          print("Except in ", line)
          text = line
      except EOFError:
        print("Except in EOF Error")
        break
      if not line:
        print("Not Line")
        continue
      for word in line.split(" "):
        print("Phase I lexer created with:", word)
        
        
        
        
        
        
if __name__ == '__main__':
  main()
