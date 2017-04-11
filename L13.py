#Lab 13 Vasile Danciu, Josh Jones, Lavinia Uruc
#President Donald Trump is well outpacing his predecessor on the green, making his 16th visit to one of his eponymous golf courses since taking office as he marks the end of another weekend at his Florida getaway.
#Trump was spotted Sunday driving a golf cart and making a putt at his Trump International Golf Course -- the only sign of his activities at the facility since his handlers have declined to detail what he's doing inside the private establishment.
#source:http://www.cnn.com/2017/04/09/politics/trump-outpacing-obama-golf/index.html

words = []
showInformation("Python Mad Libs! Type 7 words to complete a news article!")
while (len(words) < 7):
  if not words:
    str = requestString("Enter an adjective")
    str = str[:1].upper() + str[1:]
    words.append(str)
  if (words[0]):
    str = requestString("Enter a noun")
    words.append(str)
  if (words[1]):
    str = requestString("Enter a strange location")
    words.append(str)
  if (words[2]):
    str = requestString("Enter a present participle verb (-ing)")
    words.append(str)
  if (words[3]):
    str = requestString("Enter a noun")
    words.append(str)
  if (words[4]):
    str = requestString("Enter a present participle verb (-ing)")
    words.append(str)
  if (words[5]):
    str = requestString("Enter a strange location")
    words.append(str)
    showInformation(words[0] + " Donald Trump is well outpacing his predecessor on the green, making his 16th visit to one of his eponymous golf courses since taking " + words[1] + " as he marks the end of another weekend at his " + words[2] + " getaway. Trump was spotted Sunday " + words[3] + " a golf cart and making a " + words[4] + " at his Trump International Golf Course -- the only sign of his activities at the facility since his handlers have declined to detail what he's " + words[5] + " inside the " + words[6] + ".")
  if (words[6]):
    showInformation("Excelent job! Python Mad Libs is complete!")