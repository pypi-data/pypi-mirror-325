import os
from typing import Union
import pygments
from pygments.lexers.markup import MarkdownLexer
from prompt_toolkit.formatted_text import PygmentsTokens
from prompt_toolkit import print_formatted_text
from pygments.styles import get_style_by_name
from prompt_toolkit.styles.pygments import style_from_pygments_cls
from agentmake import DEFAULT_MARKDOWN_THEME

def readTextFile(textFile: str) -> Union[str, None]:
    if not os.path.isfile(textFile):
        return None
    with open(textFile, 'r', encoding='utf8') as fileObj:
        content = fileObj.read()
    return content if content else ""

def writeTextFile(textFile: str, textContent: str) -> None:
    with open(textFile, "w", encoding="utf-8") as fileObj:
        fileObj.write(textContent)

def getPygmentsStyle():
    """
    from pygments.styles import get_all_styles
    styles = list(get_all_styles())
    print(styles)
    ['abap', 'algol', 'algol_nu', 'arduino', 'autumn', 'bw', 'borland', 'coffee', 'colorful', 'default', 'dracula', 'emacs', 'friendly_grayscale', 'friendly', 'fruity', 'github-dark', 'gruvbox-dark', 'gruvbox-light', 'igor', 'inkpot', 'lightbulb', 'lilypond', 'lovelace', 'manni', 'material', 'monokai', 'murphy', 'native', 'nord-darker', 'nord', 'one-dark', 'paraiso-dark', 'paraiso-light', 'pastie', 'perldoc', 'rainbow_dash', 'rrt', 'sas', 'solarized-dark', 'solarized-light', 'staroffice', 'stata-dark', 'stata-light', 'tango', 'trac', 'vim', 'vs', 'xcode', 'zenburn']
    """
    return style_from_pygments_cls(get_style_by_name(DEFAULT_MARKDOWN_THEME))

def highlightMarkdownSyntax(content):
    try:
        tokens = list(pygments.lex(content, lexer=MarkdownLexer()))
        print_formatted_text(PygmentsTokens(tokens), style=getPygmentsStyle())
    except:
        print(content)