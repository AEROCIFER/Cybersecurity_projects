<<<<<<< HEAD
from file_processing import *
import argparse
import sys


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "help":
        print(
            """
Ceser Cipher Program: 

This program enables encryption and decryption of text and text files using the Caesar cipher technique. 
The encryption and decryption process is based on the shift value specified by the user.

Caesar Cipher Program Usage:

Options:
  -m, --mode           Mode of operation: encrypt or decrypt (required)
  -s, --shift          Shift value for the Caesar cipher (required)
  -t, --text           Text to encrypt or decrypt (optional)
  -i, --input_file     Input file for encryption or decryption (optional)
  -o, --output_file    Output file to save the result (optional, required with input_file)

Examples:
  Encrypt text:
    python main.py -m encrypt -s 3 -t "Hello, World!"
  Decrypt text:
    python main.py -m decrypt -s 3 -t "Khoor, Zruog!"
  Encrypt a file:
    python main.py -m encrypt -s 3 -i input.txt -o output.txt
  Decrypt a file:
    python main.py -m decrypt -s 3 -i output.txt -o decrypted.txt
            """
        )
        sys.exit(0)

    parser = argparse.ArgumentParser(description="Caesar Cipher Program")

    parser.add_argument(
        "-m", "--mode", required=True, choices=["encrypt", "decrypt"],
        help="Choose the mode: 'encrypt' or 'decrypt'"
    )
    parser.add_argument(
        "-s", "--shift", required=True, type=int,
        help="Shift value for the Caesar cipher"
    )
    parser.add_argument(
        "-t", "--text",
        help="Text to encrypt or decrypt (optional, for direct input)"
    )
    parser.add_argument(
        "-i", "--input_file",
        help="Input file for encryption or decryption (optional)"
    )
    parser.add_argument(
        "-o", "--output_file",
        help="Output file to save the result (optional, required with input_file)"
    )

    args = parser.parse_args()

    if args.text and args.input_file:
        print("Error: Please provide either text or an input file, not both.")
        return

    if args.input_file:
        if not args.output_file:
            print("Error: Output file is required when processing a file.")
            return
        file_processing(args.input_file, args.output_file, args.shift, args.mode)
    elif args.text:
        result = caesar_cipher(args.text, args.shift, args.mode)
        print(f"The resulting text is: {result}")
    else:
        print("Error: Please provide text or an input file.")

if __name__ == "__main__":
=======
from file_processing import *
import argparse
import sys


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "help":
        print(
            """
Ceser Cipher Program: 

This program enables encryption and decryption of text and text files using the Caesar cipher technique. 
The encryption and decryption process is based on the shift value specified by the user.

Caesar Cipher Program Usage:

Options:
  -m, --mode           Mode of operation: encrypt or decrypt (required)
  -s, --shift          Shift value for the Caesar cipher (required)
  -t, --text           Text to encrypt or decrypt (optional)
  -i, --input_file     Input file for encryption or decryption (optional)
  -o, --output_file    Output file to save the result (optional, required with input_file)

Examples:
  Encrypt text:
    python main.py -m encrypt -s 3 -t "Hello, World!"
  Decrypt text:
    python main.py -m decrypt -s 3 -t "Khoor, Zruog!"
  Encrypt a file:
    python main.py -m encrypt -s 3 -i input.txt -o output.txt
  Decrypt a file:
    python main.py -m decrypt -s 3 -i output.txt -o decrypted.txt
            """
        )
        sys.exit(0)

    parser = argparse.ArgumentParser(description="Caesar Cipher Program")

    parser.add_argument(
        "-m", "--mode", required=True, choices=["encrypt", "decrypt"],
        help="Choose the mode: 'encrypt' or 'decrypt'"
    )
    parser.add_argument(
        "-s", "--shift", required=True, type=int,
        help="Shift value for the Caesar cipher"
    )
    parser.add_argument(
        "-t", "--text",
        help="Text to encrypt or decrypt (optional, for direct input)"
    )
    parser.add_argument(
        "-i", "--input_file",
        help="Input file for encryption or decryption (optional)"
    )
    parser.add_argument(
        "-o", "--output_file",
        help="Output file to save the result (optional, required with input_file)"
    )

    args = parser.parse_args()

    if args.text and args.input_file:
        print("Error: Please provide either text or an input file, not both.")
        return

    if args.input_file:
        if not args.output_file:
            print("Error: Output file is required when processing a file.")
            return
        file_processing(args.input_file, args.output_file, args.shift, args.mode)
    elif args.text:
        result = caesar_cipher(args.text, args.shift, args.mode)
        print(f"The resulting text is: {result}")
    else:
        print("Error: Please provide text or an input file.")

if __name__ == "__main__":
>>>>>>> 298a8d58613c387487851e7ceb42a67eb491e9f2
    main()