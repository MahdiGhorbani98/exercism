DNA_TO_RNA = {"G": "C", "C": "G", "T": "A", "A": "U"}

def to_rna(dna_strand):
    list = [DNA_TO_RNA[letter] for letter in dna_strand]
    final_list = ''.join(list)
    return final_list