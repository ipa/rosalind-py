from Bio.Seq import Seq

seq = Seq("CTTATCCTTTAGCGGATTCGGTCACGTGTCAAGACATCTTAGTGAAAAGCTTGTGACTGCACCGTGTACGCCTACATACGCGACAAGCAATCAGCTGGGCAGACGCAATTCGGCTACGGATGATTATGCAAGTGCCCGACGTTATTTCAGGGTGTTAGGCGGATGGTTCGCGTAGTGCGGGCTTTAATTGCAATGCGTCGTTGTAAAAGTTCCATCTAGCAACAACAGCTCTAGTGCCCACGCTCGCTCCGGAGCATCACATCCATCTTCGCGCCATTTCACTATTTGAGGGCAGTTAGGCCACCACTCCACTCAAAAGACATTCCGAGTTACTCCTAGGCAGGTAATTGTTGGCGGCCGAATATCACTTTGAGCCCCTTGACTCGCAAAGGTCACCCGCGGACTACGGCTGTAGGAAATGAGAGGCCCCGTTCAAAATGGACCGTTGCCTTCAGATTGCATAATATGGAATGCACTTGGGGCTCCTTCAGTGTAGCCAGCCTCTCTTTTCGCTTCCATACCTATGCCTCGTCGTAAGTGGGAGGATAGTCTCAGCACCATCACGAGAGCGGCACAGTAATAATGATTAAATTGAGAGTGTGTAGGGTTACTGCCCTCAGATTCAGATTCTTAGTGTAAACCAGTTAGGTCATCTTACCATAGATTATAGCCAGCTAGGCCTTGGGAACCACAGGTCGTTCAGATGGAGCTACCAAAAAATGTCTGGGTGCATCAATACCCATGCTTTAGTATATATCGTGCCCCATACGAGGTCTCTCTTCTTCGGTATATGAGTCCTTGAATGGCTCCTTATCGCATTTAATCACGTCTGCTCCCTGTAGCTACGCCCCAACGCCTACTATGCTATTTCCGTCGAGAACTAGATTGCCTGCTGAAGTAAACTCTGGCAGGATTGCGATGAACTTACACATCAATTTCGCGGTTTTATCGAGGTCCGCAAACTTTGTCTATGACGAGAACGCATTACTCCGCG")
a = seq.count("A")
c = seq.count("C")
g = seq.count("G")
t = seq.count("T")

print (a, c, g, t)