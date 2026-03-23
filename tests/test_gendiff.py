import textwrap
from gendiff.scripts.gendiff import generate_diff


class Test:
    def test_generate_diff(self):
        result = generate_diff("file1.json", "file2.json")
        expected = textwrap.dedent("""\
            {
              - follow: False
                host: hexlet.io
              - proxy: 123.234.53.22
              - timeout: 50
              + timeout: 20
              + verbose: True
            }"""
        )
        assert result == expected
