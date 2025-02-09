# sqlitecloud-example

An example of using [SQLite Cloud](https://sqlitecloud.io/) and [SQLModel](https://sqlmodel.tiangolo.com/) together.

## Requirements

- [uv](https://github.com/astral-sh/uv)

## Setup

- Create an account on [SQLite Cloud](https://sqlitecloud.io/) and create a new database.
- Add the following environment variables to your `.env` file:

```
DATABASE_NAME=your-database-name
PROJECT_ID=your-project-id
API_KEY=your-api-key
```

- Run the following command to setup the example table:

```bash
uv run main.py
```

## Examples
Checkout the `examples.ipynb` notebook for examples.
