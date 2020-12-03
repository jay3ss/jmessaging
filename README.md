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


### Colorizing text

Text can be colorized using the `jcolorize` function from the `jcolor` module
like so

```python
import jmessaging as jm

colorized = jm.jcolorize('This is text', jm.jcolor.cyan)
print(colorized)
```

would result in

![Example of colorized text][output colorized]

### Printing on the same line

You can print on the same line repeatedly using the `print_same_line` function
like so

```python
import time
import jmessaging as jm

for i in range(1000, 0, -1):
    jm.print_same_line(f'Current num: {i}')
    time.sleep(0.001)

print('\n')
```

would result in

![Example of printing on the same line][output same line]

Notice the `print('\n')` at the end. That's necessary (or use `print()`) to move
the cursor to the next line.

[output example]: https://raw.githubusercontent.com/jay3ss/jmessaging/main/docs/output-example.png
[output modified]: https://raw.githubusercontent.com/jay3ss/jmessaging/main/docs/output-modified.png
[output background]: https://raw.githubusercontent.com/jay3ss/jmessaging/main/docs/output-background.png
[output colorized]: https://raw.githubusercontent.com/jay3ss/jmessaging/main/docs/output-colorized.png
[output same line]: https://raw.githubusercontent.com/jay3ss/jmessaging/main/docs/output-same-line.gif
