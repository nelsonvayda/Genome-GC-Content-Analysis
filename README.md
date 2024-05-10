# **Genome GC Content Analysis Program**

## Required Python and Packages
Python 3.9\
matplotlib

## Description
This program is used to create a visualization of the GC content of k-mers of the desired length across a given sequence.
The input is fasta files and the output is a PDF of a graph showing the GC content of each k-mer based on the position in the sequence.
I will be using it to quickly visualize changes in GC content of the genomes of phage I isolate to look for areas of potential recent recombination, denoted by major shifts in GC content. I'm honestly not sure how useful this will be in its current form, but I will tweak it once I am closer to the point in my research where I need to use it, I just didn't have the time for that quite yet.

## Usage
The program can be used directly in the command line using the following command:
> python GCContentScript.py **(path to fasta file/s)** -k **(desired k-mer length)**

I recommend using a value between 1,000 and 10,000 for the k-mer length, lower values will result in difficult to read graphs, and higher values may take a long time to compute.
I have included a folder called TestData that includes an example output (using 50,000-mers because it looks nice) and a fasta file with a shorter sequence which works nicer but is less realistic to my data.
