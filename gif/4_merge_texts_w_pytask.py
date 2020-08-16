import pytask
from pathlib import Path


@pytask.mark.produces("first.txt")
def task_create_first_text_file():
    Path("first.txt").write_text("This is the first text.")


@pytask.mark.produces("second.txt")
def task_create_second_text_file(produces):
    produces.write_text("This is the second text.")


# x

@pytask.mark.depends_on(["first.txt", "second.txt"])
@pytask.mark.produces("merged.txt")
def task_merge_texts(depends_on, produces):
    merged_text = depends_on[0].read_text() + " " + depends_on[1].read_text()
    produces.write_text(merged_text)
