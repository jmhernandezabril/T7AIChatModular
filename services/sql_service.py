# services/sql_service.py

class SQLService:
    def __init__(self, ddl_cmds: list[str], dml_cmds: list[str]):
        """
        Initialize the service with lists of DDL and DML command keywords.
        """
        self.ddl_cmds = {cmd.upper() for cmd in ddl_cmds}
        self.dml_cmds = {cmd.upper() for cmd in dml_cmds}
        self.select_cmd = "SELECT"

    def handle(self, text: str, user_id: str) -> dict | None:
        """
        Decide whether text is DDL, DML, or SELECT SQL.
        Delegates to the appropriate executor and returns:
          - 'response' for DDL/DML
          - 'response', 'columns', 'dataframe' for SELECT
          - None if not SQL
        """
        # Import lazy para evitar dependencias circulares
        from modules.sql_executor import ejecutar_sql_manual, ejecutar_consulta_select

        first = text.strip().split()[0].upper()

        # DDL/DML
        if first in self.ddl_cmds or first in self.dml_cmds:
            result = ejecutar_sql_manual(text, usuario=user_id)
            return {"response": result.get("error") or result.get("success")}

        # SELECT
        if first == self.select_cmd:
            result = ejecutar_consulta_select(text)
            if "error" in result:
                return {"response": result["error"]}
            return {
                "response":  result["response"],
                "columns":   result["columns"],
                "dataframe": result["dataframe"],
            }

        # No es SQL
        return None