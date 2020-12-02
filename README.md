# jmessaging

`jmessaging` is a very simple package (with no dependencies!) that makes
printing colorized messages to the console a breeze.

## Usage

```python
import jmessaging as jm

messenger = jm.Messenger()
messenger.info('This is a message')
messenger.warning('This is a warning')
messenger.error('This is an error')
```

would result in

![Example default output][output example]

### Changing the brackets and text color

The brackets around the message type can be changed along with the color
associated with the type

```python
import jmessaging as jm

messenger = jm.Messenger()

messenger._left = '<'
messenger._right = '>'

messenger._info = jm.jcolor.blue + jm.jstyle.bold
messenger._warning = jm.jcolor.magenta + jm.jstyle.bold
messenger._error = jm.jcolor.green + jm.jstyle.bold

messenger.info('This is a message')
messenger.warning('This is a warning')
messenger.error('This is an error')
```
would result in

![Example modified output][output modified]

### Changing background color

```python
import jmessaging as jm

messenger = jm.Messenger()
messenger._info = jm.jbackground.black + jm.jcolor.white + jm.jstyle.bold
messenger._warning = jm.jbackground.yellow + jm.jcolor.white + jm.jstyle.bold
messenger._error = jm.jbackground.red + jm.jcolor.white + jm.jstyle.bold

messenger.info('This is a message')
messenger.warning('This is a warning')
messenger.error('This is an error')
```

would result in

![Example of modified background][output background]

[output example]: docs/output-example.png
[output modified]: docs/output-modified.png
[output background]: docs/output-background.png
