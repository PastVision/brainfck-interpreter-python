# brainfuck-interpreter-python
A brainfuck interpreter written in python3.

## Requirements
>python3


## Usage
### Interpret a file containing BrainFuck code

```bash
python bfinterpreter.py 'file-containing-brainfuck-code'
```
### By importing it in a python script

```python
from bfinterpreter import brainF
code = 'brainfuck code'

#Default usage with register size = 200
brainF(code)

#Custom register size, just in case
registerSize = 1000
brainF(code, regSize = registerSize)

```

## Example
### code.bf contains a BrainFuck code
```bash
$cat code.bf
++++[++++>---<]>.+[--->+<]>+++.--..----.
+++++++++++.[---->+<]>+++.+[->+++<]>.+++++.
-------.+++++++++++++.-------.--.[--->+<]>----.
-[++>---<]>+.------------.
+[----->+<]>+.+.+++++.[---->+<]>+++.
+[->+++<]>.-[--->+<]>----.---------.++++.
--------.[--->+<]>----.+[-->+++++<]>-.
```

### Execution
```bash
$python bfinterpreter.py code.bf
Commit changes, not crimes!
```
