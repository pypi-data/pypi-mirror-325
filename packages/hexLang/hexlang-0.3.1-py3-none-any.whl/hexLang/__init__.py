"""hexLang"""
from . import ast, lexer, parser, runner, utils

__all__ = ["parser", "ast", "lexer", "runner", "utils"]

__version__ = "0.3.1"
__version_str__ = (
    f"hexLang v{__version__}."
    + "\nHexLang is an esoteric language inspired and based on the Riot Games Arcane Netflix series."
    + "\nCreated by Viraj Patel (https://github.com/virajp4)."
)

rpp = runner.RppRunner()
