## NCBI Genome Downloader
This Python script enables bulk downloading of multiple file types using genomic assembly accession/GenBank accession from a single list.

## Description
The script reads a CSV file containing genome information, including Assembly Accession or GenBank Accession IDs. 
It utilizes the NCBI curl to download various genomic data files for genomes with valid accession IDs. Supported file formats include FASTA sequences, annotation files, and more.

## Prerequisites
Python 3.x
curl (usually pre-installed on Unix-based systems)

## Usage
1. Ensure your CSV file contains a column named "Assembly Accession" or "GenBank Accession" with accession IDs for the genomes.
2. Update the file path in the script to point to your input CSV file containing genome information:

   df = pd.read_csv("/path/to/your/csv/file.csv")
4. Run the script:
  python ncbi_genome_downloader.py

5. After execution, the script will download genomic data files for genomes with valid accession IDs. Files will be saved in the current directory with the accession ID as the filename.
6. A missing.txt file will be generated containing the names of genomes with missing or invalid accession IDs.

## Citation
If you are using the ncbi_genome_downloader.py script for your research, please consider citing it as follows: Sharma, R. (2024).ncbi_genome_downloader.py . Retrieved from https://github.com/BioinfoRhythm/ncbi_genome_downloader.py
