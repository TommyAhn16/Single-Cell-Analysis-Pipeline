# Single-Cell-Analysis

## Docker Images

### Cell Ranger

- Docker hub URI: chungwookahn/cellranger5.0.1:0.1
- Version: 5.0.1
- [10x genomics reference page](https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/5.0/what-is-cell-ranger)
- Main command: `cellranger count`
- Takes FASTQ files and performs alignment, filtering, barcode counting, and UMI counting.
- It uses the Chromium cellular barcodes to generate feature-barcode matrices, determine clusters, and perform gene expression analysis

### cellSNP

- Docker hub URI: chungwookahn/cell_snp:0.1.1
- Version: 0.3.2
- [source code](https://github.com/single-cell-genetics/cellSNP)
- pileup whole chromosome(s) for a single BAM/SAM file

### vireoSNP

- Docker hub URI: chungwookahn/vireo_snp:0.1
- Version: 0.5.0
- [vireoSNP documentation reference](https://vireosnp.readthedocs.io/en/latest/index.html)
- Vireo is primarily designed for demultiplexing cells into donors by modelling of expressed alleles

### Souporcell

- Docker hub URI: chungwookahn/souporcell:0.1
- Anaconda Installers version: Python 3.8, Anaconda3-2021.05-Linux-x86_64
- Fasta referance: cellranger 5.0.1 reference
- minimap2: 2.7-r654
- vartrix: 1.1.22
- freebayes: 1.3.1-dirty
- cargo: 1.53.0 (4369396ce 2021-04-27)
