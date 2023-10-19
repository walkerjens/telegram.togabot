# togabot

The one and only TO/GA Telegram bot, available on Docker Hub ([miffeltoffel/telegram.togabot](https://hub.docker.com/r/miffeltoffel/telegram.togabot/))

Built on [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

## Code cleaners

For code formatting `black` is used, together with `flake8` and `pylint` for linting.

Run locally to format with

```bash
> make black
black .
All done! ✨ 🍰 ✨
13 files left unchanged.

```

Run locally to check code with

```bash
> make check
black . --diff --check
All done! ✨ 🍰 ✨
16 files would be left unchanged.
pylint togabot

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

flake8 togabot tests
mypy -p togabot
Success: no issues found in 1 source file

```

Alternatively each checker individually with

```bash
> make black-check
black . --diff --check
All done! ✨ 🍰 ✨
13 files would be left unchanged.

> make pep8
flake8 togabot tests

> make lint
pylint togabot

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

> make mypy
mypy -p togabot
Success: no issues found in 1 source file

```

## Tests

Tests are located under `tests`. Run tests locally with

```bash
> make test
pytest -v
==================================================== test session starts ====================================================
platform linux -- Python 3.9.2, pytest-6.2.2, py-1.10.0, pluggy-0.13.1 -- /home/jens/git/miffeltoffel/telegram.togabot/venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/jens/git/miffeltoffel/telegram.togabot
collected 1 item

tests/test_neweventcommand.py::NewEventCommandTest::test_getUpcomingThursdayDate PASSED                              [100%]

===================================================== 1 passed in 0.13s =====================================================

```
