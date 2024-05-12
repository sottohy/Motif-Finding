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
        max_numbers = []
        consensus = []

        # Iterate over each column index
        score = 0
        for i in range(l):
            # Get the maximum number and corresponding nucleotide in the current column
            max_in_column, nucleotide = max((profile_matrix[nucleotide][i], nucleotide) for nucleotide in profile_matrix)
            score += max_in_column
            max_numbers.append(max_in_column)
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

# Example usage
dna_sequences = [
    "cctgatagacgctatctggctatccaGgtacTtaggtcctctgtgcgaatctatgcgtttccaaccat",
    "agtactggtgtacatttgatCcAtacgtacaccggcaacctgaaacaaacgctcagaaccagaagtgc",
    "aaacgtTAgtgcaccctctttcttcgtggctctggccaacgagggctgatgtataagacgaaaatttt",
    "agcctccgatgtaagtcatagctgtaactattacctgccacccctattacatcttacgtCcAtataca",
    "ctgttatacaacgcgtcatggcggggtatgcgttttggtcgtcgtacgctcgatcgttaCcgtacgGc"
]
sequences = 5
nucleotides = 68
pattern_length = 8
brute_force_motif_search(dna_sequences, sequences, nucleotides, pattern_length)
