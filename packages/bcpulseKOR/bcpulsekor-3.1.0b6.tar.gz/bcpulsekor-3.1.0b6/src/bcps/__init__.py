__version__ = "3.1.0b6"

from bcps import core, cli


__all__ = ["core", "cli"]


def run():
    from bcps import __main__

    __main__.main()
