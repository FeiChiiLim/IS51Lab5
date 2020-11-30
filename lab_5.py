"""
The program is trying to translate a sentence capturedd by user input.
We first read in the text file textese.txt.
then from the text file, we create a list of strings from each lines in the text files.
Then, we create a dictionary with the list.
Once the text file has been read into memory, we close the file.

We then define a function for translating which envolves splitting the user input (sentence) into an
array of strings ("enjoy the excellent band tonight") ["enjoy", "the", "ecxcellent", "band", "tonight"]

Once we have the array of strings representing the user's input sentence, we
loop through each words, find the key matching the word and retunrs back the value tied to that word
in our dictionary.

After each word is translated, we then 
print out the translated sentence to the user.
"""


"""
main():
  set sentence = input()
  set dictionary = create_dictionary()
  translate(sentence, dictionary)

translate(sentence, dictionary):
  words = for each of the  word in the sentence
  for each words, translate the word
  print translated sentence to user

create_dictionary():
  read in textese.txt
  create list = each line from the file
  close the file
  create a dict off of the list
  return dict

main()
"""