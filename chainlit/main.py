import chainlit as cl

@cl.on_message
async def on_message(message: cl.Message):
    if cl.context.session.client_type == "copilot":
        fn = cl.CopilotFunction(name="getBattleStatus", args={"msg": message.content})
        battle_status = await fn.acall()
        await cl.Message(battle_status).send()
    else:
        await cl.Message(message.content).send()