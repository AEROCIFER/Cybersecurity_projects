from ceaser import *

def file_processing(input_file, output_file, shift, mode):
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        processed_content = caesar_cipher(content, shift, mode)

        with open(output_file, 'w') as file:
            file.write(processed_content)

        print(f"File succesfully {mode}ed. Output written to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error file not found.")
    except Exception as e:
        print(f"A error occured: {e}")
