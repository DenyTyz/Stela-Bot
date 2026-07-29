# ╔══════════════════════════════════════════════════════════════════╗
# ║                                                                  ║
# ║   ░█▀▀░▀█▀░█▀▀░█░░░█▀█   ░█▀▄░█▀▀░█░█░█▀▀                     ║
# ║   ░▀▀█░░█░░█▀▀░█░░░█▀█   ░█░█░█▀▀░▀▄▀░▀▀█                     ║
# ║   ░▀▀▀░░▀░░▀▀▀░▀▀▀░▀░▀   ░▀▀░░▀▀▀░░▀░░▀▀▀                     ║
# ║                                                                  ║
# ║            © 2026 Stela Devs — All Rights Reserved              ║
# ║                                                                  ║
# ║   discord  ──  https://discord.gg/steladev                      ║
# ║   youtube  ──  https://youtube.com/@StelaDevs                   ║
# ║   github   ──  https://github.com/RayExo                        ║
# ║                                                                  ║
# ╚══════════════════════════════════════════════════════════════════╝

import discord
from utils.emoji import MESSAGE
from discord.ext import commands

class _joindm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    """__Join Dm__"""
    def help_custom(self):
              emoji = MESSAGE
              label = "Joindm"
              description = "Show you Commands of Joindm"
              return emoji, label, description
    @commands.group()
    async def __Joindm__(self, ctx: commands.Context):
        """`joindm enable` , `joindm disable` , `joindm message` , `joindm test`"""