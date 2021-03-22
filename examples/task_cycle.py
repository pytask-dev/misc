import pytask


@pytask.mark.depends_on("out_2.txt")
@pytask.mark.produces("out_1.txt")
def task_1(produces):
    produces.write_text("1")


@pytask.mark.depends_on("out_1.txt")
@pytask.mark.produces("out_2.txt")
def task_2(produces):
    produces.write_text("2")
