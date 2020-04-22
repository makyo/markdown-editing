from markdown import markdown
from unittest import TestCase

from markdown_editing.extension import EditingExtension


class TestExtension(TestCase):
    def test_substitution(self):
        source = '~{out with the old}{in with the new}'

        expected = '<p><span class="substitution"><del>out with the old</del><ins>in with the new</ins></span></p>'

        html = markdown(source, extensions=[EditingExtension()])
        self.assertEqual(html, expected)

        # Only need to test this once.
        html = markdown(source, extensions=['markdown_editing'])
        self.assertEqual(html, expected)

    def test_addition(self):
        source = 'foo +{bar} baz +{qux}(yap)'
        expected = '<p>foo <ins class="addition">bar</ins> baz <ins class="addition">qux<q class="comment">yap</q></ins></p>'

        html = markdown(source, extensions=[EditingExtension()])
        self.assertEqual(html, expected)

    def test_deletion(self):
        source = 'foo -{bar} baz -{qux}(yap)'
        expected = '<p>foo <del class="deletion">bar</del> baz <del class="deletion">qux<q class="comment">yap</q></del></p>'

        html = markdown(source, extensions=[EditingExtension()])
        self.assertEqual(html, expected)

    def test_selected(self):
        source = 'foo ?{bar}(qux) baz'
        expected = '<p>foo <mark class="selected">bar<q class="comment">qux</q></mark> baz</p>'

        html = markdown(source, extensions=[EditingExtension()])
        self.assertEqual(html, expected)

    def test_comments(self):
        self.maxDiff = None
        source = """
* Substitution: ~{out with the old}{in with the new}
* With comment: ~{out with the old}{in with the new}(is what I always say)
* With attribution: ~{out with the old}{in with the new}(is what I always say (Makyo))
* With date: ~{out with the old}{in with the new}(is what I always say (Makyo 2020-04-21))
* Comment thread: +{Foxes}(More foxes are always good)!{SGTM}
* Comment with attribution: !{SGTM}(Makyo 2020-04-22)
        """.strip()

        expected = """
<ul>
<li>Substitution: <span class="substitution"><del>out with the old</del><ins>in with the new</ins></span></li>
<li>With comment: <span class="substitution"><del>out with the old</del><ins>in with the new</ins><q class="comment">is what I always say</q></span></li>
<li>With attribution: <span class="substitution"><del>out with the old</del><ins>in with the new</ins><q class="comment">is what I always say<span class="attribution">Makyo</span></q></span></li>
<li>With date: <span class="substitution"><del>out with the old</del><ins>in with the new</ins><q class="comment">is what I always say<span class="attribution">Makyo</span><span class="date">2020-04-21</span></q></span></li>
<li>Comment thread: <ins class="addition">Foxes<q class="comment">More foxes are always good</q></ins><q class="comment">SGTM</q></li>
<li>Comment with attribution: <q class="comment">SGTM<span class="attribution">Makyo</span><span class="date">2020-04-22</span></q></li>
</ul>
        """.strip()

        html = markdown(source, extensions=[EditingExtension()])
        self.assertEqual(html, expected)

    def test_level(self):
        source = """
```
?{Some text}(bad wolf)
```

    ?{Some text}(bad wolf)

> ?{Some text}(good doggy)
        """.strip()

        expected = """
<p><code>?{Some text}(bad wolf)</code></p>
<pre><code>?{Some text}(bad wolf)
</code></pre>
<blockquote>
<p><mark class="selected">Some text<q class="comment">good doggy</q></mark></p>
</blockquote>
        """.strip()

        html = markdown(source, extensions=[EditingExtension()])
        self.assertEqual(html, expected)

    def test_nesting(self):
        source = """
?{The only currently working form of nesting}(But what if...!{NO})
        """.strip()

        expected = """
<p><mark class="selected">The only currently working form of nesting<q class="comment">But what if...<q class="comment">NO</q></q></mark></p>
        """.strip()

        html = markdown(source, extensions=[EditingExtension()])
        self.assertEqual(html, expected)

    def test_mixed(self):
        source = """
+{some *fancy* new stuff}(With a **fancy** comment)
        """.strip()

        expected = """
<p><ins class="addition">some <em>fancy</em> new stuff<q class="comment">With a <strong>fancy</strong> comment</q></ins></p>
        """.strip()

        html = markdown(source, extensions=[EditingExtension()])
        self.assertEqual(html, expected)

