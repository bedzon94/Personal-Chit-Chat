def process_emails(input_file, output_file):
    try:
        # Read emails from input file
        with open(input_file, "r") as file:
            emails = file.readlines()

        # Remove duplicates and sort emails
        unique_emails = sorted(set(emails))

        # Write unique and sorted emails to output file
        with open(output_file, "w") as file:
            file.writelines(unique_emails)

        print("Processing completed successfully.")

    except Exception as e:
        print(f"Error: {e}")

# Specify the input and output file names
input_file = "input.txt"
output_file = "output.txt"

# Call the function to process emails
process_emails(input_file, output_file)

