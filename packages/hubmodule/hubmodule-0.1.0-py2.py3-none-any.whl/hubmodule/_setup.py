from pathlib import Path
from uuid import UUID

import psycopg2
from laminhub_rest.hubmodule._rls_generator import RLSGenerator
from loguru import logger
from supabase.client import Client


def install(supabase_client: Client, instance_id: UUID):
    from laminhub_rest import hubmodule
    from laminhub_rest.core.instance import InstanceHandler

    dsn_admin = InstanceHandler(supabase_client).get_db_url(instance_id)
    create_jwt_user(supabase_client, instance_id, dsn_admin)

    current_dir = Path(hubmodule.__file__).parent
    execute_sql_file(dsn_admin, current_dir / "sql/1-setup-extensions.sql")
    execute_sql_file(dsn_admin, current_dir / "sql/2-setup-secret.sql")
    execute_sql_file(dsn_admin, current_dir / "sql/3-utils-jwt.sql")
    RLSGenerator(dsn_admin).setup()
    logger.info("Applied RLS policy statements")


def create_jwt_user(supabase_client: Client, instance_id: UUID, dsn_admin: str):
    from laminhub_rest.core.access import DbUserHandler
    from laminhub_rest.core.db import DbRoleHandler

    db_role_handler = DbRoleHandler(dsn_admin)
    db_user_handler = DbUserHandler(supabase_client)

    # Create JWT user
    if not db_user_handler.exist(instance_id, "jwt"):
        jwt_role_name = f"{instance_id.hex}_jwt"
        jwt_db_url = db_role_handler.create(
            jwt_role_name, expires_in=None, alter_if_exists=True
        )
        db_role_handler.permission.grant_write_jwt(jwt_role_name)
        db_user_handler.create(instance_id, "jwt", jwt_db_url)
        logger.info("JWT db user created")
    else:
        logger.warning("JWT db user already exists")


def execute_sql_file(dsn, path):
    with psycopg2.connect(dsn) as conn, conn.cursor() as cur:  # noqa: SIM117
        with path.open("r") as file:
            cur.execute(file.read())
    logger.info(f"{path} executed")
