This pages showes the extended Markdown rules.

Some tests are from [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).


# Code

## code block

To format code or text into its own distinct block, use triple backticks (` ``` `).

~~~
```py
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
```
~~~

The code will render like this:

```py
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
```


# Task lists

To create a task list, preface list items with a regular space character followed by [ ]. To mark a task as complete, use [x].

```md
- [x] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:
```

- [x] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:


# Footnote

You can add footnotes to your content by using this bracket syntax:

```md
Here is a simple footnote[^1].

[^1]: My reference.
```

The footnote will render like this:

Here is a simple footnote[^1].

[^1]: My reference.


# Table

```md
| student-name | gender | telephone-number |
|:---|:--:|--:|
| Tom | M | 1234 |
| Jerry | M | 4321 |
| Jack | M | 5678 |
| Rose | F | 5679 |
```

The table will render like this:

| student-name | gender | telephone-number |
|:---|:--:|--:|
| Tom | M | 1234 |
| Jerry | M | 4321 |
| Jack | M | 5678 |
| Rose | F | 5679 |


# MathJax

You can render *LaTeX* mathematical expressions using **MathJax**, as on [math.stackexchange.com][1]:

```latex
The *Gamma function* satisfying $ \Gamma(n) = (n-1)!\quad\forall n\in\mathbb N $ is via the Euler integral

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$
```

The mathematical expression will render like this:

The *Gamma function* satisfying $ \Gamma(n) = (n-1)!\quad\forall n\in\mathbb N $ is via the Euler integral

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$


---

See alse [basic](basic.md).


[1]: http://math.stackexchange.com/

