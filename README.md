# Motif-Finding
### Motif finding problem using Brute Force and Median String Search algorithms

The motif finding problem is a challenge in bioinformatics that involves finding a common pattern (motif) shared by a group of DNA, RNA, or protein sequences. The output is the motif itself, which is a short sequence of nucleotides or amino acids that appears in each of the input sequences. 
The code allows for two options: read sequneces from file or generate random sequences.  

## Brute Force Algorithm
This function implements a brute-force approach to finding the best motif among a set of DNA sequences. It iterates through all possible starting positions for each sequence and builds a profile matrix to calculate a consensus motif then calculates a score. The motif is updated in each iteration if a consensus of a higher score is found.

## Median String Search Algorithm
This function implements the median string algorithm to find the motif with the minimum total Hamming distance to all sequences. The hammming_dist() function is implemented and calculates the Hamming distance between a given word (motif) and a sequence. Hamming distance is the number of positions at which the corresponding characters differ(mismatches). The Median String Search function iterates through all possible motifs of a given length and calculates the total distance for each motif, updating the best motif if a lower distance is found.

#### The output is as follows
![output](https://github.com/sottohy/Motif-Finding/assets/91037437/54354dc9-93ed-48fd-ba72-4ce9c928c746)
