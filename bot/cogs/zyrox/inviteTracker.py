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
from utils.emoji import ZPEOPLE

from discord.ext import commands

class inviteTracker(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    """Invite Tracker"""

    def help_custom(self):

              emoji = ZPEOPLE

              label = "Invite Tracker"

              description = "Show you Commands of Invite Tracker"

              return emoji, label, description

    @commands.group()

    async def __InviteTracker__(self, ctx: commands.Context):

        """`>invites`, `>addinvites`, `>inviteleaderboard`, `>invitelogging`"""