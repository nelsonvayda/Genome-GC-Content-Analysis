#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
import matplotlib.pyplot as plt
import argparse

def read_fasta(file_path):
    # Reads FASTA file and returns the sequence
    with open(file_path, 'r') as file:
        sequence = ''
        for line in file:
            if not line.startswith('>'):
                sequence += line.strip()
    return sequence

def generate_kmers(sequence, k):
    # Generates k-mers for the sequence
    return [sequence[i:i+k] for i in range(len(sequence) - k + 1)]

def gc_content(kmer):
    # Calculates the GC content of the k-mers
    return (kmer.count('G') + kmer.count('C')) / len(kmer) * 100

def process_fasta_files(directory, k):
    # Processes all FASTA files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith('.fasta'):
            file_path = os.path.join(directory, filename)
            sequence = read_fasta(file_path)
            kmers = generate_kmers(sequence, k)
            gc_contents = [gc_content(kmer) for kmer in kmers]
            #print(f"GC contents for {filename}: {gc_contents}")
            #print function used for testing but not kept in to limit output

            # Plots the GC content using matplot
            plt.figure(figsize=(10, 5))
            plt.plot(gc_contents, label='GC Content')
            plt.title(f'GC Content along the Genome for {filename}')
            plt.xlabel('Position of k-mer in genome')
            plt.ylabel('GC Content (%)')
            plt.grid(True)
            plt.legend()

            # Saves the plot to a PDF file
            output_file = os.path.splitext(filename)[0] + '_gc_content.pdf'
            plt.savefig(output_file)
            plt.close()  # Closes the plot to free memory

#Code used for testing in jupyter notebook
#current_directory = '.'  # Current directory
#process_fasta_files(current_directory)


def main():
    parser = argparse.ArgumentParser(description="Process FASTA files to plot GC content of k-mers.")
    parser.add_argument('directory', type=str, help='Directory containing FASTA files')
    parser.add_argument('-k', type=int, default=21, help='Length of the k-mers (default: 21)')
    args = parser.parse_args()

    process_fasta_files(args.directory, args.k)

if __name__ == "__main__":
    main()


# In[ ]:




