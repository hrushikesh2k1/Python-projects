## opening a file
```
file = open("<file-name>") #This will open the file in read mode default
```
## printing the contents of the file
```
file = open("<file-name>")
contents = file.read()
print(contents)
```
## writing to file
```
file = open("<file-name>", "w") #opening a file in write mode
file.write("i am writing to file") #This will remove all the existing contents of a file. It will create a file if not exists
```
## appending the text to file
```
file = open("<file-name>", "a")
file.write("I am appending this text")
```
## Obsolute file path
It is the file path which is starting from root/origin.

## Relative file path
The file path from the working directory.
