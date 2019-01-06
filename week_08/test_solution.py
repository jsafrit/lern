#!/usr/bin/env python3

from solution import create_math_problems, solve_math_problems


def test_create_math_problems(tmpdir):
    d = tmpdir / 'sub'
    d.mkdir()
    f = d / 'test-problems.txt'
    create_math_problems(open(f, 'w'))


def test_solve_problems_from_file(capsys, tmpdir):
    d = tmpdir / 'sub'
    d.mkdir()
    f = d / 'test-problems.txt'
    create_math_problems(open(f, 'w'))
    solve_math_problems(open(f))
    captured_out, captured_err = capsys.readouterr()
    assert len(captured_out.split('\n')) == 101
