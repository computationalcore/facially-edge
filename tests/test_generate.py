import pytest

from facially.lib import generate


@pytest.mark.parametrize('s,expected', [
    ('world', 'Hello world'),
    ('Vin', 'Hello Vin'),
    ('Facially-targered Ads Platform', 'Hello Facially-targered Ads Platform')
])
def test_generate(s: str, expected: str) -> None:
    assert generate(s) == expected
