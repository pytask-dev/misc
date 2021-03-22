import pytask


@pytask.mark.produces("../bld/out.txt")
def task_1(produces):
    produces.write_text("1")


@pytask.mark.produces("../bld/out.txt")
def task_2(produces):
    produces.write_text("2")
