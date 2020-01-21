import pytest

from facially import cli


def test_argparse_input():
    # calling with no arguments goes to look at sys.argv, which is our arguments to py.test.
    with pytest.raises((SystemExit, NotImplementedError)):
        cli.main()


def test_submit():
    args = ['-s', 'test output']
    cli.main(args)
