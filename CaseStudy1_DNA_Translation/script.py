def read_seq(inputFile):
    with open(inputFile, 'r') as f:
        seq = f.read()
    seq = seq.replace('\n', "")
    seq = seq.replace('\r', "")

    return seq

def dnaSequence(start, end, dna):
    return dna[start-1:end]

protein = read_seq("protein.txt")
dna = read_seq("dna.txt")
dna = dnaSequence(21,935,dna) #Eliminating the stop codon from the last part

def translate(seq):
    """Translate a string containing a nucleotide sequence into a string containing the corresponding sequence of amino acids . Nucleotides are translated in triplets using the table dictionary; each amino acid 4 is encoded with a string of length 1. """
    
    table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
    }

    # Check if the length of the table is divisible by three
    seqLen = len(seq)
    dnaSeq = ""
    if(seqLen % 3 == 0):
        for i in range(0, seqLen, 3):
            dna = seq[i:i+3]
            dnaSeq += table[dna]
    return dnaSeq

print(str(translate(dna)) == str(protein))
