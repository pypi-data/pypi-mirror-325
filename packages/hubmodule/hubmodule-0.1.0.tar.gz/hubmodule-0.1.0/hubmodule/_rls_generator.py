import textwrap
from dataclasses import dataclass
from typing import Literal

import psycopg2
from psycopg2 import sql


@dataclass
class TableInfo:
    module_name: str
    model_name: str
    is_link_table: bool
    link_table_related_models: tuple[str, str] | None


class RLSGenerator:
    def __init__(self, db_url: str) -> None:
        self.db_url = db_url

    def setup(self):
        with psycopg2.connect(self.db_url) as conn, conn.cursor() as cur:
            cur.execute(self.query_text)

    @property
    def query_text(self):
        query = "\n".join(
            self._generate_create_query(table_info, operation)
            for table_info in self._list_tables()
            for operation in ["SELECT", "INSERT", "UPDATE", "DELETE"]
        )
        return textwrap.dedent(query)

    def _list_tables(self):
        query = sql.SQL("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            AND table_type = 'BASE TABLE';
        """)

        with psycopg2.connect(self.db_url) as conn, conn.cursor() as cur:
            cur.execute(query)
            module_names = []
            model_names = []
            for row in cur.fetchall():
                table_name = row[0]
                module_name = table_name.split("_")[0]
                model_name = table_name.replace(f"{module_name}_", "")
                module_names.append(module_name)
                model_names.append(model_name)
            return [
                TableInfo(
                    module_names[i],
                    model_name,
                    *self._is_link_table(model_name, model_names),
                )
                for i, model_name in enumerate(model_names)
            ]

    @staticmethod
    def _is_link_table(model_name, all_models):
        for name_1 in all_models:
            if name_1 in model_name:
                name_2 = model_name.replace(name_1, "")
                if name_2 in all_models:
                    return True, (name_1, name_2)
        return False, None

    @staticmethod
    def _generate_create_query(
        table_info: TableInfo,
        operation: Literal["SELECT", "INSERT", "UPDATE", "DELETE"],
    ):
        table_name = f"{table_info.module_name}_{table_info.model_name}"
        policy_name = f"{table_name}_rls_{operation}_policy"

        def space_check_clause():
            indent = 8 * " " if table_info.is_link_table else ""
            return f"""space_id IN (
                {indent}    SELECT ts.space_id
                {indent}    FROM team_space ts
                {indent}    JOIN account_team at ON ts.team_id = at.team_id
                {indent}    WHERE at.account_id = current_setting('app.account_id')::int
                {indent}    AND ts.operation = '{operation}'
                {indent})"""

        def exists_clause(related_table):
            return f"""EXISTS (
                    SELECT 1
                    FROM {related_table} r
                    WHERE r.id = {table_name}.{related_table}_id
                    AND (
                        {space_check_clause()}
                    )
                )"""

        if table_info.is_link_table:
            rt1, rt2 = table_info.link_table_related_models
            clause = f"""{exists_clause(rt1)}
                AND
                {exists_clause(rt2)}"""
        else:
            clause = space_check_clause()

        if operation in {"SELECT", "DELETE"}:
            template = f"""
            CREATE POLICY {policy_name} ON {table_name}
            FOR {operation}
            USING (
                {clause}
            );
            """
        elif operation == "INSERT":
            template = f"""
            CREATE POLICY {policy_name} ON {table_name}
            FOR {operation}
            WITH CHECK (
                {clause}
            );
            """
        elif operation == "UPDATE":
            template = f"""
            CREATE POLICY {policy_name} ON {table_name}
            FOR {operation}
            USING (
                {clause}
            )
            WITH CHECK (
                {clause}
            );
            """
        return template
