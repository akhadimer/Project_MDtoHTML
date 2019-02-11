from pathlib import *
from markdown2 import *
import click

#if (Path('../fichiers_html').exists()) = false:
pathlib.Path("fichiers_html").mkdir()

filesinthefolder = sorted(Path('B:/Bureau/ynov/B1/python/projet_markdown_to_html/fichiers_markdown').glob('*.md'))
markdowner = Markdown()
for filemd in filesinthefolder:
    name_file = PurePosixPath(filemd).stem
    filehtml = open("B:/Bureau/ynov/B1/python/projet_markdown_to_html/fichiers_html/"+ name_file +".html", "a")
    filehtml.write(markdowner.convert(markdown_path(filemd)))
    filehtml.close()