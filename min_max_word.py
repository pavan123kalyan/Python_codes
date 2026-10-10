s="This is a test string"
#Output : Minimum length word: a Maximum length word: string
words=s.split()
mini=words[0]
maxi=words[0]
for i in words:
  if len(mini)>len(i):
    mini=i
  if len(maxi)<len(i):
    maxi=i
print("Minimum length word:",mini,"Maximum length word:", maxi)