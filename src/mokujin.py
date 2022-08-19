#!/usr/bin/env python3
import datetime
import logging
import os
import sys
import configurator

sys.path.insert(1, (os.path.dirname(os.path.dirname(__file__))))

import discord
from discord import app_commands
from src import tkfinder, util
from src.resources import embed
from github import Github

base_path = os.path.dirname(__file__)
config = configurator.Configurator(os.path.abspath(os.path.join(base_path, "resources", "config.json")))

# Set logger to log errors
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

logfile_directory = os.path.abspath(os.path.join(base_path, "..", "log"))
logfile_path = logfile_directory + "\\logfile.log"

# Create logfile if not exists
if not os.path.exists(logfile_directory):
    os.makedirs(logfile_directory)

if not os.path.isfile(logfile_path):
    open(logfile_path, "w")

file_handler = logging.FileHandler(logfile_path)
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

discord_token = config.read_config()['DISCORD_TOKEN']
feedback_channel_id = config.read_config()['FEEDBACK_CHANNEL_ID']
github_token = config.read_config()['GITHUB_TOKEN']
gh = Github(login_or_token=github_token)


class mokujin(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print("mokujin connected")

client = mokujin()
tree = app_commands.CommandTree(client)

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        user_message_list = message.content[1:].split(' ', 1)[1]
        user_command = user_message_list.strip().split(' ',1)
        original_name = user_command[0].lower()
        original_move = user_command[1]

        character_name = tkfinder.correct_character_name(original_name)
        if character_name is not None:
            character = tkfinder.get_character_detail(character_name)
            move_type = util.get_move_type(original_move.lower())

            if move_type:
                result = util.display_moves_by_type(character, move_type)
            else:
                result = util.display_moves_by_input(character, original_move)
        else:
            result = {"embed": embed.error_embed(f'Character {original_name} does not exist.')}

        await message.channel.send(embed=result["embed"])

@tree.command(name="fd", description="Frame data from a character move")
async def self(interaction: discord.Interaction, character: str, move: str):
    character = character.lower()
    character_name = tkfinder.correct_character_name(character)

    if character_name is not None:
        character = tkfinder.get_character_detail(character_name)
        move_type = util.get_move_type(move.lower())

        if move_type:
            result = util.display_moves_by_type(character, move_type)
        else:
            result = util.display_moves_by_input(character, move)
    else:
        result = {"embed": embed.error_embed(f'Character {character} does not exist.')}

    await interaction.response.send_message(embed=result["embed"], ephemeral=False)


@tree.command(name="feedback", description="Send feedback incase of wrong data")
async def self(interaction: discord.Interaction, message: str):
    today = datetime.datetime.strptime(datetime.datetime.now().isoformat(), "%Y-%m-%dT%H:%M:%S.%f")
    age = today - interaction.user.created_at.replace(tzinfo=None)
    print(age.days)
    if age.days < 120:
        return
    else:
        try:
            feedback_message = "{} ;{} ;{} ;{}\n".format(str(interaction.user.name), interaction.user.id,
                                                         interaction.guild, message)
            channel = client.get_channel(feedback_channel_id)
            await channel.send(feedback_message)
            result = {"embed": embed.success_embed("Feedback sent")}
        except Exception as e:
            result = {"embed": embed.error_embed("Feedback couldn't be sent caused by: " + e)}

        await interaction.response.send_message(embed=result["embed"], ephemeral=True)


@tree.command(name="last-updates", description="Show last updates of the bot on github")
async def self(interaction: discord.Interaction):
    try:
        messages = util.get_latest_commits_messages(gh, 5)
        result = {"embed": embed.success_embed(messages)}
    except Exception as e:
        result = {"embed": embed.error_embed(e)}
    await interaction.response.send_message(embed=result["embed"], ephemeral=True)

@tree.command(name="about", description="Show the meta data about the bot")
async def self(interaction: discord.Interaction):
    result = {"embed": embed.help_embed()}
    await interaction.response.send_message(embed=result["embed"], ephemeral=True)


try:
    client.run(discord_token)
except Exception as e:
    time_now = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    logger.error(f'{time_now} \n Error: {e}')
