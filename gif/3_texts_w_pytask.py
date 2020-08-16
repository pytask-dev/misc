import pytask
from pathlib import Path


@pytask.mark.produces("first.txt")
def task_create_first_text_file():
    Path("first.txt").write_text("This is the first text.")


# x

@pytask.mark.produces("second.txt")
def task_create_second_text_file(produces):
    produces.write_text("This is the second text.")
