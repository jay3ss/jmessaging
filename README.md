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
from jcolor import Color, Style

messenger = Messenger()

messenger.LEFT = '<'
messenger.RIGHT = '>'

messenger.INFO = Color.BLUE + Style.BOLD
messenger.WARNING = Color.VIOLET + Style.BOLD
messenger.ERROR = Color.GREEN + Style.BOLD

messenger.info('This is a message')
messenger.warning('This is a warning')
messenger.error('This is an error')
```
would result in

![Example modified output][output modified]

[output example]: docs/output-example.png
[output modified]: docs/output-modified.png
