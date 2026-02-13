# IDPE: Integrated Document Parsing Enhancement

A novel lightweight framework extending MonkeyOCR v1.5 for robust, adaptive, and relational document parsing.

## Key Innovations
- **Recursive Reasoning Framework (RRF)** with Chain-of-Visual-Verification for iterative self-correction of hierarchy/logical errors  
- **Active-Sampling** with Dynamic LoRA Router and zero-shot geometric pattern matching for low-resource domain adaptation  
- **Logical-Graph Extraction** with edge-weighted GNN for semantic knowledge graph output with relational fidelity

## Features
- Up to 30.3% relative hierarchy fidelity improvement (tree edit distance)  
- 27.4% average cross-domain accuracy gain on low-resource subsets  
- 24.5% relative relational edge F1 improvement  
- Super-additive synergy: 26–27% composite gains  
- Practical inference efficiency on consumer GPUs

## Installation

```bash
git clone https://github.com/yourusername/IDPE-Document-Parsing.git
cd IDPE-Document-Parsing
pip install -r requirements.txt
# Optional: editable install
pip install -e .
