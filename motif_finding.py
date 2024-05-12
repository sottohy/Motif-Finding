import time
import random
import string

def brute_force_motif_search(dna, t, n, l):
    bestScore = 0
    bestMotif = None

    s = [0] * t  # Initialize starting indices to 0 for all sequences
    total_iterations = (n - l + 1) ** t  # Calculate total iterations based on the length of the sequences and the motif length

    for _ in range(total_iterations):
        current_motifs = []
        profile_matrix = {'A': [0]*l, 'C': [0]*l, 'G': [0]*l, 'T': [0]*l}  # Initialize profile matrix with empty lists
        for i in range(t):
            current_sequence = dna[i]
            start = s[i]  # Start index
            current_motifs.append(current_sequence[start:start + l])

        # profile matrix
        for j in range(l):
            counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
            for motif in current_motifs:
                counts[motif[j].upper()] += 1 # increment the letter found
            for nucleotide in profile_matrix: # append the counts found
                profile_matrix[nucleotide][j] = counts[nucleotide]

        # consensus
        consensus = []

        # Iterate over each column index
        score = 0
        for i in range(l):
            # Get the maximum number and corresponding nucleotide in the current column
            max_in_column, nucleotide = max((profile_matrix[nucleotide][i], nucleotide) for nucleotide in profile_matrix)
            score += max_in_column
            consensus.append(nucleotide)

        # construct consensus string with correct case
        consensus_str = ''.join([consensus[i].upper() if current_motifs[0][i].isupper() else consensus[i].lower() for i in range(l)])

        # calculate score
        if score > bestScore:
            bestScore = score
            bestMotif = consensus_str

        j = t - 1 # j is the last dna sequence in the list
        while j >= 0: # a loop that iterates over each index in the s array, starting from the last one and moving towards the first one
            if s[j] < n - l: # check that the starting index is less than the maximum possible starting index
                s[j] += 1 # increment start index
                break
            else: # it means we have reached the maximum possible starting index for the current dna sequence
                s[j] = 0 # reset start index to zero
                j -= 1 # move to the next dna sequence

    print("Motif:", bestMotif)
    print("Score:", bestScore)


def hamming_dist(word, seq):
    minDist = float('inf')

    for i in range(len(seq) - len(word) + 1):  #iterates over seq as long as word can fit in, if word len=4 and seq len=9 , then iterates 6 times
        pattern = seq[i:i+len(word)]   #get the pattern from the seq with the same length as word
        mismatch = 0

        for j in range(len(word)):
            if word[j] != pattern[j]:  #compare
                mismatch += 1   #if not equal increment mismatch

        minDist = min(minDist, mismatch)
    return minDist


def MedianStringSearch(sequences, num_sequences, sequence_length, motif_length):
    best_motif = None
    best_distance = float('inf')

    for i in range(sequence_length - motif_length + 1):  #iterate on all possible sequences of the same motif lenghts
        motif = sequences[0][i:i+motif_length]  #extract 1st seq starting from index i to motif length (substring of length motif)

        total_distance = sum(hamming_dist(motif, seq) for seq in sequences)   #calc distance from cuurent motif and each seq in the list

         #update dist and best motif found
        if total_distance < best_distance:
            best_distance = total_distance
            best_motif = motif

    print("Motif:", best_motif)
    print("Hamming Distance:", best_distance)



print("Motif Finding Problem Solver\n")
print("Choose input method: \n1. Read from file (rawDNA.txt) \n2. Generate random sequences \n")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("\nReading input from file...")

    file_path = 'rawDNA.txt'
    file = open(file_path, 'r')
    file_lines = file.readlines()

    # Remove \n
    file_lines = [line.strip() for line in file_lines]

    # Reading t, n, l from the first line
    sequences, nucleotides, pattern_length = file_lines[0].split()
    sequences = int(sequences)
    nucleotides = int(nucleotides)
    pattern_length = int(pattern_length)

    # Remove the first line
    DNA = file_lines[1:]

elif choice == 2:
    pattern_length = int(input("Enter the length of the pattern to be found (L): "))
    sequences = int(input("Enter the number of sequences (t): "))
    nucleotides = int(input("Enter the length of each sequence (n): "))
    print("\nGenerating random sequences...")
    time.sleep(1)

    DNA = []
    for i in range(sequences):
      characters = 'ACGT'
      random_string = ''.join(random.choice(characters) for _ in range(nucleotides))
      print("Sequence", i+1, ":", random_string)
      DNA.append(random_string)


print("\nBrute Force Algorithm: ")
brute_force_motif_search(DNA, sequences, nucleotides, pattern_length)
print("\nMedian String Algorithm: ")
MedianStringSearch(DNA, sequences, nucleotides, pattern_length)

