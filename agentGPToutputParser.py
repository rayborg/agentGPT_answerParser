import re

def extract_responses(input_file, output_file):
    with open(input_file, 'rb') as infile:
        for encoding in ['utf-8', 'iso-8859-1', 'cp1252']:
            try:
                text = infile.read().decode(encoding)
                break
            except UnicodeDecodeError:
                pass

    pattern = r'Completing:(.*?)Added task'
    responses = re.findall(pattern, text, re.DOTALL)

    print(f"Found {len(responses)} responses")

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("Compiled Responses:\n\n")
        for i, response in enumerate(responses, 1):
            outfile.write(f"Response {i}:\n")
            outfile.write(response.strip())
            outfile.write("\n\n")
            print(f"Wrote response {i}")

    print(f"Finished writing {len(responses)} responses to {output_file}")

if __name__ == "__main__":
    input_file = 'agentGPToutput.txt'
    output_file = 'compiled.txt'
    extract_responses(input_file, output_file)
