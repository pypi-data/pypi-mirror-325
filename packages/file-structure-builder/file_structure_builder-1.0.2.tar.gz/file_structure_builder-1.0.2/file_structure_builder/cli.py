import argparse
from file_structure_builder.builder import FileStructureBuilder
from file_structure_builder.parser import StructureParser

def main():
    parser = argparse.ArgumentParser(
        description="File Structure Builder - A tool to generate file structures."
    )
    parser.add_argument(
        "--file", "-f", type=str, help="Path to the file containing the structure definition"
    )
    parser.add_argument(
        "--api", "-a", action="store_true", help="Use API to fetch the structure definition"
    )
    parser.add_argument(
        "--interactive", "-i", action="store_true", help="Interactive mode for building structures"
    )

    args = parser.parse_args()

    if args.api:
        print("API mode is not implemented yet.")
        return

    if args.interactive:
        print(
            "You are an assistant who is going to help build file structures.\n"
            "Don't give any extra explanations. Just build the file structure I want you to build.\n"
            "What you need to build: <user input>"
        )
        return

    if args.file:
        try:
            structure = StructureParser.parse_file(args.file)
            FileStructureBuilder.build_structure(structure)
            print(f"File structure created from {args.file}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Please provide a file path using the --file flag or use --interactive mode.")

if __name__ == "__main__":
    main()