import sublime, sublime_plugin

class MinionIpsum(sublime_plugin.TextCommand):
    def run(self, edit):
		bananaArray = array("pepete","aaaaaah","uuuhhh","jiji","hahaha","jeje","wiiiii","bananaaaa","bappleees","potatoooo","para tú","la bodaaa","poulet tikka masala","daa","hana dul sae","belloo!","poopayee","tank yuuu!","me want bananaaa!","underweaaar","bee do bee do bee do","tulaliloo","ti aamoo!","tatata bala tu","baboiii","po kass","gelatooo","butt","chasy")
		latinArray = array("sit amet", "consectetur", "adipisicing", "elit", "sed", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua", "enim", "ad", "minim", "veniam", "quis", "nostrud", "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "commodo", "consequat", "duis", "aute", "irure", "dolor", "reprehenderit", "voluptate", "velit", "esse", "cillum","occaecat", "qui", "officia")

        # text = "Minions ipsum tulaliloo underweaaar la bodaaa pepete jiji bananaaaa chasy baboiii hahaha. Underweaaar chasy tatata bala tu bappleees baboiii potatoooo potatoooo. Hahaha tank yuuu! Po kass tank yuuu! Baboiii underweaaar. Gelatooo la bodaaa bappleees tatata bala tu baboiii. Pepete chasy hana dul sae ti aamoo! Jeje me want bananaaa! Uuuhhh. Hahaha gelatooo ti aamoo! La bodaaa hahaha gelatooo bananaaaa hahaha. La bodaaa tulaliloo bee do bee do bee do uuuhhh poulet tikka masala potatoooo jeje aaaaaah."
        text = self.generateParagraph(bananaArray)
        self.view.insert(edit, self.view.sel()[0].begin(), text)

    def generateParagraph(self, wordsArray):
		oneParagraph = ""
		linesNumber = 5 + (10-5) * self.random()
		
		oneParagraph = self.generateLine(wordsArray)
		
		for num in range(1,linesNumber):
			oneParagraph = oneParagraph + generateLine(wordsArray)   
		}
		
		/*Wrap the paragraph inside <p> tags*/
		oneParagraph='<p>'+oneParagraph+'</p>';
		
		return oneParagraph