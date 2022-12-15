"""
Script to convert embeddings generated with the bio_embeddings pipeline in the expected format
"""

import h5py
import numpy as np
import sys


def main():
    embeddings_in = "./protT5/output/uniprot_embeddings.h5"
    embeddings_out = 'embeddings_out_2.h5'

    with h5py.File(embeddings_in, 'r') as f_in:
        with h5py.File(embeddings_out, 'w') as f_out:
            for key, embedding in f_in.items():
                #origina_id = embedding.attrs['original_id']
                original_id = key.split('|')[1] #embedding.attrs['original_id']
                embedding = np.array(embedding)
                
                print('original_id', original_id)

                f_out.create_dataset(original_id, data=embedding)


main()
