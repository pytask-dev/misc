import pytask  # x
from pathlib import Path


@pytask.mark.produces("first.txt")  # x
def task_create_first_text_file():  # x
    Path("first.txt").write_text("This is the first text.")

# x
