from Bio import SeqIO
import pandas as pd

def load_fasta(fasta_file):
    records = []

    for record in SeqIO.parse(fasta_file, "fasta"):
        records.append({
            "protein_id": record.id,
            "sequence": str(record.seq),
            "length": len(record.seq)
        })

    df = pd.DataFrame(records)
    return df
