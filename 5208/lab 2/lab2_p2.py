import random

#opens and reads the example file
with open ('example.txt', 'r') as rf:
    read_file = rf.read() 

#defines the scramble function
def scramble(words):
    
    #creates two empty strings
    result = ''
    sub_word = ''
    
    #scramble function
    for char in words + '':
        if char.isalpha():
            sub_word += char
        else:
            if len(sub_word) > 3:
                result += sub_word[0]
                result += ''.join(random.sample(sub_word[1:-1], len(sub_word)-2))
                result += sub_word[-1]
            else:
                result += sub_word
            sub_word = '' 
               
            result += char
            
    return result[:-1]

#defines the main function
def main():
    
    #scrambles the text from the example file and sets it as the variable sentence
    sentence = scramble(read_file)
    
    #prints 5 of the scramnled sentences onto the console
    for number in range(5):
        print(sentence)
    
    #creates the scrambled.txt file and fills it with 20 of the scrambled sentences
    with open('scrambled.txt', 'w') as wf:
        for number in range(20):    
            wf.writelines(sentence)
           
            
if __name__ == '__main__':
    main()    

    
