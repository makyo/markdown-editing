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
        expected = '<p>foo <ins class="addition">bar</ins> baz <ins class="addition">qux<aside>yap</aside></ins></p>'

        html = markdown(source, extensions=[EditingExtension()])
        self.assertEqual(html, expected)

    def test_deletion(self):
        source = 'foo -{bar} baz -{qux}(yap)'
        expected = '<p>foo <del class="deletion">bar</del> baz <del class="deletion">qux<aside>yap</aside></del></p>'

        html = markdown(source, extensions=[EditingExtension()])
        self.assertEqual(html, expected)

    def test_selected(self):
        source = 'foo ?{bar}(qux) baz'
        expected = '<p>foo <mark class="selected">bar<aside>qux</aside></mark> baz</p>'

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
        """.strip()

        expected = """
<ul>
<li>Substitution: <span class="substitution"><del>out with the old</del><ins>in with the new</ins></span></li>
<li>With comment: <span class="substitution"><del>out with the old</del><ins>in with the new</ins><aside>is what I always say</aside></span></li>
<li>With attribution: <span class="substitution"><del>out with the old</del><ins>in with the new</ins><aside>is what I always say<span class="attribution">Makyo</span></aside></span></li>
<li>With date: <span class="substitution"><del>out with the old</del><ins>in with the new</ins><aside>is what I always say<span class="attribution">Makyo</span><span class="date">2020-04-21</span></aside></span></li>
<li>Comment thread: <ins class="addition">Foxes<aside>More foxes are always good</aside></ins><aside class="comment">SGTM</aside></li>
</ul>
        """.strip()

        html = markdown(source, extensions=[EditingExtension()])
        self.assertEqual(html, expected)

        html = markdown(source, extensions=['markdown_editing'])
        self.assertEqual(html, expected)
