def extract_ligand():
    with open("C:/Users/hp/Downloads/1a3n.pdb","r") as pdb_file:
        for line in pdb_file:
            if line.startswith("HET"):
                print(line.strip())
    chain_id=input("Enter the chain ID: ")
    output_file=f"C:/Users/hp/Downloads/extracted_ligand_{chain_id}.pdb"
    with open("C:/Users/hp/Downloads/1a3n.pdb","r") as pdb_file,open(output_file,"w") as out_file:
        for line in pdb_file:
            if line.startswith("HETATM") and line[21]==chain_id:
                if line[17:20].strip() != "HOH":
                    out_file.write(line)
                    print(line.strip())
    print(f"Extracted ligands from chain {chain_id} saved to:\n{output_file}")
extract_ligand()