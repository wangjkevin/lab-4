def dna(s):
    n = [0, 0, 0, 0]
    for nucleotide in s:
        if nucleotide == "A":
            n[0] += 1
        elif nucleotide == "C":
            n[1] += 1
        elif nucleotide == "G":
            n[2] += 1
        elif nucleotide == "T":
            n[3] += 1
    return " ".join([str(x) for x in n])

print(dna("GACGCTCAATTTGCATTAATTAGGCACCGAGTATCGCGATGGCGAGCGGCTAGAGGTACAACGTGATCACAGTGGTCTGATTTACTATCTGGACTGCAATCCTGCACCTCGACAGATGTGTCGATCCAGCTGTGCGCACCGAACGCAACGGGCAACTGTTGAGCATCCCATGGTCCTCCTTGCGCTCTGCCTAACCCCCGGATATGAACACATGATTTCCATACGAAGTCGTCGATAGGTCTGAGATCCATCTCTCTCAGAACACTGATACCGGAATCGCGATTACCAGTGTATGTCGGGTCCTCGAGACTCGACTTGTGAACCCGGTTCTTTACGGGCAGTAAACCCCCCCCCGAGGTCTGAGGGCCCAGGCTGATATGTGTGCTCACGCATGGGTTCCCTAAAATGAGCGAGCTTCCGAGGTCCTGCGGACCAACCGTAGAACTCCACGTTCAGTTCACTGATAGTCTGGAGGATGTTTTTTTACTTACGTGGGGCGCCCGGCAGAATTTCTCTCGCATATTTGATGCATACCCGGGTGTCGCTGTGGGACCGCCCTTAATTTTAGCAAATTTTTGACCGAGACGGTCGGGGTAGGATTACGTGTCGAGACTTCCGACTTGGTTTAAGATCTGGGCAGGTGCACGATTCCAGCATCGAAAGGGGCCGCCTCAAGCAGTGCCTCGACAATCAGTATGAAATTTCATTGACCCTAACACAAGTGATGATCCGCCTCAGGTGACGTGAAGATGATTCTGATTGGTATGTGGGTCTGACCTCATTGTTCGCGGTTCGCTCAGCTGGTGCCGGATGCCGTATATCCCGTATTAATGCGGCCGGGATTCCTGCACTCTGATGTTCGCAGTGGTCGTATACTCATCCG"))