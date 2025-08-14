from Bio import SeqIO
import argparse

def extract_region_with_flanks(fasta_file, contig, start, end, flank):
    """
    Extract sequence from a specific contig in a FASTA file from start to end positions,
    including flanking sequences of specified length on both sides.

    Parameters:
    - fasta_file (str): Path to the FASTA file.
    - contig (str): Contig/sequence ID to extract from.
    - start (int): Start position (1-based, inclusive).
    - end (int): End position (1-based, inclusive).
    - flank (int): Number of nucleotides to include as flanking regions on each side.

    Returns:
    - str: Extracted sequence with flanks.
    """


    seq_dict = SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta"))

    if contig not in seq_dict:
        raise ValueError(f"Contig '{contig}' not found in FASTA file.")

    seq_record = seq_dict[contig]
    seq_len = len(seq_record.seq)
   # print(seq_len)

    flank_start = max(0, start - 1 - flank)
    flank_end = min(seq_len, end + flank)  

   # print(flank_start)
    #print(flank_end)

    extracted_seq = seq_record.seq[flank_start:flank_end]

    return str(extracted_seq)

parser = argparse.ArgumentParser(description="-")
parser.add_argument('fasta_path', type=str, help='Path to fasta file')
parser.add_argument('contig_name', type=str, help='Name of contig')
parser.add_argument('start_pos', type=int, help='Start position')
parser.add_argument('end_pos', type=int, help='End position')
parser.add_argument('flank', type=int, help='Flanking length')

args = parser.parse_args()

fasta_path = args.fasta_path
contig_name = args.contig_name
start_pos = args.start_pos
end_pos = args.end_pos
flank = args.flank

seq = extract_region_with_flanks(fasta_path, contig_name, start_pos, end_pos, flank)

with open('found_sequences.txt', 'a') as file:
    file.write(f"Contig: {contig_name}, position: {start_pos}-{end_pos} + flanking region\n")
    file.write(f"{seq}\n\n")
#print(seq)