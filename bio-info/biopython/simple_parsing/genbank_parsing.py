from Bio import SeqIO
for seq_record in SeqIO.parse("ls_orchid.gbk", "genbank"): # l'genbank is already known tambien, 
     print(seq_record.id) # l'parametre premier is l'file in l'carpeta 
     print(repr(seq_record.seq))
     print(len(seq_record))

     # 	renvoyer to d'fasta_parsing.py dosyasi