def modify_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        inside_atom_section = False

        for line in infile:
            if line.strip() == '@<TRIPOS>ATOM':
                inside_atom_section = True
            elif line.strip() == '@<TRIPOS>BOND':
                inside_atom_section = False

            if inside_atom_section and not line.startswith('@<TRIPOS>ATOM'):
                columns = line.split()
                if len(columns) >= 7:
                    columns[5] = columns[1]
                    line = ' '.join(columns) + '\n'

            outfile.write(line)

# Example usage
input_file = 'VP-30pwater-natxl-pretyped.mol2'
output_file = 'VP-30pwater-natxl-pretyped-elements.mol2'
modify_file(input_file, output_file)
