# markdown-editing

Editing markup and comments within Markdown.

```
This is a +{new} addition

This -{this} word is removed

I say, ~{out with the old}{*in* with the new}

Here !{just a comment} is a line with a comment

You can also ?{add comments to some text}(Like *this*!{And comment within comments}!{You can thread them that way} (2020-04-21))

All -{new}(Redundant (Makyo)) edit marks can have comments with attributions and dates +{like this}(See? (Makyo 2020-04-22)) (for single comments, just put the attribution in there !{like this}(Makyo))

Bottom text
```

Leads to:

```html
<p>This is a <ins class="addition">new</ins> addition</p>
<p>This <del class="deletion">this</del> word is removed</p>
<p>I say, <span class="substitution"><del>out with the old</del><ins><em>in</em> with the new</ins></span></p>
<p>Here <q class="comment">just a comment</q> is a line with a comment</p>
<p>You can also <mark class="selected">add comments to some text<q class="comment">Like <em>this</em><q class="comment">And comment within comments</q><q class="comment">You can thread them that way</q><span class="attribution">2020-04-21</span></q></mark></p>
<p>All <del class="deletion">new<q class="comment">Redundant<span class="attribution">Makyo</span></q></del> edit marks can have comments with attributions and dates <ins class="addition">like this<q class="comment">See?<span class="attribution">Makyo</span><span class="date">2020-04-22</span></q></ins> (for single comments, just put the attribution in there <q class="comment">like this<span class="attribution">Makyo</span></q>)</p>
<p>Bottom text</p>
```

It will take some styling to get it looking right. You can see a sample image [here](https://github.com/makyo/markdown-editing/blob/master/sample.png) which is generated using [this stylesheet](https://github.com/makyo/markdown-editing/blob/master/sample.css)
