# Description
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
