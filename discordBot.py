import subprocess
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", ignore_bots=True, intents=discord.Intents.all())

class SampleView(discord.ui.View):
    def __init__(self, timeout=180):
        super().__init__(timeout=timeout)
        #self.message_count = 0  # メッセージの数をカウントする変数
    
    @discord.ui.button(label="ページ数からキメル", style=discord.ButtonStyle.primary)
    async def ok(self, interaction: discord.Interaction, button: discord.ui.Button):
        result = await self.run_external_script()
        await interaction.response.send_message(f"{interaction.user.mention}ぶきち：{result}")
        await test(interaction)

    @discord.ui.button(label="全員", style=discord.ButtonStyle.primary)
    async def zen1(self, interaction: discord.Interaction, button: discord.ui.Button):
        # "一般"という名前のボイスチャンネルを取得
        channel = discord.utils.get(interaction.guild.voice_channels, name='一般')

        if channel is None:
            await interaction.response.send_message("『一般』ボイスチャンネルが見つかりません")
            return

        # ボイスチャンネルに参加しているメンバーを取得
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
        result = await self.run_external_script2()
        await interaction.response.send_message(f"{interaction.user.mention}ぶきち:{result}")
        await test(interaction)


    @discord.ui.button(label="全員", style=discord.ButtonStyle.success)
    async def zen2(self, interaction: discord.Interaction, button: discord.ui.Button):
        # "一般"という名前のボイスチャンネルを取得
        channel = discord.utils.get(interaction.guild.voice_channels, name='一般')

        if channel is None:
            await interaction.response.send_message("『一般』ボイスチャンネルが見つかりません")
            return

        # ボイスチャンネルに参加しているメンバーを取得
        members = channel.members
        sendMsg = f"ぶきち:"

        if not members:
            await interaction.response.send_message("『一般』には１匹もいません")
            return

        for member in members:
            result = await self.run_external_script2()
            sendMsg = sendMsg + f"{member.mention}は{result}"
        await interaction.response.send_message(sendMsg)


    async def run_external_script(self):
        try:
            result = subprocess.check_output(["python", "byWeaponPage.py"])
            return result.decode("utf-8")
        except subprocess.CalledProcessError as e:
            return f"Error: {e.returncode}, Output: {e.output.decode('utf-8')}"

    async def run_external_script2(self):
        try:
            result = subprocess.check_output(["python", "byAllWeapon.py"])
            return result.decode("utf-8")
        except subprocess.CalledProcessError as e:
            return f"Error: {e.returncode}, Output: {e.output.decode('utf-8')}"

    # async def count_message(self, interaction):
    #     self.message_count += 1  # メッセージの数をカウント
    #     if self.message_count == 2:
    #         try:
    #             await test(interaction)
    #         except discord.errors.NotFound:
    #             pass
    #         self.message_count = 0  # メッセージの数をリセット
    
    async def send_initial_buttons(self, interaction):
        view = SampleView(timeout=None)
        await interaction.message.edit(view=view)

@bot.command()
async def test(interaction):
    channel = interaction.channel
    view = SampleView(timeout=None)
    await channel.send(view=view)

bot.run("MTEyMTQyNjYxNjAwMjgxNDA2Nw.Gv-0w-.MWME7AL3-o6-oFyoXpyz_G5CTMMHw-hOsJWeH0")
