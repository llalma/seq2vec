import fastq_reader

def fastq2fasta(path,f1,f2):
    #Read file
    sequences = fastq_reader.read(path+".fastq")



    for seq in sequences:
        f1.write(">"+seq.get("name")+"\n")
        seq = seq.get("sequence")+"\n"
        seq = seq.replace("N","")
        f1.write(seq)

        #For each sequence write the city name .
        f2.write(path[0-1-6:-1-3]+"\n")
    #end
#ends