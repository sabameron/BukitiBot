import os
import subprocess
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", ignore_bots=True, intents=discord.Intents.all())

class SampleView(discord.ui.View):
    def __init__(self, timeout=180):
        super().__init__(timeout=timeout)
    
    @discord.ui.button(label="ページ数からキメル", style=discord.ButtonStyle.primary)
    async def ok(self, interaction: discord.Interaction, button: discord.ui.Button):
        result = await self.run_external_script()
        await interaction.response.send_message(f"{interaction.user.mention}ぶきち：{result}")
    
    @discord.ui.button(label="全員", style=discord.ButtonStyle.primary)
    async def zen1(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = discord.utils.get(interaction.guild.voice_channels, name='一般')

        if channel is None:
            await interaction.response.send_message("『一般』ボイスチャンネルが見つかりません")
            return

        members = channel.members
        sendMsg = f"ぶきち:"

        if not members:
            await interaction.response.send_message("『一般』には１匹もいません")
            return

        for member in members:
            result = await self.run_external_script()
            sendMsg = sendMsg + f"{member.mention}は{result}"
        await interaction.response.send_message(sendMsg)
    
    @discord.ui.button(label="全武器からキメル", style=discord.ButtonStyle.success)
    async def ng(self, interaction: discord.Interaction, button: discord.ui.Button):
        result = await self.run_external_script2("None")
        await interaction.response.send_message(f"{interaction.user.mention}ぶきち:{result}")

    @discord.ui.button(label="全員", style=discord.ButtonStyle.success)
    async def zen2(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = discord.utils.get(interaction.guild.voice_channels, name='一般')

        if channel is None:
            await interaction.response.send_message("『一般』ボイスチャンネルが見つかりません")
            return

        members = channel.members
        sendMsg = f"ぶきち:"

        if not members:
            await interaction.response.send_message("『一般』には１匹もいません")
            return

        for member in members:
            #print(member.id)
            result = await self.run_external_script2(str(member.id))
            sendMsg = sendMsg + f"{member.mention}は{result}"
        await interaction.response.send_message(sendMsg)

    async def run_external_script(self):
        try:
            result = subprocess.check_output(["python", "byWeaponPage.py"])
            return result.decode("utf-8")
        except subprocess.CalledProcessError as e:
            return f"Error: {e.returncode}, Output: {e.output.decode('utf-8')}"

    async def run_external_script2(self, discord_id):
        try:
            result = subprocess.check_output(["python", "byAllWeapon.py", discord_id])
            return result.decode("utf-8")
        except subprocess.CalledProcessError as e:
            return f"Error: {e.returncode}, Output: {e.output.decode('utf-8')}"


class NewView(discord.ui.View):
    def __init__(self, timeout=180):
        super().__init__(timeout=timeout)
    
    @discord.ui.button(label="検証！", style=discord.ButtonStyle.primary)
    async def ok(self, interaction: discord.Interaction, button: discord.ui.Button):
        result = await self.verify(button, interaction)
        await interaction.response.send_message(result)
    
    async def verify(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            result = subprocess.check_output(["python", "CalcurationKakuritu.py"])
            return result.decode("utf-8")
        except subprocess.CalledProcessError as e:
            return f"Error: {e.returncode}, Output: {e.output.decode('utf-8')}"

@bot.command()
async def test(ctx):
    channel = ctx.channel
    view = SampleView(timeout=None)
    await channel.send("ボタンをクリックして検証を開始してください！", view=view)

@bot.command()
async def 検証(ctx):
    view = NewView(timeout=None)
    await ctx.channel.send("ボタンをクリックして検証を開始してください！", view=view)

bot.run(os.environ["BUKITI_TOKEN"])
