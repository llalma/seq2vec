from os import listdir
from os.path import isfile, join

from fastq2fasta import fastq2fasta


if __name__ == "__main__":

    ###########################################
    #Convert fastq to fasta files
    ###########################################

    #Get lsit of fastq files
    path = "data/fastq/"
    onlyfiles = [f[0:7] for f in listdir(path) if isfile(join(path, f))]

    #Open file to write fasta file
    fasta = open("data/compiled.fasta", "w")
    cities = open("data/compiled_cities.txt", "w")

    # #Convert all fastq files to a single fasta file
    for f in onlyfiles:
        print("Converting "+f)
        fastq2fasta(path+f,fasta,cities)
    #end

    fasta.close()

    ###########################################
    #Run script
    ###########################################

#end