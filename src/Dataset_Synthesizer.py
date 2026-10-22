import random
from pathlib import Path
import pandas as pd

def generate_patient_cohort(weight_table_path, output_dir, cohort_type="case", num_files=10):
    try:
        weights_df = pd.read_csv(weight_table_path, sep=r'\s+', comment='#')
    except Exception:
        print("[Error]")
        return

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    alt_alleles = {'A': 'G', 'C': 'T', 'G': 'A', 'T': 'C'}

    for i in range(1, num_files + 1):
        lines = [
            f"# Synthetic Parkinson's 23andMe file for {cohort_type} profile #{i:03d}",
            "# rsid\tchromosome\tposition\tgenotype"
        ]
        
        for _, row in weights_df.iterrows():
            rsid = str(row['rsID'])
            chrom = str(row['chr_name']).replace('chr', '')
            position = str(row['chr_position'])
            
            effect_allele = str(row['effect_allele']).strip()
            if len(effect_allele) != 1:
                effect_allele = 'A'
                
            alt_allele = alt_alleles.get(effect_allele, 'C')

            if cohort_type == "case":
                genotype = random.choices(
                    [effect_allele + effect_allele, effect_allele + alt_allele, alt_allele + alt_allele],
                    weights=[0.55, 0.35, 0.10], 
                    k=1
                )[0]
            else:
                genotype = random.choices(
                    [effect_allele + effect_allele, effect_allele + alt_allele, alt_allele + alt_allele],
                    weights=[0.10, 0.30, 0.60], 
                    k=1
                )[0]
                
            lines.append(f"{rsid}\t{chrom}\t{position}\t{genotype}")
            
        file_path = output_dir / f"parkinsons_{cohort_type}_{i:03d}.txt"
        file_path.write_text("\n".join(lines) + "\n")
        
    print(f"Generated {num_files} files in {output_dir}")

def main():
    current_script_dir = Path(__file__).resolve().parent
    project_root = current_script_dir.parent
    data_dir = project_root / "data"
    
    weights_path = data_dir / "gp2_parkinsons_weights.txt"
    
    if not weights_path.exists():
        print(f"[Error] Weight file not found at: {weights_path}")
        return
        
    generate_patient_cohort(weights_path, data_dir / "parkinsons_cases", cohort_type="case", num_files=10)
    generate_patient_cohort(weights_path, data_dir / "healthy_controls", cohort_type="control", num_files=10)
    
    print("Done")

if __name__ == "__main__":
    main()