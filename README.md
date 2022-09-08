# PROIECT
## CONTENT AND DEFINITION
The purpose of this PROJECT is to create some portable tools like:
  1. Notepad
  2. PIM
  3. Library
  4. Bible study enviroment
  5. ...
  
## ORGANIZARE
PROIECT(folder) 
+   program_1.bat
+   program_2.bat
+   ...
+   program_n.bat
+   PROGRAM(folder)
    -   program_1.py and PROGRAM_1(folder)
    -   program_2.py and PROGRAM_2(folder)
    -   ...
    -   program_n.py and PROGRAM_n(folder)
+   DATA_BASE_1(folder)
+   DATA_BASE_2(folder)
+   DATA_BASE_BIBLE(folder)
+   ...

## DATA_BASE(folder)
+   name.index    {Nodes, Childs, etc.}
    Example of .index file:
    `
    {
    {name:('name', 1), title:'NAME', val:1, text:(0, 10), tags:['program', 'python', 'project_1']}
    }
+   name.text     {ASCII content, text, (Unicode utf-8)}
+   name.fancy    {html, rtf = formating}
+   name(folder)  {Pictures, Music, Movie, etc. = files}
