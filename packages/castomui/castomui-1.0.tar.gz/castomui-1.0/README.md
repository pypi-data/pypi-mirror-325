# CastomUi

A python package for TUI

Include many TUI functions like **'Prompt'** or **Selection**

## Installation

[Pypi](https://pypi.org/project/castomui/)
[Github](https://github.com/Hansha2011/CastomUi)

## How to use

You can use the demo function

```python
import castomui as cstm
cstm.demo()
```

Or you can customize

```python
import castomui as cstm
a=cstm.DirectedSelection(value=["Selection 1","Selection 2","Selection 3","Selection 4","Selection 5","Selection 6","Selection 7","Support me?"])
a.show()
print(a.get())
```

## Update log

2025/02/06 - `1.0.0` first release