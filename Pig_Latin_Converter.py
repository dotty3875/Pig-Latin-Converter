#################################################################################################################################################################################
# STEP 1. OPENING THE FILE CONTENTS AND CONVERTING TO LIST

inputWords = open("inputWords.txt", "r") #opens file for reading
inputWordsList = (inputWords.read()).split() #turns the file contents into a list

#################################################################################################################################################################################
# STEP 2. FOR LOOP TO CONVERT TO PIG LATIN
wordsList = ""
vowelIndex = 0
vowels = ["a", "e", "i", "o", "u"]
for words in inputWordsList:
    for letter in words:
        if words[0] in vowels: #this if checks if the input word starts with a vowel
            newWord = words + "way\n"
            break
            #print(newWord) #for testing
        elif letter not in vowels: 
                newWord = words + "ay\n"
            #print(newWord) #for testing
        else:  #this else covers the final criteria where it needs to find the vowel and then shuffle the first part of the word (from start till the first vowel) to the end of the word, then add ay
            vowelIndex = words.find(letter) 
            addEnd = words[0:vowelIndex]
            newWord = words[vowelIndex:] + addEnd + "ay\n" 
            #print(newWord) #for testing
            break
    wordsList += newWord
    #print(newWord) #for testing 
#print(wordsList) #for testing

#################################################################################################################################################################################
# STEP 3. WRITE TO FILE AND FINISH

#opens output text file to recieve the pig latin words list
output = open("outputWords.txt", "w")
output.write(wordsList.strip()) #the .strip() removes giant empty spaces. need this or else the final line in the text document will be an empty line caused by a final \n
output.close() #closing it to re-open it so that it goes from "write" to "read" so that it can be printed
output = open("outputWords.txt", "r")
print(output.read()) #prints the contents of output text file

#closes the two opened files and quits program
output.close() 
inputWords.close()
quit()