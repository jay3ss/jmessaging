# jmessaging

`jmessaging` is a very simple package that makes printing colorized messages to
the console a breeze.

## Usage

```python
messenger = Messenger()
messenger.info('This is a message')
messenger.warning('This is a warning')
messenger.error('This is an error')
```

which would result in

<code>
<span style="font-weight: bold;">This is a message</span><br>
<span style="color: yellow;font-weight: bold;">This is a warning</span><br>
<span style="color: red;font-weight: bold;">This is an error</span><br>
</code>
