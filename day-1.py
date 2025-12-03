import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""
    # Day 1

    ## Assignments and Expressions

    In Python, you will mainly be working with two language constructs: **assignments** and **expressions**. These take the following form:

    Expression are bits of code that evaluate to a single value. All of these are expressions:

    ```python
    3
    3 + x
    x.call_method()
    do_thing(x)
    ```

    Assignments use the equals sign `=` to *assign* the value of an expression to a variable. These take the form $variable = expression$. For example:

    ```python
    a = 3
    b = a + 4
    y = x.call_method()
    z = do_thing(y)
    ```

    **Lesson 1:** In Marimo, if the final bit of code in a cell is an **expression,** then the value of that expression is output to the screen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.vstack(
        [
            mo.md("""

    ### Exercise 1

    I have defined a function called `do_things`. Copy this code into the blank cell beneath this cell. What happens when you remove the comment (`#`) character? What did `do_things` evaluate to?

    ```python
    a = do_things()
    #a
    ```
    """),
            mo.accordion({"See Solution": mo.md(f"`{do_things()}`")}),
            mo.md("""_Prefer to copy code by hand, rather than copy/pasting the whole block. Learning code is orders of magnitude more effective with hands on keyboard._
    """).callout(kind="info"),
        ]
    )
    return


@app.cell
def _():
    # Copy code here. What is the value of "a"?
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Marimo Inputs

    Marimo features a number of input elements
    """)
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.function(hide_code=True)
def do_things():
    return "Congratulations! You did it."


if __name__ == "__main__":
    app.run()
