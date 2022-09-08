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
+   name.index    {Nodes, Childs, etc.} = a file

    Example of .index file:
    
    -  `{    
    {name:('name', 1), title:'NAME', val:1, text:(0, 10), tags:['program', 'python', 'project_1']},
    {name:('name', 2), title:'NAME', val:2, text:(10, 20), tags:['design', 'technical']},
      }`
    -   `name = unic composit from: 
        a.  NAME (given by author)(can be more nodes with same NAME)
        b.  a number, begining with 1 (unic number at the same NAME)`
    -   `title = NAME given by author, the name of the node`
    -   `val = indentation of the node: 1=Parent, 2=Child, 3=Child of Child, ...`
    -   `text = from what index to what index is text taken from file "name.text"`
    -   `tags = keywords for a quick search`

+   name.text     {ASCII content, text, (Unicode utf-8)} = a file

    Example of .text file:
    
    First line of text of first node  
    Second line of text   
    Third line of text of second node

+   name.fancy    {html, rtf = formating} = a file
+   name(folder)  {Pictures, Music, Movie, etc. = files} = a Folder
