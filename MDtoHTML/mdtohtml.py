from pathlib import *
from markdown2 import *

filesinthefolder = sorted(Path('../MDtoHTML/fichiers_markdown').glob('*.md'))
markdowner = Markdown()

if (Path('../MDtoHTML/fichiers_html').exists()) == False:
    Path('../MDtoHTML/fichiers_html').mkdir()

for filemd in filesinthefolder:
    name_file = PurePosixPath(filemd).stem
    filehtml = open("../MDtoHTML/fichiers_html/"+ name_file +".html", "a")
    filehtml.write(markdowner.convert(markdown_path(filemd)))
    filehtml.close()