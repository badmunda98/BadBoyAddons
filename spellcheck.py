

"""
✘ Commands Available -

• {i}spcheck <text/reply to message>
    check spelling of the text/sentence
"""

from textblob import TextBlob

from . import *


@BadBoy_cmd(pattern="spcheck ?(.*)")
async def spellchk(event):
    to_check = event.pattern_match.group(1)
    if not to_check and event.is_reply:
        reply = await event.get_reply_message()
        if reply.text:
            to_check = reply.text
    if not (to_check or event.is_reply):
        return await event.eor("`Give me some text/sentence to check its spelling!.`")
    check = TextBlob(to_check)
    correct = check.correct()
    await eor(
        event, f"**Given Phrase:** `{to_check}`\n**Corrected Phrase:** `{correct}`"
    )
