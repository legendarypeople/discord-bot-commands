@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
      await ctx.channel.purge(limit=amount)
      await ctx.send("**Cleared `" + str(amount) + "` Messages**")
