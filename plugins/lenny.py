"""
less args, more lennys
( ͡° ͜ʖ ͡°)
"""


import random


COMMAND = '.lenny'
LENNYS = (
    """( ͡° ͜ʖ ͡°)""",
    """¯\_(ツ)_/¯""",
    """̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\З= ( ▀ ͜͞ʖ▀) =Ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿""",
    """▄︻̷̿┻̿═━一""",
    """( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)""",
    """ʕ•ᴥ•ʔ""",
    """(▀̿Ĺ̯▀̿ ̿)""",
    """(ง ͠° ͟ل͜ ͡°)ง""",
    """༼ つ ◕_◕ ༽つ""",
    """ಠ_ಠ""",
    """(づ｡◕‿‿◕｡)づ""",
    """̿'̿'\̵͇̿̿\З=( ͠° ͟ʖ ͡°)=Ε/̵͇̿̿/'̿̿ ̿ ̿ ̿ ̿ ̿""",
    """(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)""",
    """[̲̅$̲̅(̲̅5̲̅)̲̅$̲̅]""",
    """┬┴┬┴┤ ͜ʖ ͡°) ├┬┴┬┴""",
    """( ͡°╭͜ʖ╮͡° )""",
    """(͡ ͡° ͜ つ ͡͡°)""",
    """(• Ε •)""",
    """(ง'̀-'́)ง""",
    """(ಥ﹏ಥ)""",
    """﴾͡๏̯͡๏﴿ O'RLY?""",
    """(ノಠ益ಠ)ノ彡┻━┻""",
    """[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]""",
    """(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧""",
    """(☞ﾟ∀ﾟ)☞""",
    """| (• ◡•)| (❍ᴥ❍Ʋ)""",
    """(◕‿◕✿)""",
    """(ᵔᴥᵔ)""",
    """(╯°□°)╯︵ ꞰOOQƎƆⱯɟ""",
    """(¬‿¬)""",
    """(☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜)""",
    """(づ￣ ³￣)づ""",
    """ლ(ಠ益ಠლ)""",
    """ಠ╭╮ಠ""",
    """̿ ̿ ̿'̿'\̵͇̿̿\З=(•_•)=Ε/̵͇̿̿/'̿'̿ ̿""",
    """/╲/\╭( ͡° ͡° ͜ʖ ͡° ͡°)╮/\╱\\""",
    """(;´༎ຶД༎ຶ`)""",
    """♪~ ᕕ(ᐛ)ᕗ""",
    """♥‿♥""",
    """༼ つ ͡° ͜ʖ ͡° ༽つ""",
    """༼ つ ಥ_ಥ ༽つ""",
    """(╯°□°）╯︵ ┻━┻""",
    """( ͡ᵔ ͜ʖ ͡ᵔ )""",
    """ヾ(⌐■_■)ノ♪""",
    """~(˘▾˘~)""",
    """◉_◉""",
    """\ (•◡•) /""",
    """(~˘▾˘)~""",
    """(._.) ( L: ) ( .-. ) ( :L ) (._.)""",
    """༼ʘ̚ل͜ʘ̚༽""",
    """༼ ºل͟º ༼ ºل͟º ༼ ºل͟º ༽ ºل͟º ༽ ºل͟º ༽""",
    """┬┴┬┴┤(･_├┬┴┬┴""",
    """ᕙ(⇀‸↼‶)ᕗ""",
    """ᕦ(Ò_Óˇ)ᕤ""",
    """┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻""",
    """⚆ _ ⚆""",
    """(•_•) ( •_•)>⌐■-■ (⌐■_■)""",
    """(｡◕‿‿◕｡)""",
    """ಥ_ಥ""",
    """ヽ༼ຈل͜ຈ༽ﾉ""",
    """⌐╦╦═─""",
    """(☞ຈل͜ຈ)☞""",
    """˙ ͜ʟ˙""",
    """☜(˚▽˚)☞""",
    """(•Ω•)""",
    """(ง°ل͜°)ง""",
    """(｡◕‿◕｡)""",
    """（╯°□°）╯︵( .O.)""",
    """:')""",
    """┬──┬ ノ( ゜-゜ノ)""",
    """(っ˘ڡ˘Σ)""",
    """ಠ⌣ಠ""",
    """ლ(´ڡ`ლ)""",
    """(°ロ°)☝""",
    """｡◕‿‿◕｡""",
    """( ಠ ͜ʖರೃ)""",
    """╚(ಠ_ಠ)=┐""",
    """(─‿‿─)""",
    """ƪ(˘⌣˘)Ʃ""",
    """(；一_一)""",
    """(¬_¬)""",
    """( ⚆ _ ⚆ )""",
    """(ʘᗩʘ')""",
    """☜(⌒▽⌒)☞""",
    """｡◕‿◕｡""",
    """¯\(°_O)/¯""",
    """(ʘ‿ʘ)""",
    """ლ,ᔑ•ﺪ͟͠•ᔐ.ლ""",
    """(´・Ω・`)""",
    """ಠ~ಠ""",
    """(° ͡ ͜ ͡ʖ ͡ °)""",
    """┬─┬ノ( º _ ºノ)""",
    """(´・Ω・)っ由""",
    """ಠ_ಥ""",
    """Ƹ̵̡Ӝ̵̨̄Ʒ""",
    """(>ლ)""",
    """ಠ‿↼""",
    """ʘ‿ʘ""",
    """(ღ˘⌣˘ღ)""",
    """ಠOಠ""",
    """ರ_ರ""",
    """(▰˘◡˘▰)""",
    """◔̯◔""",
    """◔ ⌣ ◔""",
    """(✿´‿`)""",
    """¬_¬""",
    """ب_ب""",
    """｡゜(｀Д´)゜｡""",
    """(Ó Ì_Í)=ÓÒ=(Ì_Í Ò)""",
    """°Д°""",
    """( ﾟヮﾟ)""",
    """٩◔̯◔۶""",
    """≧☉_☉≦""",
    """☼.☼""",
    """^̮^""",
    """(>人<)""",
    """〆(・∀・＠)""",
    """(~_^)""",
    """^̮^""",
    """^̮^""",
    """>_>""",
    """(^̮^)""",
    """(/) (°,,°) (/)""",
    """^̮^""",
    """^̮^""",
    """=U""",
    """(･.◤)"""
)


def main(bot, author_id, message, thread_id, thread_type, **kwargs):
    bot.sendMessage(random.choice(LENNYS), thread_id=thread_id, thread_type=thread_type)
