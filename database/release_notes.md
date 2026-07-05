# Bacterial StressomeDB v1.0 Release Notes

This release provides Bacterial StressomeDB as a single SQLite database.

## Release statistics

- Curated metadata records: 18,391
- Unique nonredundant protein sequences: 12,046
- Curated stress category labels: 24
- Higher order functional groups: 9
- Bacterial taxa: 1,466
- BacFITBase linked records: 3,378
- Official release format: SQLite

## Notes

- CSV and FASTA files are not distributed separately in this release.
- Protein sequences are stored in the `protein_sequences` table.
- Metadata and sequences can be queried through the `records_with_sequences` view.
- Full text search is supported through the `stressome_fts` table.
