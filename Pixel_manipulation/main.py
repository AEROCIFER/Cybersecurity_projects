from PIL import Image
import argparse
import random


def encrypt_image(input_path, output_path, key):
    try:
        img = Image.open(input_path)
        img = img.convert("RGBA")  # Ensure RGBA format for consistency
        pixels = img.load()

        random.seed(key)  # Seed the random generator with the key
        width, height = img.size

        # Use the first pixel as the marker (you can choose any location)
        marker = (123, 234, 45, 255)  # Arbitrary marker to verify key validity
        rand_marker = (
            marker[0] ^ random.randint(0, 255),
            marker[1] ^ random.randint(0, 255),
            marker[2] ^ random.randint(0, 255),
            marker[3],  # Keep alpha unchanged
        )
        pixels[0, 0] = rand_marker  # Save encrypted marker in the first pixel

        for i in range(width):
            for j in range(height):
                if i == 0 and j == 0:
                    continue  # Skip the marker pixel
                r, g, b, a = pixels[i, j]  # Extract RGBA channels

                # Generate random values for encryption
                rand_r = random.randint(0, 255)
                rand_g = random.randint(0, 255)
                rand_b = random.randint(0, 255)

                # XOR the pixel values with the random values
                encrypted_pixel = (
                    r ^ rand_r,
                    g ^ rand_g,
                    b ^ rand_b,
                    a,  # Keep alpha unchanged
                )
                pixels[i, j] = encrypted_pixel

        img.save(output_path)
        print("File successfully encrypted and saved to:", output_path)
    except Exception as e:
        print("Error during encryption:", e)


def decrypt_image(input_path, output_path, key):
    try:
        img = Image.open(input_path)
        img = img.convert("RGBA")  # Ensure RGBA format for consistency
        pixels = img.load()

        random.seed(key)  # Seed the random generator with the same key
        width, height = img.size

        # Verify the marker
        marker = (123, 234, 45, 255)  # Original marker
        rand_marker = pixels[0, 0]  # Encrypted marker in the first pixel
        original_marker = (
            rand_marker[0] ^ random.randint(0, 255),
            rand_marker[1] ^ random.randint(0, 255),
            rand_marker[2] ^ random.randint(0, 255),
            rand_marker[3],  # Keep alpha unchanged
        )

        if original_marker != marker:
            print("Error: Incorrect key provided. Decryption aborted.")
            return

        for i in range(width):
            for j in range(height):
                if i == 0 and j == 0:
                    continue  # Skip the marker pixel
                r, g, b, a = pixels[i, j]  # Extract RGBA channels

                # Generate the same random values used in encryption
                rand_r = random.randint(0, 255)
                rand_g = random.randint(0, 255)
                rand_b = random.randint(0, 255)

                # XOR the encrypted values with the same random values to decrypt
                decrypted_pixel = (
                    r ^ rand_r,
                    g ^ rand_g,
                    b ^ rand_b,
                    a,  # Keep alpha unchanged
                )
                pixels[i, j] = decrypted_pixel

        img.save(output_path)
        print("File successfully decrypted and saved to:", output_path)
    except Exception as e:
        print("Error during decryption:", e)


def main():
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt an image using a key.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-m", "--mode", 
        choices=["encrypt", "decrypt"], 
        required=True,
        help="Operation mode: 'encrypt' to encrypt an image, 'decrypt' to decrypt an image."
    )
    parser.add_argument(
        "-i", "--input", 
        required=True, 
        help="Path to the input image file to be processed."
    )
    parser.add_argument(
        "-o", "--output", 
        required=True, 
        help="Path to save the processed image file."
    )
    parser.add_argument(
        "-k", "--key", 
        type=int, 
        required=True,
        help="Encryption/Decryption key. Use the same key for encryption and decryption."
    )

    args = parser.parse_args()

    # Call the appropriate function based on the mode
    if args.mode == "encrypt":
        encrypt_image(args.input, args.output, args.key)
    elif args.mode == "decrypt":
        decrypt_image(args.input, args.output, args.key)


if __name__ == "__main__":
    main()

