# 🧬 Universal Biological Sequence & Motif Analyzer

A lightweight, high-performance Python command-line tool designed for bioinformaticians and researchers to automatically detect sequence types (**DNA, RNA, or Protein**), compute **Reverse Complements**, and map exact **Motif occurrences and positions** with overlapping support.

---

## ✨ Features
- **Automatic Sequence Type Detection**: Intelligently identifies whether the input string is DNA (A, T, G, C), RNA (A, U, G, C), or a standard Protein (20 Amino Acids).
- **Strand-Specific Analysis**: Automatically computes the reverse complement strand for nucleic acids (DNA/RNA) and searches motifs on both strands.
- **Overlapping Motif Support**: Detects all occurrences even if motifs overlap within the sequence.
- **Zero External Dependencies**: Built entirely using Python's standard library (`O(n)` string searching), meaning no heavy installations like Biopython or Pandas are required.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have **Python 3.x** installed on your system.

### Running the Project
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/bio-motif-analyzer.git](https://github.com/YOUR_USERNAME/bio-motif-analyzer.git)
   cd bio-motif-analyzer