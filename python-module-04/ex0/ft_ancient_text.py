
import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print('Usage: ft_ancient_text.py <file>')
        return

    file_path = sys.argv[1]

    print('=== Cyber Archives Recovery ===')
    print(f"Accessing file '{file_path}'")

    try:
        file: typing.IO = open(file_path, "r")
        content = file.read()

        print('---')
        print(content)
        print('---')

        file.close()
        print(f"File '{file_path}' closed.")

    except OSError as error:
        print(f"Error opening file '{file_path}': {error}")


if __name__ == "__main__":
    main()
