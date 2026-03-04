import pandas as pd
import numpy as np
from scipy.spatial.distance import hamming
from chunkup import chunked_up_list, process_text_file

ref_seq = 'ecoli.fasta'
example_seq = '14test.txt'
chunk_size = 14
score_list = []

ref_name = ref_seq.split('.', 1)[0] #takes name of ref seq, removes .fasta; will print later to show title of dataframe
data_file = ref_name + '_vs_' + example_seq.split('.', 1)[0] + '_hamming_data.txt' #name of output file based on names of ref and example seqs

#sees if example seq is a .txt and if it has been processed already

ref_chunk_list = chunked_up_list(ref_seq, chunk_size)
seq_chunk_list = process_text_file(example_seq)
#seq_chunk_list = chunked_up_list(example_seq, chunk_size)


#print(ref_chunk_list)
 
for seq_chunk in seq_chunk_list:
    for ref_chunk in ref_chunk_list:
        score = hamming(ref_chunk, seq_chunk) * len(ref_chunk) #multiply by len to get actual hamming dist number

        score_list.append(score)

#turning arrays back into string for dataframe
ref_chunk_strings = []
seq_chunk_strings = []

for ref_chunk in ref_chunk_list:
     ref_chunk = ''.join(ref_chunk) 
     ref_chunk_strings.append(ref_chunk)

for seq_chunk in seq_chunk_list:
     seq_chunk = ''.join(seq_chunk) 
     seq_chunk_strings.append(seq_chunk)


hamming_data = pd.DataFrame(index=seq_chunk_strings, columns=ref_chunk_strings) #need rows to be chunks of other sequence

#turning list of scores into matrix based on size of ref chunks and seq chunks to put into dataframe
score_matrix = np.array(score_list).reshape(len(seq_chunk_strings), len(ref_chunk_strings))
#print(score_matrix)

hamming_data = pd.DataFrame(score_matrix, index=seq_chunk_strings, columns=ref_chunk_strings)
#print(hamming_data)

hamming_data.to_csv(data_file, sep='\t')

#adding name of reference sequence as title of tsv
with open(data_file, 'r') as f:
     content = f.read()
with open(data_file, 'w') as f:
     f.write('Reference Sequence: ' + ref_name + '\n' + content)