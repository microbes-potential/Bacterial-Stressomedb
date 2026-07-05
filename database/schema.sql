CREATE INDEX idx_cat_id ON record_categories(stressome_id)
CREATE INDEX idx_evidence_id ON evidence(stressome_id)
CREATE INDEX idx_records_cat ON stressome_records(stress_category)
CREATE INDEX idx_records_gene ON stressome_records(gene_symbol)
CREATE INDEX idx_records_id ON stressome_records(stressome_id)
CREATE INDEX idx_records_md5 ON stressome_records(sequence_md5)
CREATE INDEX idx_records_org ON stressome_records(organism)
CREATE INDEX idx_seq_id ON protein_sequences(stressome_id)
CREATE INDEX idx_seq_md5 ON protein_sequences(sequence_md5)
CREATE TABLE "evidence" (
"stressome_id" TEXT,
  "evidence_source" TEXT,
  "evidence_level" TEXT,
  "evidence_type" TEXT
)
CREATE TABLE "organisms" (
"organism_id" TEXT,
  "organism" TEXT,
  "taxon_id" TEXT
)
CREATE TABLE "protein_sequences" (
"stressome_id" TEXT,
  "fasta_header" TEXT,
  "sequence" TEXT,
  "sequence_length" INTEGER,
  "sequence_md5" TEXT
)
CREATE TABLE "record_categories" (
"stressome_id" TEXT,
  "stress_category" TEXT,
  "higher_order_group" TEXT
)
CREATE TABLE "release_info" (
"key" TEXT,
  "value" TEXT
)
CREATE TABLE "stress_category_map" (
"stress_category" TEXT,
  "higher_order_group" TEXT
)
CREATE VIRTUAL TABLE stressome_fts USING fts5(stressome_id, gene_symbol, gene_symbol_primary, protein_name, description, organism, stress_category, uniprot_accession)
CREATE TABLE "stressome_records" (
"stressome_id" TEXT,
  "gene_symbol_primary" TEXT,
  "gene_symbol" TEXT,
  "synonyms" TEXT,
  "protein_name" TEXT,
  "description" TEXT,
  "stress_category" TEXT,
  "stress_subcategory" TEXT,
  "organism" TEXT,
  "taxon_id" TEXT,
  "uniprot_accession" TEXT,
  "evidence_sources" TEXT,
  "evidence_levels" TEXT,
  "evidence_types" TEXT,
  "source_tables" TEXT,
  "source_count" TEXT,
  "sequence_length" TEXT,
  "sequence_md5" TEXT,
  "has_sequence" TEXT
)
CREATE VIEW category_summary AS
SELECT higher_order_group, stress_category, COUNT(DISTINCT stressome_id) AS record_count
FROM record_categories
GROUP BY higher_order_group, stress_category
ORDER BY record_count DESC
CREATE VIEW records_with_sequences AS
SELECT r.*, p.fasta_header, p.sequence
FROM stressome_records r
LEFT JOIN protein_sequences p ON r.sequence_md5 = p.sequence_md5