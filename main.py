"""
Project Name: Universal Biological Sequence & Motif Analyzer
Author: Tejaskumar Parmar
Description: A clean, modular Python utility to analyze DNA, RNA, and Protein sequences, 
             detect sequence types, calculate reverse complements, and find exact motif positions.
"""

def detect_sequence_type(sequence: str):
    """Detects whether the given sequence is DNA, RNA, or Protein."""
    seq_set = set(sequence.upper())
    
    if seq_set.issubset({"A", "T", "G", "C"}):
        return "DNA", "ATGC"
    elif seq_set.issubset({"A", "U", "G", "C"}):
        return "RNA", "AUGC"
    else:
        protein_alphabet = set("ACDEFGHIKLMNPQRSTVWY")
        if seq_set.issubset(protein_alphabet):
            return "Protein", protein_alphabet
        else:
            return "Unknown/Invalid", set()

def get_reverse_complement(sequence: str, seq_type: str):
    """Calculates reverse complement for DNA or RNA strands."""
    if seq_type == "DNA":
        trans_table = str.maketrans("ATGC", "TACG")
    elif seq_type == "RNA":
        trans_table = str.maketrans("AUGC", "UACG")
    else:
        return None
    
    return sequence.translate(trans_table)[::-1]

def find_motif_positions(sequence: str, motif: str):
    """Finds all 1-indexed start positions of a motif allowing overlaps."""
    positions = []
    start = 0
    while True:
        pos = sequence.find(motif, start)
        if pos == -1:
            break
        positions.append(pos + 1)
        start = pos + 1
    return positions

def main():
    print("=" * 65)
    print("       UNIVERSAL BIOLOGICAL SEQUENCE & MOTIF ANALYZER")
    print("=" * 65)
    
    main_sequence = input("\nEnter Main Sequence (DNA/RNA/Protein): ").strip().upper()
    target_motif = input("Enter Motif to Search: ").strip().upper()
    
    if not main_sequence or not target_motif:
        print("[!] Error: Sequence and Motif cannot be empty.")
        return
        
    seq_type, _ = detect_sequence_type(main_sequence)
    
    print("\n" + "-" * 65)
    print(f" Detected Sequence Type : {seq_type}")
    print(f" Main Sequence Length   : {len(main_sequence)} residues")
    print(f" Target Motif           : {target_motif}")
    print("-" * 65)
    
    # Forward Strand Analysis
    motif_positions = find_motif_positions(main_sequence, target_motif)
    occurrence_count = len(motif_positions)
    
    print(f"\n >>> FORWARD STRAND ANALYSIS ({seq_type}) <<<")
    print(f"     Occurrences Found : {occurrence_count}")
    print(f"     Exact Positions   : {motif_positions if motif_positions else 'Not Found'}")
    
    # Reverse Complement Analysis (for DNA/RNA)
    if seq_type in ["DNA", "RNA"]:
        rev_motif = get_reverse_complement(target_motif, seq_type)
        rev_positions = find_motif_positions(main_sequence, rev_motif)
        
        print(f"\n >>> REVERSE COMPLEMENT STRAND ANALYSIS <<<")
        print(f"     Reverse Motif     : {rev_motif}")
        print(f"     Occurrences Found : {len(rev_positions)}")
        print(f"     Exact Positions   : {rev_positions if rev_positions else 'Not Found'}")
        
        total_hits = occurrence_count + len(rev_positions)
        print(f"\n Total Combined Matches (Forward + Reverse): {total_hits}")
        
    print("=" * 65)

if __name__ == "__main__":
    main()