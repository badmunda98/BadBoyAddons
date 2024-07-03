# <p align="center"><a href="https://github.com/badmunda98/BadBoyAddons"><img src="https://github-readme-stats.vercel.app/api/pin?username=TeamBadBoy&show_icons=true&theme=dracula&hide_border=true&repo=BadBoyAddons"></a></p>
<p align="center">

# BadBoyAddons
Plugins repository for [@BadBoy](https://github.com/Badhacker98/BadBoy).


# Contributing
If you want to contribute to this repository (adding your plugins/porting from other bots), use the format given below and create a pull request.   
⚠️ First check whether the stuff you push works. Also, if the pull request doesn't follow the below format, it will be closed without prior notice.

```python
# Credits @username (creator of plugin and who ported)   
   
# Ported from (if ported else skip)   
   
# Ported for BadBoy < https://github.com/Badhacker98/BadBoy >   
```
   
Kindly do not **steal** others works without credits.<br>

# Example Plugin
   Required Import are Automatically Done.

<kbd>This Example Works Everywhere. (e.g. Groups, Personal Chats ...)</kbd>
```python
@BadBoy_cmd(pattern="hoi")
async def hello_world_example(event):
    # As telethon is an asyncio based lib, you will have to use `async`/`await` Syntax.
    await event.reply("Hello **World**.")
```

<kbd>This Example Works Only In Groups.</kbd>
```python
@BadBoy_cmd(pattern="hoi", groups_only=True,)
async def hello_world_example(event):
    await event.reply("Hello **World**.")
```

If Your plugin need any additional requirements, it can be added to <a href="https://github.com/badmunda98/BadBoyAddons/blob/main/addons.txt">addons.txt</a><br><br>

<br>


> Made with 💕 by [@TeamPbx](https://t.me/PBX_CHAT).
