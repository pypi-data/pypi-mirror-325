# Python aria2 RPC call.

## Installation

You can install from [pypi](https://pypi.org/project/ariarpc/)

```console
pip install -U ariarpc
```

## Usage

```python
from ariarpc import rpc_call, Arai2RPC

rpc = Arai2RPC()
rpc.system.listMethods()
```
