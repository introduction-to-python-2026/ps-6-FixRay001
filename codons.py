def create_codon_dict(file_path):
    codon_dict = {}

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            codon, amino = line.split()
            codon_dict[codon] = amino

    return codon_dict
