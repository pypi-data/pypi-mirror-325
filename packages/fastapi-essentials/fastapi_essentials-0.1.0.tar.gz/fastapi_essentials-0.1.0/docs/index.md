# Welcome to FastAPI Unk!

Hello, make yourself at home!

This is the library where we define all common `FastAPI` functionality like
error handlers, middleware, etc, that we use throughout the majority of our
`FastAPI` services. We define them here to avoid code repetition. Feel free
to roam around these docs for more info!

- [Usage](#usage)
- [Adding to the library](#adding-to-the-library)
- [Wrapping up](#wrapping-up)

## Usage 

Adding it to your `FastAPI` service is pretty easy:

```python
from fastapi_essentials import Unk
from fastapi import FastAPI

app = FastAPI()

Unk(app)
```

That's it! All the common functionality and app behavior is registered by the class.
It currently registers logging configuration and http middleware. Though it's likely that more
will be added soon!

## Adding to the library

Whenever you feel like you're writing logic that would be useful for all our `FastAPI` services
to have access to, and you think it is not appropriate to create a whole new package for that purpose,
add it to this library.

## Wrapping up

So, that's it. We're excited for what you're going to do with it 😆.
