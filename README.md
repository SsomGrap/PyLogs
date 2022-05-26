# PyLogs
### A logging package for your python project
***

## Description
PyLogs allow you to add a logger to your python project. This logger can send the logs directly to the terminal and/or save them to an external file. Several options are available, such as :
- format of the logs
- the colorization of the text
- etc...

Work on python 3 and 2. For Windows, macOS and Linux.
***

## Installation
You just need to run this command in your **terminal** : 
```
pip install PyLogs
```
***

## Functions
A list of all functions in this package.
```
pylogs.PyLogs()

pylogs.PyLogs.getFormat()
pylogs.PyLogs.setFormat()

pylogs.PyLogs.colorization()
pylogs.PyLogs.terminalOutput()
pylogs.PyLogs.fileOutput()

pylogs.PyLogs.info()
pylogs.PyLogs.warn()
pylogs.PyLogs.error()
pylogs.PyLogs.critical()
```
***

## Exemple
An example of how to implement PyLogs to your projects
```
import pylogs

pylogs.PyLogs()
```
***

## Credits
developed by *SsomGrap*