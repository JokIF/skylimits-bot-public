import click
import logging


@click.group()
@click.option("-d", "--debug", "debug", is_flag=True, default=False)
def cli(debug):
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    import core.init as init
    init.setup()


@cli.command()
def start():
    from core.init import dp, bot
    dp.run_polling(bot)