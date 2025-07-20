from asyncio import run as arun
from aiogram import types, Bot, Dispatcher
from aiogram.filters import ChatMemberUpdatedFilter
from aiogram.filters.chat_member_updated import IS_NOT_MEMBER, IS_MEMBER
import logging; logging.basicConfig(level = logging.INFO)
from aiogram.filters.command import Command
from os import getenv
from dotenv import load_dotenv; load_dotenv()

dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.react(reaction=[types.ReactionTypeEmoji(emoji="👍")])

@dp.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def joined(event: types.ChatMemberUpdated):
    await event.chat.ban(event.new_chat_member.user.id)
    await event.chat.unban(event.new_chat_member.user.id)

async def main():
    bot = Bot(token=getenv('API-KEY'))
    await dp.start_polling(bot)

if __name__ == "__main__":
    arun(main())
