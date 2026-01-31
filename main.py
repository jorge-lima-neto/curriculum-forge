import os
import argparse
import sys
from src.parser import ResumeParser
from src.generator import HTMLGenerator

def main():
    parser = argparse.ArgumentParser(description="Professional Resume Generator")
    parser.add_argument('input', nargs='?', default=os.path.join('input', 'sample.txt'), 
                        help="Path to the input text file (default: input/sample.txt)")
    parser.add_argument('--output', '-o', default=os.path.join('output', 'resume.html'),
                        help="Path to the output HTML file (default: output/resume.html)")
    
    args = parser.parse_args()
    
    input_file = args.input
    output_file = args.output

    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)

    print(f"Reading resume from: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    print("Parsing text...")
    resume_parser = ResumeParser()
    resume_data = resume_parser.parse(text)
    
    if not resume_data:
        print("Failed to parse data. Ensure file content is valid.")
        sys.exit(1)

    print(f"Parsed {len(resume_data.sections)} sections: {[s.title for s in resume_data.sections]}")
    
    print("Generating HTML...")
    generator = HTMLGenerator()
    final_path = generator.generate(resume_data, output_file)
    
    print(f"Success! HTML resume generated at: {final_path}")
    print("Open this file in your browser and use 'Print to PDF' to save it.")

if __name__ == "__main__":
    main()
