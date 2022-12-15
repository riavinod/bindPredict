# bindEmbed21 fixed bugs and plotting (adapted from the rost lab, see https://github.com/Rostlab/bindPredict for full documentation)

bindEmbed21 is a method to predict whether a residue in a protein is binding to metal ions, nucleic acids (DNA or RNA), or small molecules. Towards this end, bindEmbed21 combines homology-based inference and Machine Learning. Homology-based inference is executed using MMseqs2 [1]. For the Machine Learning method, bindEmbed21DL uses ProtT5 embeddings [2] as input to a 2-layer CNN. Since bindEmbed21 is based on single sequences, it can easily be applied to any protein sequence.

## Usage

`run_bindEmbed21DL.py` shows an example how to generate binding residue predictions using the Machine Learning part of bindEmbed21 (bindEmbed21DL)

`run_bindEmbed21HBI.py` shows an example how to generate bidning residue predictions using the homology-inference part of bindEmbed21 (bindEmbed21HBI)

`run_bindEmbed21.py` combines ML and HBI into the final method bindEmbed21

`develop_bindEmbed21DL.py` provides the code to reproduce the bindEmbed21DL development (hyperparameter optimization, training, performance assessment on the test set).

All needed files and paths can be set in `config.py` (marked as TODOs).

## Data

wget all 3:

* Pre-computed big80 DB: [ftp://rostlab.org/bindEmbed21/profile_db.tar.gz](ftp://rostlab.org/bindEmbed21/profile_db.tar.gz)
* Pre-computed lookup DB: [ftp://rostlab.org/bindEmbed21/lookup_db.tar.gz](ftp://rostlab.org/bindEmbed21/lookup_db.tar.gz)
* FASTA for lookup DB: [ftp://rostlab.org/bindEmbed21/lookup.fasta](ftp://rostlab.org/bindEmbed21/lookup.fasta)
* Uniprot per residue embeddings [https://ftp.ebi.ac.uk/pub/contrib/UniProt/embeddings/current_release/UP000005640_9606/per-residue.h5]

## Computing Predictions

* Download a Uniprot multifasta (or use your own)
* Fill in [seq_path] in get_embeddings.py with your fasta
* Use process_fasta.py to to correctly format sequence headers
* Fill in TODOs in config.py (paths to data and where to make store predictions)
* Run any of [run_bindEmbed21DL.py, run_bindEmbed21HBI.py, develop_bindEmbed21DL.py]
* Use check_h5.py to look at the keys of any h5 file

## Availability

bindEmbed21 is also part of [the bio_embeddings pipeline](https://github.com/sacdallago/bio_embeddings) [4]. Also, predictions of bindEmbed21DL can also be run and visualized on a predicted 3D structure using [LambdaPP](https://embed.predictprotein.org/) [5].  

## Requirements

bindEmbed21 is written in Python3. In order to execute bindEmbed21, Python3 has to be installed locally. Additionally, the following Python packages have to be installed:
- numpy
- scikit-learn
- torch
- pandas
- h5py

To be able to run homology-based inference, MMseqs2 has to be locally installed. Otherwise, it is also possible to only run the Machine Learning part of bindEmbed21 (bindEmbed21DL).

## Cite

In case, you are using this method and find it helpful, we would appreciate if you could cite the following publication:

Littmann M, Heinzinger M, Dallago C, Weissenow K, Rost B. Protein embeddings and deep learning predict binding residues for various ligand classes. *Sci Rep* **11**, 23916 (2021). https://doi.org/10.1038/s41598-021-03431-4


## References
[1] Steinegger M, Söding J (2017). MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nat Biotechnol 35.

[2] Elnaggar A, Heinzinger M, Dallago C, Rihawi G, Wang Y, Jones L, Gibbs T, Feher T, Angerer C, Bhowmik D, Rost B (2021). ProtTrans: towards cracking the language of life's code through self-supervised deep learning and high performance computing. bioRxiv.

[3] Yang J, Roy A, Zhang Y (2013). BioLip: a semi-manually curated database for biologically relevant ligand-protein interactions. Nucleic Acids Research, 41.

[4] Dallago C, Schütze K, Heinzinger M, Olenyi T, Littmann M, Lu AX, Yang KK, Min S, Yoon S, Morton JT, & Rost B (2021). Learned embeddings from deep learning to visualize and predict protein sets. Current Protocols, 1, e113. doi: 10.1002/cpz1.113

[5] Olenyi T, Marquet C, Heinzinger M, Kröger B, Nikolova T, Bernhofer M, Sändig P, Schütze K, Littmann M, Mirdita M, Steinegger M, Dallago C, & Rost B (2022). LambdaPP: Fast and accessible protein-specific phenotype predictions. bioRxiv
