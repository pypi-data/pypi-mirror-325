from typing import Callable
from fastapi.testclient import TestClient
from fastapi import FastAPI

CreateClientFixture = Callable[[Callable[[FastAPI], None]], TestClient]
