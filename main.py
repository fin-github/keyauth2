from assets.auth import Auth
from assets.config import conf
from assets.logging import log
import interactions as i


print("Ready....")

TOKEN = open(conf.get("token_file"), 'r').read()
AUTH = Auth()
MSGS: dict[str: str] = conf.get("messages")
KeyModal = i.Modal(
    i.ShortText(
        label=MSGS["modal_key_input_name"],
        custom_id="key",
    ),
    title="Key Authentication",
    custom_id="keymodal"
)

bot = i.Client(intents=i.Intents.ALL)
print("Set....")


@i.listen()
async def on_ready():
    print("GO!!!!!")
    if conf.get("alert_on_awake"): await bot.get_channel(1177004986446647346).send(MSGS["awake"])



@i.slash_command(name=conf.get("auth_command"), description=conf.get("auth_cmd_desc"))
async def auth_cmd(ctx: i.SlashContext):
    await ctx.send_modal(KeyModal)
    
    
@i.modal_callback("keymodal")
async def keymodal_call(ctx: i.ModalContext, key: str):
    res = AUTH.check_key(
        key, int(ctx.author_id)
    )
    embed_details: dict = conf.get("key_res_embed")
    success_details: dict = embed_details["success"]
    failure_details: dict = embed_details["failure"]
    success_color = i.Color.from_rgb(
        success_details["color"][0],
        success_details["color"][1],
        success_details["color"][2],
    )
    failure_color = i.Color.from_rgb(
        failure_details["color"][0],
        failure_details["color"][1],
        failure_details["color"][2],
    )
    
    await ctx.respond(embed=i.Embed(
        title=success_details["title"] if res else failure_details["title"],
        description=success_details["desc"] if res else failure_details["desc"],
        color=success_color if res else failure_color
    ), ephemeral=True)
    log(
        user=ctx.user,
        res=res
    )

bot.start(TOKEN)