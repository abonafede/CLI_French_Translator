import pytest
from click.testing import CliRunner
from translator import translate


def test():
    runner = CliRunner()
    result = runner.invoke(translate, ["--text", "my name is andrew"])
    assert result.exit_code == 0
    assert "Mon" in result.output.strip()
    assert "nom" in result.output.strip()
    assert "est" in result.output.strip()
    assert "Andrew" in result.output.strip()

if __name__ == '__main__':
    test()