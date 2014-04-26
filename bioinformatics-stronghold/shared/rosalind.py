class Rosalind:

    def __init__(self):
        pass

    @staticmethod
    def readfasta(filename):
        f = open(filename, 'r')
        fastas = []
        fasta = None
        for line in f:
            if line.startswith(">"):
                if fasta != None:
                    fastas.append(fasta)

                fasta = Fasta()
                fasta.id = line
            else:
                fasta.dna += line.replace("\n", "")

        fastas.append(fasta)

        return fastas


class Fasta:
    id = ""
    dna = ""

    def __init__(self):
        pass

    def printfasta(self):
        print(self.id, self.dna)