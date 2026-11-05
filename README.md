# Protein Structure Analysis Tool

## Overview

Protein Structure Analysis Tool is a Python-based interactive application developed using Streamlit for processing and analysing Protein Data Bank (PDB) files. It provides a collection of tools for extracting protein chains, isolating ligands, removing water molecules, extracting protein atoms, calculating distances between residues, and identifying neighbouring residues within a specified distance cutoff.

The application provides a simple graphical interface that allows users to upload PDB files, select specific structural components, perform analyses, and download the resulting files.

## Features

### 1. Chain Extractor
- Identifies available chains in an uploaded PDB file.
- Allows users to select a specific chain.
- Extracts ATOM and HETATM records belonging to the selected chain.
- Generates a separate PDB file containing the extracted chain.

### 2. Water Remover
- Identifies water molecules (HOH) in the PDB file.
- Removes water molecule records.
- Generates a modified PDB file without HOH records.

### 3. Ligand Isolator
- Identifies available non-water hetero-residues in the PDB file.
- Allows users to select a ligand using its three-letter residue code.
- Extracts the selected ligand's HETATM records.
- Generates a separate PDB file containing the isolated ligand.

### 4. Protein Extractor
- Extracts ATOM records from the uploaded PDB file.
- Separates protein atom records from heteroatom records.
- Generates a PDB file containing the extracted ATOM records.

### 5. Distance Calculator
- Allows users to select a protein chain.
- Accepts two residue identifiers as input.
- Extracts C-alpha (CA) atomic coordinates for the selected residues.
- Calculates the Euclidean distance between the two residues in Angstroms (Å).

### 6. Residues Within Cutoff
- Allows users to select a protein chain and a reference residue.
- Accepts a user-defined distance cutoff in Angstroms (Å).
- Identifies other residues whose C-alpha atoms are within the specified distance of the reference residue.
- Displays the neighbouring residues and their calculated distances.

### 7. Interacting Residues Identification
- Identifies residues surrounding a selected ligand or reference atom based on a user-defined distance cutoff.
- Calculates distances between selected atoms using their three-dimensional Cartesian coordinates.
- Identifies nearby amino acid residues that may participate in protein–ligand interactions.
- Reports the interacting residues and their corresponding distances for further structural analysis.

## Technologies Used

- Python 3
- Streamlit
- Math module
- PDB file format

## Requirements

- Python 3
- Streamlit

## Installation

Install Streamlit using pip:

```bash
pip install streamlit
```

## Usage

Navigate to the project directory and launch the application:

```bash
streamlit run protein_gui.py
```

1. Upload a PDB file through the application interface.
2. Select one of the available structural analysis tools.
3. Provide the required inputs, such as chain ID, ligand code, residue identifiers, or distance cutoff.
4. Execute the selected operation.
5. View the results and download the generated PDB files where applicable.

## Project Structure

```text
Protein_structure_analysis_tool/
│
├── Chain_extractor.py
├── Ligand_extractor.py
├── protein_gui.py
├── Distance_cutoff.py
├── distance_cal.py
├── Neighbouring_residues.py
├── H2O_removal.py
├── protein_extractor.py
└── README.md
```



## Author

Kruttika R
