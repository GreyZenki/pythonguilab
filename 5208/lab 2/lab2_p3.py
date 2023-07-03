import random
import time
#defined function to generate random list of words
def random_sentence():
    #by line is used to open/read contents of the words file including splitting each line into an array format
    byLine = open('words.txt').read().splitlines()
    #wordCount is used to create the >= 7 words will be different each time
    wordCount = random.randint(1,7)
    #this generates the random words to fit the guidlines of 7 words or less
    randWords = random.sample(byLine,wordCount)
    #declared to return the generated words to the user
    combineSentence = ' '.join(randWords)
    return combineSentence
#this function is used for user input
def write_results(userSentence, timed):
    #first create an empty file to record results
    createFile = 'times.txt'
    #open the empty file and start filling in information
    with open(createFile, 'w+') as resultFile:
        #Used PEP8 format to fill in information starting with the legend 0:100 being the spacing of words and 1:50 being the spacing for time
        #to be more visually pleasing
        resultFile.write('{0:<100}{1:<50}\n'.format('Sentence', 'Time to Complete'))
        #for loop is used to run number of enteries
        for i in range(len(userSentence)):
            #following the same spacing to have neatness of the generated words and recorded time
            resultFile.write('{0:<100}{1:<50}\n'.format(userSentence[i], timed[i]))
            #this displays the average time of all entries
        resultFile.write('{0:<100}{1:<50}\n'.format('Average:',sum(timed)/len(timed)))
#Empty arrays for future use to recored all data from users completion
recordedTime = []
userSentence = []
#for loop is used to run 5 different tests
for completion in range(1,6):
    #initialize to random_sentence function
    combineSentence = random_sentence()
    #PEP8 format used to display the given sequence of words
    print("Please type the sentence: {}".format(combineSentence))
    #time starts when displayed
    timerStarted = time.time()
    #when the test is not completed yet
    while True:
        #user inputs entry
        response= input("")
        #if the users response is the same as the generated words then time stops
        if response ==combineSentence:
             timerStopped = time.time()
             break
        else:
            #if the users input does not match the generated words then they retry
            print("Entry does not match !")
    #total time is recorded by subtracting the start to end time displays for each trial
    recordedTime.append(timerStopped- timerStarted)
    #sends random words to array
    userSentence.append(combineSentence)
    #used for delay of sentences popping up
    time.sleep(1)
#calls function to start the test itself
write_results(userSentence,recordedTime)
