"""Example task shown in README.rst."""
import pytask


@pytask.mark.produces("hello_earth.txt")
def task_hello_earth(produces):
    produces.write_text("Hello, earth!")
