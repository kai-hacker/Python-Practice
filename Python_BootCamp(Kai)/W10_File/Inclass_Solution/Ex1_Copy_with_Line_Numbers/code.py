# Read from input.txt and write to output.txt with line numbers
input_f = "Python_BootCamp(Kai)/W10_File/Inclass_Solution/Ex1_Copy_with_Line_Numbers/input.txt"
output_f = "Python_BootCamp(Kai)/W10_File/Inclass_Solution/Ex1_Copy_with_Line_Numbers/output.txt"

print(f"Reading from: {input_f}")
print(f"Writing to: {output_f}")

with open(input_f, "r") as infile, open(output_f, "w") as outfile:
    line_count = 0
    for i, line in enumerate(infile, start=1):
        # Write number + original content
        outfile.write(f"{i}: {line}")
        line_count += 1
    print(f"Wrote {line_count} lines to output file")