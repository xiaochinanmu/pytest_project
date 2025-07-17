def test_reverse_string(sample_string):
    from src.utils import reverse_string
    assert reverse_string("abc") == "cba"
    assert reverse_string(sample_string) == "tsetyp olleh"

def test_capitalize_words(sample_string):
    from src.utils import capitalize_words
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words(sample_string) == "Hello Pytest"