import sublime, sublime_plugin

class MinionIpsum(sublime_plugin.TextCommand):
    def run(self, edit):
        text = "Minions ipsum tulaliloo underweaaar la bodaaa pepete jiji bananaaaa chasy baboiii hahaha. Underweaaar chasy tatata bala tu bappleees baboiii potatoooo potatoooo. Hahaha tank yuuu! Po kass tank yuuu! Baboiii underweaaar. Gelatooo la bodaaa bappleees tatata bala tu baboiii. Pepete chasy hana dul sae ti aamoo! Jeje me want bananaaa! Uuuhhh. Hahaha gelatooo ti aamoo! La bodaaa hahaha gelatooo bananaaaa hahaha. La bodaaa tulaliloo bee do bee do bee do uuuhhh poulet tikka masala potatoooo jeje aaaaaah."
        self.view.insert(edit, self.view.sel()[0].begin(), text)