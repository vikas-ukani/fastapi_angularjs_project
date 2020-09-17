# Project - FastAPI using AngularJs - Boilerplate Code For Deploy ML Project


* FastAPI framework, high performance, easy to learn, fast to code, ready for production

## Documentation and Sourse Code

[Documentation to implement **FastAPI**](https://fastapi.tiangolo.com/)

[Sourse Code for **FastAPI**](https://github.com/tiangolo/fastapi)


## Requirements

* Python 3.6+

* FastAPI stands on the shoulders of giants:
 - [Starlette](https://www.starlette.io/) for the web parts.
 - [Pydantic](https://pydantic-docs.helpmanual.io/) for the data parts.


## Installation

1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install fastapi.

```bash
pip install fastapi

```

2.  Use the package manager [pip](https://pip.pypa.io/en/stable/) to install uvicorn

```bash
pip install uvicorn

```


## Usage [ Example ]

```python
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

```

## How to Run 
- *Run the server with*

```
$ uvicorn main:app --reload
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


- Developed by **Vikas Ukani**
