def update_file(file1_path, file2_path, output_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()

    # Ensure we only process up to the total number of lines in file2
    total_lines = len(file2_lines)

    # Prepare the output lines
    updated_lines = []
    for i in range(total_lines):
        # Skip the first line (index 0)
        if i == 0:
            updated_lines.append(file2_lines[i])
            continue

        # Read lines from both files
        line1 = file1_lines[i].strip() if i < len(file1_lines) else None
        line2 = file2_lines[i].strip()

        # Split lines into columns
        columns1 = line1.split() if line1 else []
        columns2 = line2.split()

        # Skip lines with fewer than 4 items
        if len(columns2) < 4:
            updated_lines.append(file2_lines[i])
            continue
        print(columns1[0])
        print(columns2[0])
        # Check if column 1 matches and update column 5
        if columns1 and columns1[0] == columns2[0]:
            if len(columns2) >= 5:
                columns2[4] = columns1[4] if len(columns1) > 4 else columns2[4]
            else:
                columns2.append(columns1[4] if len(columns1) > 4 else '')

        # Reconstruct the line and add it to the updated lines
        updated_lines.append(' '.join(columns2) + '\n')

    # Write the updated lines to the output file
    with open(output_path, 'w') as output_file:
        output_file.writelines(updated_lines)


# Example usage
file1_path = 'vpaa-pcff-prexl.car'
file2_path = 'VP-50pwater-pretyped.car'
output_path = 'VP-50pwater-typed.car'

update_file(file1_path, file2_path, output_path)
