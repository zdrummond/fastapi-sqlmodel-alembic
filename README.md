# FastAPI + SQLModel + Alembic

Full guide https://testdriven.io/blog/fastapi-sqlmodel/

Async is [possible](https://testdriven.io/blog/fastapi-sqlmodel/#alembic:~:text=%22Mogwai%22%0A%7D-,Async%20SQLModel,-Moving%20on%2C%20let%27s) but adds complexity for low value on simple CRUD apps

- The doc assumes you have moved to Async for Alembic, but we will try with the generic template

Key Alembic things

- DB has to exit
- `alembic init migrations` init Alembic, add `-t async` to make the calls compatible with async
- `alembic upgrade head` applies migrations
- `alembic revision --autogenerate -m <name>` adds a new migrations
