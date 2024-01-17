def main():
    input_file = "input.txt"
    output_file = "output.txt"
    remove_duplicates_and_sort_by_domain(input_file, output_file)
    

def remove_duplicates_and_sort_by_domain(input_file, output_file):
    # Read emails from input file
    with open(input_file, "r") as file:
        emails = file.read().splitlines()

    # Remove duplicates
    unique_emails = list(set(emails))

    # Sort by domain
    sorted_emails = sorted(unique_emails, key=lambda x: x.split("@")[1])

    # Write the result to output file
    with open(output_file, "w") as file:
        file.write("\n".join(sorted_emails))

if __name__ == "__main__":
    main()

