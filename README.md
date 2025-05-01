# Time App

A simple Python app to demonstrate GUI/CLI interface on top of a common base
class whose API is comprised of required subclass methods.

## Installation

First, you need to be sure that tkinter is installed. This is included in the
standard Python installations in Windows and Ubuntu desktop. Verify with
`python3 -m tkinter`. Then you will be able to install and run this app:

```
~$ git clone https://github.com/n8marti/time-app
~$ cd ./time-app
~/time-app$ python3 -m pip install .
```

## Run CLI
```
$ python3 -m time_app cli
Get the time
Get current time? [Y/n]: y
09:04:39 AM
Get current time? [Y/n]:
```

## Run GUI
```
$ python3 -m time_app
```
![initial window](/img/gui-new.png)
![button clicked](/img/gui-clicked.png)

## Run Unimplemented UI
```
$ python3 -m time_app test
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/home/nate/g/time-app/env/lib/python3.12/site-packages/time_app/__main__.py", line 96, in <module>
    app.run()
  File "/home/nate/g/time-app/env/lib/python3.12/site-packages/time_app/__main__.py", line 24, in run
    raise NotImplementedError
NotImplementedError
```