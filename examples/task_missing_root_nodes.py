import pytask


@pytask.mark.depends_on("in.txt")
@pytask.mark.produces("out.txt")
def task_d(produces):
    produces.write_text("1")
