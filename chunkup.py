import os
import numpy as np

cwd = os.getcwd()

chunk_size = 14
seq = 'test.txt'

#if given text file, run this function to remove newlines
def process_text_file(file):
    sequences = []

    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                sequences.append(np.array(list(line)))

    return sequences

#takes inputted sequence, iterates through it in chunks of defined size moving over by 1 each time
def chunked_up_list(seq, chunk_size):
    chunked_seqs = []

    with open(seq, 'r') as f:
        sequence = f.read()
        sequence = np.array(list(sequence))

    for i in range(0, len(sequence) - chunk_size + 1, 1): #starting at i = 0, going to len(sequence) - chunk_size + 1 to include last chunk, step size 1
        chunk = sequence[i:i + chunk_size] #ex index 0 to 15, then 1 to 16
        chunked_seqs.append(chunk)

    return chunked_seqs

#print(*process_text_file(seq), sep='\n')
#print(*chunked_up_list(seq, chunk_size), sep='\n')

#test case
# seq_2 = 'ACGTAGCTAGCTAGCGTACCGTAAAGCTCGACAGTAGGAATCGCT'
# chunk_size_2 = 5
# chunked_seqs_2 = []

# for i in range(0, len(seq_2) - chunk_size_2 + 1, 1):
    
#     chunk = seq_2[i:(i + chunk_size_2)]
#     chunked_seqs_2.append(chunk)

# #print(len(seq_2)-chunk_size_2)

# #print(*chunked_seqs_2, sep='\n')

# #print first and last chunk, number of iterations to check
# print(chunked_seqs_2[0])
# print(chunked_seqs_2[-1])

# print(len(chunked_seqs_2))
