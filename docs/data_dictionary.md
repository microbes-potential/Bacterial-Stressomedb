# Data Dictionary

## `stressome_records`

Main curated metadata table.

| Column | Description |
|---|---|
| `stressome_id` | Unique Bacterial StressomeDB record identifier |
| `gene_symbol_primary` | Standardized primary gene symbol where available |
| `gene_symbol` | Gene symbol or gene name field from source records |
| `synonyms` | Alternative gene names or synonyms |
| `protein_name` | Protein name or functional product description |
| `description` | Curated functional description |
| `stress_category` | Curated stress response category label |
| `stress_subcategory` | More specific stress response mechanism where available |
| `organism` | Source organism or bacterial taxon |
| `taxon_id` | NCBI taxonomy identifier where available |
| `uniprot_accession` | UniProt accession where available |
| `evidence_sources` | Source databases supporting the record |
| `evidence_levels` | Evidence level assignments |
| `evidence_types` | Type of supporting evidence |
| `source_tables` | Original source table or source resource |
| `source_count` | Number of supporting sources |
| `sequence_length` | Protein sequence length where available |
| `sequence_md5` | MD5 checksum of the amino acid sequence |
| `has_sequence` | Indicates whether sequence information is available |

## `protein_sequences`

Sequence nonredundant protein reference set.

| Column | Description |
|---|---|
| `stressome_id` | Representative StressomeDB ID |
| `fasta_header` | FASTA header used for the reference sequence |
| `sequence` | Amino acid sequence |
| `sequence_length` | Protein length in amino acids |
| `sequence_md5` | MD5 checksum used for sequence level matching |

## `record_categories`

Exploded stress category assignments.

| Column | Description |
|---|---|
| `stressome_id` | StressomeDB record identifier |
| `stress_category` | Individual stress category |
| `higher_order_group` | Higher order biological stress group |

## `evidence`

Evidence source information.

| Column | Description |
|---|---|
| `stressome_id` | StressomeDB record identifier |
| `evidence_source` | Source database or evidence resource |
| `evidence_level` | Evidence confidence level |
| `evidence_type` | Description of evidence type |

## `records_with_sequences`

Joined view connecting metadata with the sequence nonredundant protein table.

## `stressome_fts`

SQLite full text search table for rapid keyword searching.
