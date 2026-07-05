# Frequently Asked Questions

## Why is only SQLite provided?

SQLite stores metadata, protein sequences, evidence sources, category mappings, and search indexes in a single self contained file. This avoids duplicated information across CSV and FASTA files and provides a cleaner official release format.

## Does the database still contain protein sequences?

Yes. Protein sequences are stored in the `protein_sequences` table and can be retrieved by joining records through `sequence_md5`.

## Can I export CSV or FASTA if needed?

Yes. Users can export tables or sequences from SQLite using standard SQL queries or the lightweight query utility provided in this repository.

## Is the web application included in this repository?

No. This repository is the official database release repository. The web application is available online at https://bacterial-stressomedb.online/.
