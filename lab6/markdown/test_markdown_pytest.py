'''
Test markdown.py with nose or pytest

To run tests: py.test             test_markdown_pytest.py
          or: python -m pytest    test_markdown_pytest.py
Verbose (-v): py.test -v          test_markdown_pytest.py
          or: python -m pytest -v test_markdown_pytest.py
'''

from markdown_adapter import run_markdown

def test_non_marked_lines():
    print ('in test_non_marked_lines')
    assert run_markdown('this line has no special handling') == '<p>this line has no special handling</p>'

def test_em():
    print ('in test_em')
    assert run_markdown('*this should be wrapped in em tags*') == '<p><em>this should be wrapped in em tags</em></p>'
    assert run_markdown('_this should be wrapped in em tags_') == '<p><em>this should be wrapped in em tags</em></p>'

def test_strong():
    print ('in test_strong')
    assert run_markdown('**this should be wrapped in strong tags**') == '<p><strong>this should be wrapped in strong tags</strong></p>'
    assert run_markdown('__this should be wrapped in strong tags__') == '<p><strong>this should be wrapped in strong tags</strong></p>'

def test_h3():
    print ('in test_h3')
    assert run_markdown('###this should be wrapped in h3 tags') == '<p><h3>this should be wrapped in h3 tags</h3></p>'

def test_h2():
    print ('in test_h2')
    assert run_markdown('##this should be wrapped in h3 tags') == '<p><h2>this should be wrapped in h3 tags</h2></p>'

def test_h1():
    print ('in test_h1')
    assert run_markdown('#this should be wrapped in h3 tags') == '<p><h1>this should be wrapped in h3 tags</h1></p>'

def test_block():
    print ('in test_block')
    assert run_markdown('>this should be wrapped in \n>blockquote tags\n but this should not') == '<blockquote><p>this should be wrapped in</p> <p>blockquote tags</p> </blockquote><p> but this should not</p>'
