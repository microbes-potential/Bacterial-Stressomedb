import argparse
import csv
import sqlite3
import sys
from pathlib import Path

DEFAULT_DB = Path(__file__).resolve().parents[1] / "database" / "Bacterial_StressomeDB_v1.sqlite"


def connect(db_path):
    con = sqlite3.connect(str(db_path))
    con.row_factory = sqlite3.Row
    return con


def print_rows(rows, limit=None):
    rows = list(rows)
    if limit:
        rows = rows[:limit]
    if not rows:
        print("No records found.")
        return
    cols = rows[0].keys()
    writer = csv.DictWriter(sys.stdout, fieldnames=cols, delimiter="\t")
    writer.writeheader()
    for r in rows:
        writer.writerow(dict(r))


def cmd_stats(args):
    con = connect(args.db)
    rows = con.execute("SELECT key, value FROM release_info ORDER BY key").fetchall()
    print_rows(rows)


def cmd_search(args):
    con = connect(args.db)
    q = f"%{args.query}%"
    rows = con.execute(
        """
        SELECT stressome_id, gene_symbol, protein_name, organism, stress_category, uniprot_accession
        FROM stressome_records
        WHERE gene_symbol LIKE ? OR gene_symbol_primary LIKE ? OR protein_name LIKE ?
              OR description LIKE ? OR organism LIKE ? OR stress_category LIKE ? OR uniprot_accession LIKE ?
        LIMIT ?
        """,
        (q, q, q, q, q, q, q, args.limit),
    ).fetchall()
    print_rows(rows)


def cmd_category(args):
    con = connect(args.db)
    q = f"%{args.group}%"
    rows = con.execute(
        """
        SELECT r.stressome_id, r.gene_symbol, r.protein_name, r.organism, c.stress_category, c.higher_order_group
        FROM stressome_records r
        JOIN record_categories c ON r.stressome_id = c.stressome_id
        WHERE c.higher_order_group LIKE ? OR c.stress_category LIKE ?
        LIMIT ?
        """,
        (q, q, args.limit),
    ).fetchall()
    print_rows(rows)


def cmd_sequence(args):
    con = connect(args.db)
    rows = con.execute(
        """
        SELECT r.stressome_id, r.gene_symbol, r.protein_name, r.organism, p.sequence
        FROM stressome_records r
        JOIN protein_sequences p ON r.sequence_md5 = p.sequence_md5
        WHERE r.stressome_id = ?
        LIMIT 1
        """,
        (args.id,),
    ).fetchall()
    if not rows:
        print("No sequence found.")
        return
    r = rows[0]
    print(f">{r['stressome_id']}|gene={r['gene_symbol']}|organism={r['organism']}|protein={r['protein_name']}")
    seq = r["sequence"]
    for i in range(0, len(seq), 70):
        print(seq[i:i+70])


def main():
    parser = argparse.ArgumentParser(description="Query the Bacterial StressomeDB SQLite database.")
    parser.add_argument("--db", default=str(DEFAULT_DB), help="Path to Bacterial_StressomeDB_v1.sqlite")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("stats", help="Show release statistics")
    p.set_defaults(func=cmd_stats)

    p = sub.add_parser("search", help="Search by gene, protein, organism, accession, category, or description")
    p.add_argument("--query", required=True)
    p.add_argument("--limit", type=int, default=20)
    p.set_defaults(func=cmd_search)

    p = sub.add_parser("category", help="Search by stress category or higher order group")
    p.add_argument("--group", required=True)
    p.add_argument("--limit", type=int, default=20)
    p.set_defaults(func=cmd_category)

    p = sub.add_parser("sequence", help="Retrieve a protein sequence by StressomeDB ID")
    p.add_argument("--id", required=True)
    p.set_defaults(func=cmd_sequence)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
