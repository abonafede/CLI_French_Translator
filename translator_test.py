import pytest
from click.testing import CliRunner
from translator import translate


def test():
    runner = CliRunner()
    result = runner.invoke(translate, ["--text", "my name is andrew"])
    assert result.exit_code == 0
    assert "mon" in result.output
    assert "nom" in result.output
    assert "est" in result.output
    assert "andrew" in result.output

if __name__ == '__main__':
    test()