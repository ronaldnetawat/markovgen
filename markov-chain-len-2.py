import random

def make_transitions(filename):
    #make transition dictionary using pairs of words as states
    # Initialize empty dictionary for word pair
    transitions = {}
    
    # read and convert text to lowercase
    with open(filename,'r') as file:
        text = file.read().lower()
    
    # Convert into list of words
    words = text.split()
    
    # Iterate through words to build pairs (need three words)
    # stop at length 2 because we need current pair and the next word
    for i in range(len(words) - 2):
        # create this word pair tuple as a state
        word_pair = (words[i], words[i + 1])
        # getting the word that follows this pair
        next_word = words[i + 2]
        
        # Add to the transitions dictionary
        if word_pair in transitions:
            transitions[word_pair].append(next_word)
        else:
            transitions[word_pair] = [next_word]
            
    # return transitions and first two words for possible starting
    return transitions, words[:2]

def generate_text(transitions, start_pair, num_words):
    # Generating text using pairs of words as states
    # Verifying that the  start pair exists
    if start_pair not in transitions:
        return "Starting word pair not found in text"
    
    # initialize the result with starting pair
    result = list(start_pair)
    current_pair = start_pair
    
    # generating remaining words
    for _ in range(num_words - 2):  # -2 as we start with two words
        if current_pair in transitions:
            # Choose random next word based on current pair
            next_word = random.choice(transitions[current_pair])
            result.append(next_word)
            # drop first word of pair and add new word
            current_pair = (current_pair[1], next_word)
        else:
            # at a dead end, jump to any random pair
            current_pair = random.choice(list(transitions.keys()))
            result.append(current_pair[1])
    
    return ' '.join(result)

def main():
    filename = input("Enter the path to your text file: ")
    
    # Make transitions and get initial pair
    transitions, first_pair = make_transitions(filename)
    
    while True:
        num_words = int(input("how many words should I generate? "))
        
        # Get two starting words from user
        word1 = input("Enter first word to start with: ").lower()
        word2 = input("Enter second word to start with: ").lower()
        start_pair = (word1, word2)
        
        generated_text = generate_text(transitions, start_pair, num_words)
        print("\nGenerated text:")
        print(generated_text)
        
        again = input("\nGenerate more text? (y/n): ").lower()
        if again != 'y':
            break


if __name__ == "__main__":
    main()