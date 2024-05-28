# Motif Finding Problem Solver

Python application that implements two algorithms for solving the motif finding problem: Brute Force algorithm and Median String Search algorithm. The application can read input sequences from a file or generate random sequences for analysis.

## Features

- Implements Brute Force Motif Search algorithm.
- Implements Median String Search algorithm.
- Allows user to input sequences from a file or generate random sequences.
- Calculates and displays the best motif and its score or Hamming distance.

## Requirements

- Python 3.7 or later

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sottohy/mMtif-Finding.git
   cd Motif-Finding

## Usage
1. Run the application:
   ```
   python motif_finding.py
   ```


2. Choose the input method:

   - Option 1: Read sequences from a file named rawDNA.txt.
   - Option 2: Generate random sequences.
  
3. Follow the prompts to enter the pattern length, number of sequences, and sequence length.

## Input File Format
If you choose to read input from a file, ensure the file rawDNA.txt follows this format:

- The first line should contain three integers separated by spaces: number of sequences (t), length of each sequence (n), and length of the pattern to be found (L).
- The subsequent lines should contain the DNA sequences.


## Code Overview

- brute_force_motif_search(dna, t, n, l): Implements the Brute Force Motif Search algorithm.
- hamming_dist(word, seq): Calculates the Hamming distance between a word and a sequence.
- MedianStringSearch(sequences, num_sequences, sequence_length, motif_length): Implements the Median String Search algorithm.
- The main() function prompts the user for input, reads sequences, and calls the appropriate functions to find motifs and display results.


## Output
![output](https://github.com/sottohy/Motif-Finding/assets/91037437/54354dc9-93ed-48fd-ba72-4ce9c928c746)
