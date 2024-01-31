# Initialize empty lists for each status
warnings = []
threats = []
errors = []

# Read the data from raw.txt
with open('raw.txt', 'r') as file:
    lines = file.readlines()

# Iterate through each line and categorize them
for line in lines:
    if "WARNING" in line:
        warnings.append(line)
    elif "THREAT" in line:
        threats.append(line)
    elif "ERROR" in line:
        errors.append(line)

# Write the categorized data to separate .txt files
with open('warnings.txt', 'w') as file:
    file.writelines(warnings)

with open('threats.txt', 'w') as file:
    file.writelines(threats)

with open('errors.txt', 'w') as file:
    file.writelines(errors)

print("Files 'warnings.txt', 'threats.txt', and 'errors.txt' have been created with the respective data.")
