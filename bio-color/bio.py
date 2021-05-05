# adenine is green, thymine is red, cytosine is yellowish  and guanine is blue. 

from colorama import Fore, Back, Style
file_name = input("put the filename with extension: ")

    
fasta = open(file_name)


fasta = fasta.read()

print('startingggg now! ')


for i in range(len(fasta)):
  if fasta[i] == "a" or fasta[i] == "A" :
      print(Fore.GREEN  + 'a', end ="")
      print(Style.RESET_ALL, end ="")
  elif fasta[i] == "t" or fasta[i] == "T" :
      print(Fore.RED + 't', end ="" )
      print(Style.RESET_ALL, end ="")
  elif fasta[i] == "c" or fasta[i] == "C" :
      print(Fore.YELLOW + 'c', end ="")
      print(Style.RESET_ALL, end ="")
  elif fasta[i] == "g" or fasta[i] == "G" :
      print(Fore.BLUE + 'g', end ="")
      print(Style.RESET_ALL, end ="")
  else:
      print("UNIDENTIFIED")

print(Style.RESET_ALL)
print('sequence ended woohoo!')
