# services/chat_service.py

from services.sql_service import SQLService
from modules.llm_manager import procesar_peticion_llm

class ChatService:
    def __init__(self, ddl_cmds: list[str], dml_cmds: list[str]):
        self.sql_svc = SQLService(ddl_cmds=ddl_cmds, dml_cmds=dml_cmds)

    def handle_message(self, text: str, user_id: str) -> dict:
        """
        Delegates to SQLService *only* if, tras quitar espacios y 
        signos de apertura '¿'/'¡', el mensaje arranca exactamente 
        con CREATE, INSERT o SELECT. En cualquier otro caso, llama 
        al LLM.
        """
        # 1) Quitar espacios a la izquierda...
        msg = text.lstrip()
        # …y descartar todos los signos de apertura
        while msg and msg[0] in ('¿', '¡'):
            msg = msg[1:]
        msg = msg.lstrip()

        # 2) Si queda vacío → fallback al LLM
        if not msg:
            return {"response": procesar_peticion_llm(text, user_id)}

        # 3) Extraer primera palabra, sin ';', en MAYÚSCULAS
        token = msg.split()[0].rstrip(';').upper()

        # 4) Si coincide EXACTAMENTE con un comando SQL configurado
        if (
            token in self.sql_svc.ddl_cmds
            or token in self.sql_svc.dml_cmds
            or token == self.sql_svc.select_cmd
        ):
            return self.sql_svc.handle(text, user_id)

        # 5) Cualquier otro caso → fallback al LLM
        return {"response": procesar_peticion_llm(text, user_id)}