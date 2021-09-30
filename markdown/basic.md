This pages showes the basic Markdown rules.

Almost all of the tests are from [Markdown: Basics](https://daringfireball.net/projects/markdown/basics) & [Markdown: Syntax](https://daringfireball.net/projects/markdown/syntax).


A First Level Header
====================

There are 6 levels of header.

A Second Level Header
---------------------

## Another Second Level Header

### Header 3

#### Header 4

##### Header 5

###### Header 6


# Texts

The quick brown fox jumped over the lazy
dog's back.

# Blockquote

## common blockquote

> This is a blockquote.
>
> This is the second paragraph in the blockquote.

## nested blockquote

Blockquotes can be nested (i.e. a blockquote-in-a-blockquote) by adding additional levels of >:

> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.

## blockquotes contain other elements

Blockquotes can contain other Markdown elements, including headers, lists, and code blocks:

> ## This is a header.
>
> 1.   This is the first list item.
> 2.   This is the second list item.
>
> Here's some example code:
>
>     return shell_exec("echo $input | $markdown_script");


## Phrase Emphasis

Some of these words *are emphasized*.
Some of these words _are emphasized also_.

Use two asterisks for **strong emphasis**.
Or, if you prefer, __use two underscores instead__.


# Lists

## Unordered (bulleted) lists

Unordered (bulleted) lists use asterisks, pluses, and hyphens (*, +, and -) as list markers. These three markers are interchangable; this:

*  Candy.
*  Gum.
*  Booze.
+  Noodle
-  Water

## Ordered (numbered) lists

Ordered (numbered) lists use regular numbers, followed by periods, as list markers:

1. Red
2. Green
3. Blue

## nested list

1. item-1
   1. item-1-1
   2. item-1-2
2. item-2
   * item-2-a
   * item-2-b
3. item-3<br/>
   some text in a new line
4. item-4


# Links

## Inline-style links

Inline-style links use parentheses immediately after the link text. For example:

* This is an [example link](http://example.com/).
* This is an [example link](http://example.com/ "With a Title").

## Reference-style links

Reference-style links allow you to refer to your links by names, which you define elsewhere in your document:

I get 10 times more traffic from [Google][1] than from
[Yahoo][2] or [MSN][3].

[1]: http://google.com/        "Google"
[2]: http://search.yahoo.com/  "Yahoo Search"
[3]: http://search.msn.com/    "MSN Search"

The title attribute is optional. Link names may contain letters, numbers and spaces, but are not case sensitive:

I start my morning with a cup of coffee and
[The New York Times][NY Times].

[ny times]: http://www.nytimes.com/

## Automatic Links

Markdown supports a shortcut style for creating “automatic” links for URLs and email addresses: simply surround the URL or email address with angle brackets. What this means is that if you want to show the actual text of a URL or email address, and also have it be a clickable link, you can do this:

```md
<http://example.com/>
```

<http://example.com/>


# Images

Image syntax is very much like link syntax.

Inline (titles are optional):

```md
![alt text](/path/to/img.jpg "Title")
```

This project is powered by ![python](python-logo.png).

Reference-style:

```md
![alt text][id]

[id]: /path/to/img.jpg "Title"
```

# Code

## code span

To indicate a span of code, wrap it with backtick quotes (`). Unlike a pre-formatted code block, a code span indicates code within a normal paragraph. For example:

Use the `printf()` function.

To include a literal backtick character within a code span, you can use multiple backticks as the opening and closing delimiters:

``There is a literal backtick (`) here.``

## code block

To specify an entire block of pre-formatted code, indent every line of the block by 4 spaces or 1 tab. Just like with code spans, &, <, and > characters will be escaped automatically.

If you want your page to validate under XHTML 1.0 Strict,
you've got to put paragraph tags in your blockquotes:

    <blockquote>
        <p>For example.</p>
    </blockquote>


---

See alse [extend](extend.md).
