# jmessaging

`jmessaging` is a very simple package (with no dependencies!) that makes
printing colorized messages to the console a breeze.

## Usage

```python
from jmessaging import Messenger

messenger = Messenger()
messenger.info('This is a message')
messenger.warning('This is a warning')
messenger.error('This is an error')
```

would result in

![Example default output][output example]

The brackets around the message type can be changed along with the color
associated with the type

```python
from jmessaging import Messenger
from jcolor import jcolor, jstyle

messenger = Messenger()

messenger._left = '<'
messenger._right = '>'

messenger.info = jcolor.blue + jstyle.bold
messenger.warning = jcolor.violet + jstyle.bold
messenger.error = jcolor.green + jstyle.bold

messenger.info('This is a message')
messenger.warning('This is a warning')
messenger.error('This is an error')
```
would result in

![Example modified output][output modified]

[output example]: docs/output-example.png
[output modified]: docs/output-modified.png
