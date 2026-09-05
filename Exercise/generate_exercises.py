import json

# All problems transcribed with LaTeX and Markdown tables
questions = [
    r"""1. Print "I love Python" using Python Shell.""",
    
    r"""2. Print "I love Python" by typing it into a .py file and run it from command line.""",
    
    r"""3. Type import antigravity in the Ipython Shell, it will take you to xkcd and see the awesome Python.""",
    
    r"""4. Launch a new Jupyter notebook server in a folder called "excercis" and create a new Python notebook with the name "excercis_1", then you can do the rest of the problems within this notebook.""",
    
    r"""5. Compute the area of a triangle with base 10 and height 12. Recall that the area of a triangle is half the base times the height.""",
    
    r"""6. Compute the surface area and volume of a cylinder with radius 5 and height 3.""",
    
    r"""7. Compute the slope between the points $(3,4)$ and $(5,9)$. Recall that the slope between points $(x_1, y_1)$ and $(x_2, y_2)$ is $\frac{y_2 - y_1}{x_2 - x_1}$.""",
    
    r"""8. Compute the distance between the points $(3,4)$ and $(5,9)$. Recall that the distance between points in two dimensions is $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.""",
    
    r"""9. Use Python's factorial function to compute $6!$""",
    
    r"""10. A year is considered to be 365 days long. However, a more exact figure is 365.24 days. As a consequence, if we held to the standard 365-day year, we would gradually lose that fraction of the day over time, and seasons and other astronomical events would not occur as expected. A leap year is a year that has an extra day, February 29, to keep the timescale on track. Leap years occur on years that are exactly divisible by 4, unless it is exactly divisible by 100, unless it is divisible by 400. For example, the year 2004 is a leap year, the year 1900 is not a leap year, and the year 2000 is a leap year.

Compute the number of leap years between the years 1500 and 2010.""",

    r"""11. A very powerful approximation for $\pi$ was developed by a brilliant mathematician named Srinivasa Ramanujan. The approximation is the following:
$$\frac{1}{\pi} \approx \frac{2\sqrt{2}}{9801} \sum_{k=0}^{N} \frac{(4k)!(1103+26390k)}{(k!)^4 396^{4k}}$$

Use Ramanujan's formula for $N = 0$ and $N = 1$ to approximate $\pi$. Be sure to use format long. Compare your approximation with Python's stored value for pi. Hint: $0! = 1$ by definition.""",

    r"""12. The hyperbolic $\sin$ or $\sinh$ is defined in terms of exponentials as $\sinh(x) = \frac{\exp(x)-\exp(-x)}{2}$.

Compute $\sinh$ for $x = 2$ using exponentials. Verify that the result is indeed the hyperbolic $\sin$ using Python's function $\sinh$ in the math module.""",

    r"""13. Verify that $\sin^2(x) + \cos^2(x) = 1$ for $x = \pi, \frac{\pi}{2}, \frac{\pi}{4}, \frac{\pi}{6}$.""",
    
    r"""14. Compute the $\sin 87^\circ$.""",
    
    r"""15. Write a Python statement that generates the following error:
"AttributeError: module 'math' has no attribute 'sni'"

Hint: sni is a misspelling of the function $\sin$.""",

    r"""16. Write a Python statement that generates the following error:
"TypeError: sin() takes exactly one argument (0 given)"

Hint: Input arguments refers to the input of a function (any function); for example, the input in $\sin(\pi/2)$ is $\pi/2$.""",

    r"""17. If $P$ is a logical expression, the law of noncontradiction states that $P \text{ AND } (\text{NOT } P)$ is always false. Verify this for $P$ true and $P$ false.""",
    
    r"""18. Let $P$ and $Q$ be logical expressions. De Morgan's rule states that $\text{NOT } (P \text{ OR } Q) = (\text{NOT } P) \text{ AND } (\text{NOT } Q)$ and $\text{NOT } (P \text{ AND } Q) = (\text{NOT } P) \text{ OR } (\text{NOT } Q)$. Generate the truth tables for each statement to show that De Morgan's rule is always true.""",
    
    r"""19. Under what conditions for $P$ and $Q$ is $(P \text{ AND } Q) \text{ OR } (P \text{ AND } (\text{NOT } Q))$ false?""",
    
    r"""20. Construct an equivalent logical expression for OR using only AND and NOT.""",
    
    r"""21. Construct an equivalent logical expression for AND using only OR and NOT.""",
    
    r"""22. The logical operator XOR has the following truth table:
Construct an equivalent logical expression for XOR using only AND, OR, and NOT that has the same truth table (see the following figure)

| P \ Q | 1 | 0 |
| :---: | :---: | :---: |
| **1** | 0 | 1 |
| **0** | 1 | 0 |""",

    r"""Bonus 1. Do the following calculation at the Python command prompt.
$$e^2 \sin(\pi/6) + \log_e(3) \cos(\pi/9) - 5^3$$""",

    r"""Bonus 2. Do the following logical and comparison operations at the Python command prompt. You may assume that P and Q are logical expressions.
For P = 1 and Q = 1; Compute $\text{NOT}(P) \text{ AND } \text{NOT}(Q)$.
For a = 10 and b = 25; Compute $(a < b) \text{ AND } (a = b)$."""
]

cells = []

# Build the JSON structure for the Jupyter Notebook
for q in questions:
    # 1. Add the markdown cell for the question
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [q]
    })
    # 2. Add an empty code cell below it for the answer
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": []
    })

notebook = {
    "cells": cells,
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 2
}

# Generate the file
with open("Chapter1_Exercises.ipynb", "w") as f:
    json.dump(notebook, f, indent=1)
    
print("Notebook generated successfully!")