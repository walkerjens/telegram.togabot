# ONGAbot

The one and only ON/GA Telegram bot, available on Docker Hub ([tingvarsson/telegram.ongabot](https://hub.docker.com/r/tingvarsson/telegram.ongabot/))

Built on [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

## Code cleaners

For code formatting `black` is used, together with `flake8` and `pylint` for linting.

To run them simply do

```bash
> make black
black .
All done! ✨ 🍰 ✨
13 files left unchanged.

> make pep8
flake8 ongabot tests

> make lint
PYTHONPATH=YTHONPATH:./ongabot pylint ongabot

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

```

## Tests

Tests are located under `tests`. Run tests locally with

```bash
> PYTHONPATH=$PYTHONPATH:./ongabot python -m unittest
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

```
