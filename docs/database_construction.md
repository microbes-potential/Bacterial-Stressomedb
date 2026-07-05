# Database Construction and Curation

Bacterial StressomeDB was developed as a curated repository of bacterial stress response systems by integrating information from UniProtKB, KEGG Orthology, and BacFITBase.

## Data sources

Stress response proteins and annotations were collected from:

- UniProtKB reviewed bacterial protein entries
- KEGG Orthology functional annotations
- BacFITBase infection fitness evidence
- NCBI and GenBank sequence-linked identifiers where available

## Curation workflow

Records were standardized across source databases by harmonizing gene symbols, protein names, organism names, taxonomic identifiers, functional descriptions, evidence sources, sequence information, and literature references.

## Sequence dereplication

Protein sequences were dereplicated at 100% amino acid sequence identity. Identical protein sequences were represented by a single reference sequence, whereas homologous proteins with sequence variation were retained to preserve taxonomic and functional diversity.

The release is compatible with the following CD-HIT workflow for exact protein sequence dereplication:

```bash
cd-hit \
-i StressomeDB_all_proteins.fasta \
-o StressomeDB_nonredundant.fasta \
-c 1.00 \
-n 5 \
-d 0 \
-M 0 \
-T 0
```

Parameter interpretation:

- `-c 1.00`: 100% amino acid sequence identity
- `-n 5`: word size appropriate for high identity protein clustering
- `-d 0`: retain complete FASTA headers
- `-M 0`: no memory limit
- `-T 0`: use all available CPU threads

## Category organization

Curated stress category labels were organized into nine higher order groups for comparative analysis:

1. Oxidative stress
2. Metal homeostasis and resistance
3. Acid adaptation
4. Envelope stress
5. Heat shock
6. Osmotic stress
7. Detoxification systems
8. Multidrug and biocide efflux
9. Global stress regulation

## Official release format

The official downloadable release is distributed as a single SQLite database. Separate CSV and FASTA files are not included because the SQLite file stores both curated metadata and protein sequences.
