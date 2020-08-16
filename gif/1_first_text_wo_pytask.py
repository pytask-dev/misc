from pathlib import Path


def create_first_text_file():
    Path("first.txt").write_text("This is the first text.")


if __name__ == '__main__':
    create_first_text_file()
