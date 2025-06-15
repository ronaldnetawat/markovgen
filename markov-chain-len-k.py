import random

def make_transitions(filename, k):
    #Make transition dictionary using k words as states"""
    # Initializing transitions dictionary
    transitions = {}
    
    # open and Read the file
    with open(filename, 'r') as file:
        text = file.read().lower()
    
    words = text.split()
    
    # make transitions dictionary using k-word sequences
    # need k+1 words at a time (k words for state and 1 for the next word)
    for i in range(len(words) - k):
        # Create tuple of k words as  the current state
        state = tuple(words[i:i + k])
        # Getting the word that follows this sequence
        next_word = words[i + k]
        
        # Add to the dict
        if state in transitions:
            transitions[state].append(next_word)
        else:
            transitions[state] = [next_word]
            
    # Return the dict and first k words
    return transitions, words[:k]

def generate_text(transitions, start_state, num_words):
    #Generate text using k-word states
    # Get k from length of start_state
    k = len(start_state)
    
    # Verifying that the start state exists
    if start_state not in transitions:
        return "Starting state not found in text"
    
    # Initialize result with starting state
    result = list(start_state)
    current_state = start_state
    
    #generate remaining words
    for _ in range(num_words - k):  # -k because we start with k words
        if current_state in transitions:
            #choose random next word based on current k-word state
            next_word = random.choice(transitions[current_state])
            result.append(next_word)
            # update: drop first word, add new word
            current_state = tuple(list(current_state[1:]) + [next_word])
        else:
            # handling the ends
            current_state = random.choice(list(transitions.keys()))
            result.append(current_state[-1])
    
    return ' '.join(result)

def get_starting_words(k):
    #Helper function to get k starting words from user
    starting_words = []
    for i in range(k):
        word = input(f"Enter word {i+1} to start with: ").lower()
        starting_words.append(word)
    return tuple(starting_words)

def main():
    filename = input("Enter the path to your text file: ")
    
    # gettink k
    k = int(input("Enter the length k for the Markov chain: "))
    
    # Make transitions with the given k
    transitions, first_k_words = make_transitions(filename, k)
    
    while True:
        num_words = int(input("How many words should I generate? "))
        
        # Get k starting words
        start_state = get_starting_words(k)
        
        generated_text = generate_text(transitions, start_state, num_words)
        print("\nGenerated text:")
        print(generated_text)
        
        again = input("\nGenerate more text? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()