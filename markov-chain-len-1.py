import random

def make_transitions(filename):
    # Make transition dictionary from text file where each word maps to its possible next words
    # Initialize empty dictionary
    transitions = {}
    
    # Open and read the entire file, convert to lowercase
    with open(filename, 'r') as file:
        text = file.read().lower()
    
    # Convert text into list of words
    words = text.split()
    
    # Iterate through words (except last one since it has no next word)
    for i in range(len(words) - 1):
        current_word = words[i]   # current word becomes the state
        next_word = words[i + 1] # next word is what we might transition to
        
        # if we've seen this word before, append the next word to its list
        if current_word in transitions:
            transitions[current_word].append(next_word)
        # if it's a new word, create a new list with the next word
        else:
            transitions[current_word] = [next_word]
            
    return transitions

def generate_text(transitions, start_word, num_words):
    #generate text by walking through the markov chain
    # check if starting word exists in our dict
    if start_word not in transitions:
        return "Starting word not found in text"
    
    # initialize result list with starting word
    result = [start_word]
    current_word = start_word
    
    # Generate remaining words
    for _ in range(num_words - 1):
        if current_word in transitions:
            # Randomly select next word from possible transitions
            current_word = random.choice(transitions[current_word])
            result.append(current_word)
        else:
            #if we reach a dead end, randomly go to a new word
            current_word = random.choice(list(transitions.keys()))
            result.append(current_word)
    
    #joining all words with spaces
    return ' '.join(result)

def main():
    # Getting filename from user
    filename = input("Enter the path to your text file: ")
    
    # creating transition dictionary from file
    transitions = make_transitions(filename)
    
    while True:
        # Get parameters for text generation
        num_words = int(input("How many words should I generate? "))
        start_word = input("Enter a word to start with: ").lower()
        
        # Generate and display the text
        generated_text = generate_text(transitions, start_word, num_words)
        print("\nGenerated text:")
        print(generated_text)
        
        #checking if the user wants to go again
        again = input("\nGenerate more text? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()