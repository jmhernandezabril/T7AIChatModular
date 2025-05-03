# services/chat_service.py

import os
import sys
from services.sql_service import SQLService
from modules.llm_manager import procesar_peticion_llm

# Debug: verificar desde dónde se carga el módulo
print("▶▶▶ ChatService cargado desde:", os.path.abspath(__file__))
print("▶▶▶ sys.path[0]:", sys.path[0])

class ChatService:
    def __init__(self, ddl_cmds: list[str], dml_cmds: list[str]):
        self.sql_svc = SQLService(ddl_cmds=ddl_cmds, dml_cmds=dml_cmds)

    def handle_message(self, text: str, user_id: str) -> dict:
        """
        Delegates to SQLService only if the first token (after stripping '¿'/'¡' and whitespace)
        matches DDL, DML, or SELECT. Otherwise, always fallback to LLM.
        """
        # DEBUG: ¿qué estamos recibiendo?
        print("🔍 DEBUG handle_message. text recibido:", repr(text))
        # 1) Remove leading whitespace and opening punctuation
        msg = text.lstrip()
        while msg and msg[0] in ('¿', '¡'):
            msg = msg[1:]
        msg = msg.lstrip()

        # 2) If empty, fallback to LLM
        if not msg:
            return {"response": procesar_peticion_llm(text, user_id)}

        # 3) Extract first token, strip trailing ';', uppercase
        token = msg.split()[0].rstrip(';').upper()
        print("🔍 DEBUG token extraído:", repr(token))

        # 4) Delegate to SQLService only if exact command
        if (
            token in self.sql_svc.ddl_cmds
            or token in self.sql_svc.dml_cmds
            or token == self.sql_svc.select_cmd
        ):
            return self.sql_svc.handle(text, user_id)

        # 5) Otherwise fallback to LLM
        return {"response": procesar_peticion_llm(text, user_id)}