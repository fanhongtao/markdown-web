# Summary

I use [Gollum](https://github.com/gollum/gollum) as my daily wiki engine. It is a great work.

A few days ago, one of my [VPS](http://en.wikipedia.org/wiki/Virtual_private_server) was expired, and I didn't want to renew it. So I tried to install some kind of Linux on my HONOR-10X mobile phone. Because I couldn't ROOT my HONOR-10X, I installed [Termux](https://termux.com/), and found that I coundn't install Gollum or use docker in Termux!

In order to use my wikis in Termux, I write this 'Markdown-web'. It is based on [Python-Markdown](https://python-markdown.github.io).


# Features

* Show markdown files as HTML. <br/>
  Note: This is *NOT* a wiki engine. just a simple web-based markdown reader.
* Support common markdown rulse.<br/>
  With Python-Markdown and it's [extentions](https://github.com/Python-Markdown/markdown/wiki/Third-Party-Extensions), it is easy to do that.<br/>
  Supported markdown rules can be found in [basic](markdown/basic.md) and [extend](markdown/extend.md).
* A Gollum like outlook.<br/>
  With respect to Gollum, I copy/modify [Gollum's CSS](web/app/static/css/skin.css) to get a similar look.
* Support global `custom.css` and/or `custom.js` in markdown root directory.<br/>
  This feature is also copied from Gollum.
* Support `favicon.ico` in markdown root directory.


# Target

Who may use this markdown-web?

Someone who likes to explore the capability of his/her devices.

It's terrible a shame that a developer/I.T. lover just use his/her powerful mobile phone to make calls or text messages.

# Usage

See [install](install.md)

