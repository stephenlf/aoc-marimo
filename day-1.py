import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
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
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        f"""In Marimo, if the final bit of code in a cell is an **expression,** then the value of that expression is output to the screen."""
    ).callout(kind="info")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    ### Exercise 1

    I have defined a function called `do_things`. Run this function as an **expression** in the cell below. What does `do_things` evaluate to?

    <details><summary>See solution</summary>

    ```python
    # What does `do_things()` evaluate to?
    do_things()
    ```
    <blockquote><code>{do_things()}</code></blockquote>

    </details>
    """)
    return


@app.cell
def _():
    # What does `do_things()` evaluate to?
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Marimo Inputs

    Marimo features a number of input elements that can serve as _user inputs_. For example, you can create text boxes, number inputs, date pickers, and file upload elements. Most of these elements are defined in the `mo.ui` namespace. In a new cell, start typing in `mo.ui.` and see what autocompletes.

    You can access the value of most input elements using the `.value` property. [Read more about Marimo's interactive elements](https://docs.marimo.io/guides/interactivity/).
    """)
    return


@app.cell
def _():
    # Type in "mo.ui." and see what pops up
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercise 2

    Create an `text_area` input element and assign it to a variable. Present this element in the output of the cell it is defined in. In another cell, emit the value of the `text_area`.

    <details><summary>See solution</summary>

    ```python
    # Create a text element, assign it to a variable, and show it in this cell's output
    input = mo.ui.text_area(label='My Input')
    input
    ```

    ```python
    # Show the value of the text element created above.
    input.value
    ```

    </details>
    """)
    return


@app.cell
def _():
    # Create a text element, assign it to a variable, and show it in this cell's output
    return


@app.cell
def _():
    # Show the value of the text element created above.
    return


@app.cell(hide_code=True)
def _(mo, solve):
    mo.md(rf"""
    ## Solving the Puzzle

    I have create a Python function `solve` which accepts the puzzle input and returns the puzzle solution.

    ### Exercise 3

    1. Use a `text_area` input element to capture the puzzle input.
    2. Pass the value of this `text_area` into the `solve` function to solve the puzzle.

    {mo.callout(solve)}

    <details><summary>See solution</summary>

    Define and present text_area input

    ```python
    solution_input = mo.ui.text_area(label='Paste Solution Here')
    solution_input
    ```

    Pass value of text_area input into "solve" function to get solution

    ```python
    solve(solution_input.value)
    ```

    </details>
    """)
    return


@app.cell
def _():
    # Define and present text_area input
    return


@app.cell
def _():
    # Pass value of text_area input into "solve" function to get solution
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.function(hide_code=True)
def do_things():
    return "Congratulations! You did it."


@app.cell(hide_code=True)
def _(mo):
    def _solve_1(input: str) -> int:
        pos = 50
        num_zeroes = 0
        for line in input.splitlines():
            if line.strip() == "":
                continue
            dir = 1 if line[0] == "R" else -1
            amount = int(line[1:])
            pos = (pos + (amount * dir)) % 100
            if pos == 0:
                num_zeroes += 1
        return num_zeroes


    def _solve_2(input: str) -> int:
        """Ugly algorithm that simply simulates each click. Please don't judge."""
        pos = 50
        num_zeroes = 0
        for line in input.splitlines():
            if line.strip() == "":
                continue
            dir = 1 if line[0] == "R" else -1
            amount = int(line[1:])
            new_pos = pos + (dir * amount)
            print(pos, line, new_pos % 100)
            for _click in range(pos, new_pos, dir):
                pos += dir
                pos = pos % 100
                if pos == 0:
                    num_zeroes += 1
        return num_zeroes


    def solve(input: str) -> mo.Html:
        """
        Crack the polar safe. This functions solves AoC 2025 - Day 1.

        Arguments
        ---------
        input : str
            Encrypted lock combo. [Full puzzle input.]

        """
        return mo.md(f"""
            **Part 1**
            ```
            {_solve_1(input)}
            ```

            **Part 2**
            ```
            {_solve_2(input)}
            ```
        """)
    return (solve,)


if __name__ == "__main__":
    app.run()
