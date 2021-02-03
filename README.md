# ma2buzzer
 Python to Execute MA2 commands based off the contents of a text file
 
 Use case is that a user visits a web-page (can be hosted on the same web server) and upon clicking their buzzer, a PHP script will change the text file contents to "A" or "B" (in this case the text BMFL was used.
 
 Python script routinely checks this file and when it reads a contents of A or B, it will push executor 1 to 100 (can be cloned indefinitely for file contents and executor) via MA2's telnet functionality
 
 Script then wipes the file via FTP ready for the next question
