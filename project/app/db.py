# project/app/db.py


import logging
import os

from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

log = logging.getLogger("uvicorn")


# For aerich to do migrations
TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": ["app.models.tortoise", "aerich.models"],
            "default_connection": "default",
        },
    },
}


# generate_schema set to False - Tortoise does not do migrations
# allows the flexibility to allow aerich or Tortoise to do migration at later point
def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )


# Sometimes we need to do only the final migration
# Tell tortoise to do apply the final migration
# python app/db.py
async def generate_schema() -> None:
    log.info("Intializing Tortoise...")

    await Tortoise.init(
        db_url=os.environ.get("DATABASE_URL"), modules={"models": ["models.tortoise"]}
    )

    log.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schema())
