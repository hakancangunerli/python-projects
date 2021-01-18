from Bio import SeqIO #SeqIO es un in-out sequence alignement 
for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"): 
    print(seq_record.id) # l'systeme already knows l'fasta sistemi
    print(repr(seq_record.seq))
    print(len(seq_record))

# l' parsaj d'fasta is actually très facil, the only necesidad is Biopython. 

