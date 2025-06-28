# bot.py
import discord
from discord.ext import commands
from tournament import TournamentManager
from bracket import draw_bracket
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)
tournament = TournamentManager()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def start_tournament(ctx):
    tournament.reset()
    tournament.host_id = ctx.author.id
    msg = await ctx.send("React with ⚽ to join the tournament!")
    tournament.registration_message_id = msg.id
    tournament.channel_id = ctx.channel.id
    await msg.add_reaction("⚽")

@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == tournament.registration_message_id and str(payload.emoji) == "⚽":
        guild = bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        if member and not member.bot:
            tournament.add_player(member.display_name)

@bot.command()
async def start_bracket(ctx):
    if ctx.author.id != tournament.host_id:
        return await ctx.send("Only the host can start the bracket.")
    tournament.generate_bracket()
    draw_bracket(tournament)
    await ctx.send(file=discord.File("bracket.png"))
    next_match = tournament.get_next_match()
    if next_match:
        await ctx.send(f"Next match: {next_match[0]} vs {next_match[1]}")

@bot.command()
async def result(ctx, p1: str, score1: int, p2: str, score2: int):
    if ctx.author.id != tournament.host_id:
        return await ctx.send("Only the host can report results.")
    winner = p1 if score1 > score2 else p2
    tournament.record_result(p1, p2, winner)
    draw_bracket(tournament)
    await ctx.send(f"✅ Result recorded: {winner} wins!")
    await ctx.send(file=discord.File("bracket.png"))
    next_match = tournament.get_next_match()
    if next_match:
        await ctx.send(f"Next match: {next_match[0]} vs {next_match[1]}")
    else:
        await ctx.send(f"🏆 Tournament winner: {winner}!")

bot.run(os.getenv("DISCORD_TOKEN"))