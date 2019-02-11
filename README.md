# Project_MDtoHTML
Thomas Dumont

## Instructions 
Pour faire fonctionner l'ensemble du projet, merci d'utiliser tout le dossier "MDtoHTML".
Pour transformer vos fichiers markdown en HTML, les mettres dans le dossier "fichiers_markdown" et executer le programme "mdtohtml.py", les fichiers HTML générés seront ensuite envoyé dans un dossier qui se créera automatiquement s'il n'ai pas déjà créé nommé "fichiers_html".

## Présentation du code

Dans un premier temps j'importe deux bibliothèques, une pour manipuler les chemins windows qui s'appelle "pathlib" et l'autre qui s'appelle "markdown2" permettant de transformer du texte en format markdown en format HTML.

Dans un second temps je demande de stocker dans un tableau tous les chemins des fichiers markdown présent dans le dossier "fichiers_mardown". J'utilise en même temps la fonction "sorted" qui permet de trier.
J'attribue la fonction "Markdown()" à la variable "markdowner"

Dans un troisième temps je place une condition qui créer le dossier "fichiers_html" s'il n'est pas créer, il sera utilisé pour stocker les fichiers html généré depuis le markdown.

Dans un quatrième et dernier temps je créer une condition for qui va appliquer un traitement à chaque fichier markdown présent dans le dossier "fichiers_markdown".

"filemd" contient donc à chaque tour de boucle un des éléments du tableau "filesinthefolder" par ordre où ils sont triés.

On attribue à "name_file" : "PurePosixPath(filemd).stem" qui va permettre de seulement garder le nom du fichier markdown sans l'extension à la fin pour pouvoir donner ce nom de fichier au fichier HTML qui sera généré.
Ensuite grâce à la fonction "open", on ouvre notre fichier HTML qui sera créé par la même occasion, grâce à "+ name_file +" on lui attribu le nom de du fichier markdown que l'on transforme.

Ensuite on écrit dans ce même fichier, grâce à la fonction "markdowner.convert" on converti notre fichier markdown.
La fonction "markdown_path" permet de renseigner que ce que l'on donne au convertisseur et le chemin d'un fichier.
Et ensuite on ferme notre fichier HTML comme on l'a ouvert juste avant.
