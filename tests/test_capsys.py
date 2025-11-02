import pytest

from src.decorators import log


@log()
def success_func(a, b):
    return a + b


@log()
def fail_func(a, b):
    return a / b


@log(filename="test_log.txt")
def file_success_func(x):
    return x * 2


@log(filename="test_log.txt")
def file_fail_func(x):
    raise ValueError("fail!")


def test_log_console_success(capsys):
    assert success_func(2, 3) == 5
    captured = capsys.readouterr()
    assert "success_func ok" in captured.out


def test_log_console_failure(capsys):
    with pytest.raises(ZeroDivisionError):
        fail_func(1, 0)
    captured = capsys.readouterr()
    assert "fail_func error: ZeroDivisionError. Inputs: (1, 0), {}" in captured.out


def test_log_file_success(tmp_path):
    log_file = tmp_path / "mylog.txt"

    # Переопределим функцию с новым файлом
    @log(filename=str(log_file))
    def temp_func(a):
        return a

    temp_func(123)
    with open(log_file, encoding='utf-8') as f:
        assert "temp_func ok" in f.read()


def test_log_file_failure(tmp_path):
    log_file = tmp_path / "errlog.txt"

    @log(filename=str(log_file))
    def temp_fail(a):
        raise RuntimeError("fail!")

    with pytest.raises(RuntimeError):
        temp_fail(77)
    with open(log_file, encoding='utf-8') as f:
        content = f.read()
        assert "temp_fail error: RuntimeError. Inputs: (77,), {}" in content
