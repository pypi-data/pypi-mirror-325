from typing import Any

from fastapi import APIRouter, HTTPException
from json_repair import repair_json
from loguru import logger

from ..gomtmclients.rest.models.chat_req import ChatReq
from ..teammanager import TeamManager

router = APIRouter()


@router.api_route(path="/tenants/{tenant}/chat", methods=["GET", "POST"])
async def chat(r: ChatReq):
    try:
        user_messages = r.messages
        if len(user_messages) == 0:
            raise HTTPException(status_code=400, detail="No messages provided")
        task = user_messages[-1].content
        # 练习1: 简单调用

        # assistant = AssistantAgent(name="assistant", model_client=get_oai_Model())

        # async def chat_stream():
        #     chat_response = assistant.run_stream(task=user_message)
        #     async for chunk in chat_response:
        #         if isinstance(chunk, TextMessage):
        #             yield f"0:{json.dumps(chunk.content)}\n"

        # return StreamingResponse(chat_stream(), media_type="text/event-stream")

        team_manager = TeamManager()
        team = await team_manager.create_demo_team()
        team_component = team.dump_component()
        result_message = await team_manager.run(task=task, team_config=team_component)
        return result_message

    except Exception as e:
        logger.exception("Chat error")
        return {"error": str(e)}


class LoggingModelClient:
    def __init__(self, wrapped_client):
        self.wrapped_client = wrapped_client

    async def create(self, *args: Any, **kwargs: Any) -> Any:
        try:
            response = await self.wrapped_client.create(*args, **kwargs)
            if kwargs.get("json_output", False):
                # 修正json格式
                if isinstance(response.content, str):
                    response.content = repair_json(response.content)

            logger.info(
                "OpenAI API Response",
                request_args=args,
                request_kwargs=kwargs,
                response_content=response.content,
            )
            return response
        except Exception as e:
            logger.exception(
                "OpenAI API Error", error=str(e), error_type=type(e).__name__
            )
            raise


# @router.api_route(path="/test_m1", methods=["GET", "POST"])
# async def test_m1(r: Request):
#     from autogen_ext.agents.web_surfer import PlaywrightController

#     # 测试 megentic one agent
#     try:
#         model_client = get_oai_Model()
#         logging_client = LoggingModelClient(model_client)

#         assistant = AssistantAgent(
#             "Assistant",
#             model_client=logging_client,
#         )

#         surfer = PlaywrightController(
#             downloads_folder=".vol/WebSurfer",
#             model_client=model_client,
#         )

#         team = MagenticOneGroupChat([surfer], model_client=logging_client)
#         await Console(team.run_stream(task="用中文写一段关于马克龙的新闻"))

#     except Exception as e:
#         logger.error("Chat error", error=str(e))
#         return {"error": str(e)}
#         return {"error": str(e)}
#         return {"error": str(e)}
