# -*- coding: utf-8 -*-

from md_testsuite import IO
from engines import *

original = [
IO("2-paragraphs-hard-return-spaces",
"""This is a first paragraph,
on multiple lines.
     
This is a second paragraph.
There are spaces in between the two.""",

"""<p>This is a first paragraph,
on multiple lines.</p>

<p>This is a second paragraph.
There are spaces in between the two.</p>"""
),

IO("2-paragraphs-hard-return",
"""This is a first paragraph,
on multiple lines.

This is a second paragraph
which has multiple lines too.""",

"""<p>This is a first paragraph,
on multiple lines.</p>

<p>This is a second paragraph
which has multiple lines too.</p>"""
),

IO("2-paragraphs-line-returns",
"""A first paragraph.



A second paragraph after 3 CR (carriage return).""",

"""<p>A first paragraph.</p>

<p>A second paragraph after 3 CR (carriage return).</p>"""
),

IO("2-paragraphs-line-spaces",
"""This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.
     
A few spaces and a new long long long long long long long long long long long long long long long long paragraph on 1 line.""",

"""<p>This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.</p>

<p>A few spaces and a new long long long long long long long long long long long long long long long long paragraph on 1 line.</p>"""
),

IO("2-paragraphs-line-tab",
"""This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.
	
1 tab to separate them and a new long long long long long long long long long long long long long long long long paragraph on 1 line.""",

"""<p>This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.</p>

<p>1 tab to separate them and a new long long long long long long long long long long long long long long long long paragraph on 1 line.</p>"""
),

IO("2-paragraphs-line",
"""This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.

A new long long long long long long long long long long long long long long long long paragraph on 1 line.""",

"""<p>This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.</p>

<p>A new long long long long long long long long long long long long long long long long paragraph on 1 line.</p>"""
),

IO("EOL-CR+LF",
"""These lines all end with end of line (EOL) sequences.

Seriously, they really do.

If you don't believe me: HEX EDIT!

""",

"""<p>These lines all end with end of line (EOL) sequences.</p>

<p>Seriously, they really do.</p>

<p>If you don't believe me: HEX EDIT!</p>"""
),

IO("EOL-CR",
"""These lines all end with end of line (EOL) sequences.Seriously, they really do.If you don't believe me: HEX EDIT!""",

"""<p>These lines all end with end of line (EOL) sequences.</p><p>Seriously, they really do.</p><p>If you don't believe me: HEX EDIT!</p>"""
),

IO("EOL-LF",
"""These lines all end with end of line (EOL) sequences.

Seriously, they really do.

If you don't believe me: HEX EDIT!

""",

"""<p>These lines all end with end of line (EOL) sequences.</p>

<p>Seriously, they really do.</p>

<p>If you don't believe me: HEX EDIT!</p>"""
),

IO("ampersand-text-flow",
"""An ampersand & in the text flow is escaped as an html entity.""",

"""<p>An ampersand &amp; in the text flow is escaped as an html entity.</p>"""
),

IO("ampersand-uri",
"""There is an [ampersand](http://validator.w3.org/check?uri=http://www.w3.org/&verbose=1) in the URI.""",

"""<p>There is an <a href="http://validator.w3.org/check?uri=http://www.w3.org/&amp;verbose=1">ampersand</a> in the URI.</p>"""
),

IO("asterisk-near-text",
"""This is \*an asterisk which should stay as is.""",

"""<p>This is *an asterisk which should stay as is.</p>"""
),

IO("asterisk",
"""This is * an asterisk which should stay as is.""",

"""<p>This is * an asterisk which should stay as is.</p>"""
),

IO("backslash-escape",
"""\\   backslash
\`   backtick
\*   asterisk
\_   underscore
\{\}  curly braces
\[\]  square brackets
\(\)  parentheses
\#   hash mark
\+   plus sign
\-   minus sign (hyphen)
\.   dot
\!   exclamation mark""",

"""<p>\   backslash
`   backtick
*   asterisk
_   underscore
{}  curly braces
[]  square brackets
()  parentheses
#   hash mark
+   plus sign
-   minus sign (hyphen)
.   dot
!   exclamation mark</p>"""
),

IO("blockquote-added-markup",
"""> # heading level 1
> 
> paragraph""",

"""<blockquote>
<h1>heading level 1</h1>

<p>paragraph</p>
</blockquote>"""
),

IO("blockquote-line-2-paragraphs",
""">A blockquote with a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long line.

>and a second very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long line.""",

"""<blockquote>
<p>A blockquote with a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long line.</p>

<p>and a second very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long line.</p>
</blockquote>"""
),

IO("blockquote-line",
""">This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph in a blockquote.""",

"""<blockquote>
<p>This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph in a blockquote.</p>
</blockquote>"""
),

IO("blockquote-multiline-1-space-begin",
"""> A blockquote
> on multiple lines
> like this.""",

"""<blockquote>
<p>A blockquote
on multiple lines
like this.</p>
</blockquote>"""
),

IO("blockquote-multiline-1-space-end",
""">A blockquote 
>on multiple lines 
>like this. """,

"""<blockquote>
<p>A blockquote 
on multiple lines 
like this. </p>
</blockquote>"""
),

IO("blockquote-multiline-2-paragraphs",
""">A blockquote
>on multiple lines
>like this.
>
>But it has
>two paragraphs.""",

"""<blockquote>
<p>A blockquote
on multiple lines
like this.</p>

<p>But it has
two paragraphs.</p>
</blockquote>"""
),

IO("blockquote-multiline",
""">A blockquote
>on multiple lines
>like this""",

"""<blockquote>
<p>A blockquote
on multiple lines
like this</p>
</blockquote>"""
),

IO("blockquote-nested-multiplereturn-level1",
"""> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.
""",

"""<blockquote>
<p>This is the first level of quoting.</p>

<blockquote>
<p>This is nested blockquote.</p>
</blockquote>

<p>Back to the first level.</p>
</blockquote>"""
),

IO("blockquote-nested-multiplereturn",
"""> This is the first level of quoting.
>
> > This is nested blockquote.""",

"""<blockquote>
<p>This is the first level of quoting.</p>

<blockquote>
<p>This is nested blockquote.</p>
</blockquote>
</blockquote>"""
),

IO("blockquote-nested-return-level1",
"""> This is the first level of quoting.
> > This is nested blockquote.
> Back to the first level.
""",

"""<blockquote>
<p>This is the first level of quoting.</p>

<blockquote>
<p>This is nested blockquote.
Back to the first level.</p>
</blockquote>
</blockquote>"""
),

IO("blockquote-nested",
"""> This is the first level of quoting.
> > This is nested blockquote.
""",

"""<blockquote>
<p>This is the first level of quoting.</p>

<blockquote>
<p>This is nested blockquote.</p>
</blockquote>
</blockquote>"""
),

IO("code-1-tab",
"""	10 PRINT HELLO INFINITE
	20 GOTO 10""",

"""<pre><code>10 PRINT HELLO INFINITE
20 GOTO 10
</code></pre>"""
),

IO("code-4-spaces-escaping",
"""    10 PRINT < > &
    20 GOTO 10""",

"""<pre><code>10 PRINT &lt; &gt; &amp;
20 GOTO 10
</code></pre>"""
),

IO("code-4-spaces",
"""    10 PRINT HELLO INFINITE
    20 GOTO 10""",

"""<pre><code>10 PRINT HELLO INFINITE
20 GOTO 10
</code></pre>"""
),

IO("em-middle-word",
"""as*te*risks""",

"""<p>as<em>te</em>risks</p>"""
),

IO("em-star",
"""*single asterisks*""",

"""<p><em>single asterisks</em></p>"""
),

IO("em-underscore",
"""_single underscores_""",

"""<p><em>single underscores</em></p>"""
),

IO("entities-text-flow",
"""HTML entities are written using ampersand notation: &copy;""",

"""<p>HTML entities are written using ampersand notation: &copy;</p>"""
),

IO("header-level1-equal-underlined",
"""This is an H1
=============""",

"""<h1>This is an H1</h1>"""
),

IO("header-level1-hash-sign-closed",
"""# This is an H1 #""",

"""<h1>This is an H1</h1>"""
),

IO("header-level1-hash-sign-trailing-1-space",
""" # This is an H1""",

"""<p># This is an H1</p>"""
),

IO("header-level1-hash-sign-trailing-2-spaces",
"""# this is an h1 with two trailing spaces  
A new paragraph.""",

"""<h1>this is an h1 with two trailing spaces</h1>

<p>A new paragraph.</p>"""
),

IO("header-level1-hash-sign",
"""# This is an H1""",

"""<h1>This is an H1</h1>"""
),

IO("header-level2-dash-underlined",
"""This is an H2
-------------""",

"""<h2>This is an H2</h2>"""
),

IO("header-level2-hash-sign-closed",
"""## This is an H2 ##""",

"""<h2>This is an H2</h2>"""
),

IO("header-level2-hash-sign",
"""## This is an H2""",

"""<h2>This is an H2</h2>"""
),

IO("header-level3-hash-sign-closed",
"""### This is an H3 ###""",

"""<h3>This is an H3</h3>"""
),

IO("header-level3-hash-sign",
"""### This is an H3""",

"""<h3>This is an H3</h3>"""
),

IO("header-level4-hash-sign-closed",
"""#### This is an H4 ####""",

"""<h4>This is an H4</h4>"""
),

IO("header-level4-hash-sign",
"""#### This is an H4""",

"""<h4>This is an H4</h4>"""
),

IO("header-level5-hash-sign-closed",
"""##### This is an H5 #####""",

"""<h5>This is an H5</h5>"""
),

IO("header-level5-hash-sign",
"""##### This is an H5""",

"""<h5>This is an H5</h5>"""
),

IO("header-level6-hash-sign-closed",
"""###### This is an H6  ######""",

"""<h6>This is an H6</h6>"""
),

IO("header-level6-hash-sign",
"""###### This is an H6""",

"""<h6>This is an H6</h6>"""
),

IO("horizontal-rule-3-dashes-spaces",
"""- - -""",

"""<hr />"""
),

IO("horizontal-rule-3-dashes",
"""---""",

"""<hr />"""
),

IO("horizontal-rule-3-stars",
"""***""",

"""<hr />"""
),

IO("horizontal-rule-3-underscores",
"""___""",

"""<hr />"""
),

IO("horizontal-rule-7-dashes",
"""-------""",

"""<hr />"""
),

IO("img-idref-title",
"""![HTML5][h5]

[h5]: http://www.w3.org/html/logo/img/mark-word-icon.png "HTML5 for everyone"""",

"""<p><img src="http://www.w3.org/html/logo/img/mark-word-icon.png" alt="HTML5" title="HTML5 for everyone" /></p>"""
),

IO("img-idref",
"""![HTML5][h5]

[h5]: http://www.w3.org/html/logo/img/mark-word-icon.png""",

"""<p><img src="http://www.w3.org/html/logo/img/mark-word-icon.png" alt="HTML5" /></p>"""
),

IO("img-title",
"""![HTML5](http://www.w3.org/html/logo/img/mark-word-icon.png "HTML5 logo for everyone")""",

"""<p><img src="http://www.w3.org/html/logo/img/mark-word-icon.png" alt="HTML5" title="HTML5 logo for everyone" /></p>"""
),

IO("img",
"""![HTML5](http://www.w3.org/html/logo/img/mark-word-icon.png)""",

"""<p><img src="http://www.w3.org/html/logo/img/mark-word-icon.png" alt="HTML5" /></p>"""
),

IO("inline-code-escaping-entities",
"""We love `<code> and &` for everything""",

"""<p>We love <code>&lt;code&gt; and &amp;</code> for everything</p>"""
),

IO("inline-code-with-visible-backtick",
"""``We love `code` for everything``""",

"""<p><code>We love `code` for everything</code></p>"""
),

IO("inline-code",
"""``We love `code` for everything``""",

"""<p><code>We love `code` for everything</code></p>"""
),

IO("line-break-2-spaces",
"""A first sentence  
and a line break.""",

"""<p>A first sentence<br />
and a line break.</p>"""
),

IO("line-break-5-spaces",
"""A first sentence     
and a line break.""",

"""<p>A first sentence<br />
and a line break.</p>"""
),

IO("link-automatic-email",
"""This is an automatic email link <foolspam@example.org>""",

"""<p>This is an automatic email link <a href="&#x6d;&#x61;&#105;&#x6c;&#116;&#x6f;&#x3a;&#102;&#111;&#x6f;&#x6c;&#x73;&#x70;&#x61;&#x6d;&#x40;&#101;&#120;&#x61;&#x6d;&#112;&#x6c;&#101;&#46;&#x6f;&#114;&#x67;">&#x66;&#x6f;&#x6f;&#x6c;&#x73;&#112;&#x61;&#109;&#64;&#101;&#x78;&#97;&#x6d;&#112;&#x6c;&#101;&#x2e;&#x6f;&#x72;&#x67;</a></p>"""
),

IO("link-automatic",
"""This is an automatic link <http://www.w3.org/>""",

"""<p>This is an automatic link <a href="http://www.w3.org/">http://www.w3.org/</a></p>"""
),

IO("link-bracket-paranthesis-title",
"""[W3C](http://www.w3.org/ "Discover w3c")""",

"""<p><a href="http://www.w3.org/" title="Discover w3c">W3C</a></p>"""
),

IO("link-bracket-paranthesis",
"""[W3C](http://www.w3.org/)""",

"""<p><a href="http://www.w3.org/">W3C</a></p>"""
),

IO("link-idref-angle-bracket",
"""[World Wide Web Consortium][w3c]

[w3c]: <http://www.w3.org/>""",

"""<p><a href="http://www.w3.org/">World Wide Web Consortium</a></p>"""
),

IO("link-idref-implicit-spaces",
"""[World Wide Web Consortium][]

[World Wide Web Consortium]: http://www.w3.org/""",

"""<p><a href="http://www.w3.org/">World Wide Web Consortium</a></p>"""
),

IO("link-idref-implicit",
"""[w3c][]

[w3c]: http://www.w3.org/""",

"""<p><a href="http://www.w3.org/">w3c</a></p>"""
),

IO("link-idref-space",
"""[World Wide Web Consortium] [w3c]

[w3c]: http://www.w3.org/""",

"""<p><a href="http://www.w3.org/">World Wide Web Consortium</a></p>"""
),

IO("link-idref-title-next-line",
"""[World Wide Web Consortium][w3c]

[w3c]: http://www.w3.org/
   "Discover W3C"""",

"""<p><a href="http://www.w3.org/" title="Discover W3C">World Wide Web Consortium</a></p>"""
),

IO("link-idref-title-paranthesis",
"""[World Wide Web Consortium][w3c]

[w3c]: http://www.w3.org/ (Discover w3c)""",

"""<p><a href="http://www.w3.org/" title="Discover w3c">World Wide Web Consortium</a></p>"""
),

IO("link-idref-title-single-quote",
"""[World Wide Web Consortium][w3c]

[w3c]: http://www.w3.org/ 'Discover w3c'""",

"""<p><a href="http://www.w3.org/" title="Discover w3c">World Wide Web Consortium</a></p>"""
),

IO("link-idref-title",
"""[World Wide Web Consortium][w3c]

[w3c]: http://www.w3.org/ "Discover w3c"""",

"""<p><a href="http://www.w3.org/" title="Discover w3c">World Wide Web Consortium</a></p>"""
),

IO("link-idref",
"""[World Wide Web Consortium][w3c]

[w3c]: http://www.w3.org/""",

"""<p><a href="http://www.w3.org/">World Wide Web Consortium</a></p>"""
),

IO("list-blockquote",
"""*   a list containing a blockquote

    > this the blockquote in the list""",

"""<ul>
<li><p>a list containing a blockquote</p>

<blockquote>
<p>this the blockquote in the list</p>
</blockquote></li>
</ul>
"""
),

IO("list-code",
"""*   a list containing a block of code

	    10 PRINT HELLO INFINITE
	    20 GOTO 10""",

"""<ul>
<li><p>a list containing a block of code</p>

<pre><code>10 PRINT HELLO INFINITE
20 GOTO 10
</code></pre></li>
</ul>"""
),

IO("list-multiparagraphs-tab",
"""*   This is a list item with two paragraphs. Lorem ipsum dolor
	sit amet, consectetuer adipiscing elit. Aliquam hendrerit
	mi posuere lectus.

	Vestibulum enim wisi, viverra nec, fringilla in, laoreet
	vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
	sit amet velit.

*   Suspendisse id sem consectetuer libero luctus adipiscing.""",

"""<ul>
<li><p>This is a list item with two paragraphs. Lorem ipsum dolor
sit amet, consectetuer adipiscing elit. Aliquam hendrerit
mi posuere lectus.</p>

<p>Vestibulum enim wisi, viverra nec, fringilla in, laoreet
vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
sit amet velit.</p></li>
<li><p>Suspendisse id sem consectetuer libero luctus adipiscing.</p></li>
</ul>"""
),

IO("list-multiparagraphs",
"""*   This is a list item with two paragraphs. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

*   Suspendisse id sem consectetuer libero luctus adipiscing.""",

"""<ul>
<li><p>This is a list item with two paragraphs. Lorem ipsum dolor
sit amet, consectetuer adipiscing elit. Aliquam hendrerit
mi posuere lectus.</p>

<p>Vestibulum enim wisi, viverra nec, fringilla in, laoreet
vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
sit amet velit.</p></li>
<li><p>Suspendisse id sem consectetuer libero luctus adipiscing.</p></li>
</ul>"""
),

IO("ordered-list-escaped",
"""1\. ordered list escape""",

"""<p>1. ordered list escape</p>"""
),

IO("ordered-list-items-random-number",
"""1. list item 1
8. list item 2
1. list item 3""",

"""<ol>
<li>list item 1</li>
<li>list item 2</li>
<li>list item 3</li>
</ol>"""
),

IO("ordered-list-items",
"""1. list item 1
2. list item 2
3. list item 3""",

"""<ol>
<li>list item 1</li>
<li>list item 2</li>
<li>list item 3</li>
</ol>"""
),

IO("paragraph-hard-return",
"""This is a paragraph
on multiple lines
with hard return.""",

"""<p>This is a paragraph
on multiple lines
with hard return.</p>"""
),

IO("paragraph-line",
"""This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.""",

"""<p>This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph on 1 line.</p>"""
),

IO("paragraph-trailing-leading-spaces",
""" This is a paragraph with a trailing and leading space. """,

"""<p>This is a paragraph with a trailing and leading space. </p>"""
),

IO("paragraph-trailing-tab",
"""This is a paragraph with 1 trailing tab.	""",

"""<p>This is a paragraph with 1 trailing tab.    </p>"""
),

IO("paragraphs-2-leading-spaces",
"""  This is a paragraph with 2 leading spaces.""",

"""<p>This is a paragraph with 2 leading spaces.</p>"""
),

IO("paragraphs-3-leading-spaces",
"""   This is a paragraph with 3 leading spaces.""",

"""<p>This is a paragraph with 3 leading spaces.</p>"""
),

IO("paragraphs-leading-space",
""" This is a paragraph with 1 leading space.""",

"""<p>This is a paragraph with 1 leading space.</p>"""
),

IO("paragraphs-trailing-spaces",
"""This is a paragraph with a trailing space. """,

"""<p>This is a paragraph with a trailing space. </p>"""
),

IO("strong-middle-word",
"""as**te**risks""",

"""<p>as<strong>te</strong>risks</p>"""
),

IO("strong-star",
"""**double asterisks**""",

"""<p><strong>double asterisks</strong></p>"""
),

IO("strong-underscore",
"""__double underscores__""",

"""<p><strong>double underscores</strong></p>"""
),

IO("unordered-list-items-asterisk",
"""* list item 1
* list item 2
* list item 3
""",

"""<ul>
<li>list item 1</li>
<li>list item 2</li>
<li>list item 3</li>
</ul>"""
),

IO("unordered-list-items-dashsign",
"""- list item 1
- list item 2
- list item 3""",

"""<ul>
<li>list item 1</li>
<li>list item 2</li>
<li>list item 3</li>
</ul>"""
),

IO("unordered-list-items-leading-1space",
""" * list item 1
 * list item 2
 * list item 3""",

"""<ul>
<li>list item 1</li>
<li>list item 2</li>
<li>list item 3</li>
</ul>
"""
),

IO("unordered-list-items-leading-2spaces",
"""  * list item 1
  * list item 2
  * list item 3""",

"""<ul>
<li>list item 1</li>
<li>list item 2</li>
<li>list item 3</li>
</ul>"""
),

IO("unordered-list-items-leading-3spaces",
"""   * list item 1
   * list item 2
   * list item 3""",

"""<ul>
<li>list item 1</li>
<li>list item 2</li>
<li>list item 3</li>
</ul>"""
),

IO("unordered-list-items-plussign",
"""+ list item 1
+ list item 2
+ list item 3""",

"""<ul>
<li>list item 1</li>
<li>list item 2</li>
<li>list item 3</li>
</ul>"""
),

IO("unordered-list-paragraphs",
"""* list item in paragraph

* another list item in paragraph""",

"""<ul>
<li><p>list item in paragraph</p></li>
<li><p>another list item in paragraph</p></li>
</ul>"""
),

IO("unordered-list-unindented-content",
"""*   This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph in a list.
*   and yet another long long long long long long long long long long long long long long long long long long long long long long line.""",

"""<ul>
<li>This a very long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long long paragraph in a list.</li>
<li>and yet another long long long long long long long long long long long long long long long long long long long long long long line.</li>
</ul>"""
),

IO("unordered-list-with-indented-content",
"""*   This is a list item
    with the content on
    multiline and indented.
*   And this another list item
    with the same principle.""",

"""<ul>
<li>This is a list item
with the content on
multiline and indented.</li>
<li>And this another list item
with the same principle.</li>
</ul>"""
),
]

extensions = [
IO("fenced-code-block-p",
"""```
a
```""",
"""<p><code>a</code></p>"""
),

IO("fenced-code-block-pre",
"""```
a
```""",
"""<pre><code>a</code></pre>"""
),

IO("url-autolink",
"""https://a""",
"""<a href="https://a">https://a</a>""",
[pandoc('+')]
),

IO("utf8",
"""€""",
"""<p>€</p>"""
),
]
