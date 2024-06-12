import pandas as pd
import os

df = pd.read_csv("/home/neo/Documents/Project_1/analysis_of_560_genomes/ncbi_genome_downloading/BVBRC_genome_working.csv")
# df.head()
missing = []

for i in range(len(df.index)):
    accession = df["Assembly Accession"][i]
    if isinstance(accession, str) and accession[:3] == 'GCA':
        print(accession)
        os.system(f"curl https://api.ncbi.nlm.nih.gov/datasets/v2alpha/genome/accession/{accession}/download?include_annotation_type=GENOME_FASTA,GENOME_GFF,RNA_FASTA,CDS_FASTA,PROT_FASTA,SEQUENCE_REPORT --output {accession}")
    else:
        missing.append(df['Genome Name'][i])
pd.to_csv("./missing.txt",header = None)
print("\a[Done...]")

