import sublime, sublime_plugin

class MinionIpsum(sublime_plugin.TextCommand):
	def run(self, edit):
		bananaArray = array("pepete","aaaaaah","uuuhhh","jiji","hahaha","jeje","wiiiii","bananaaaa","bappleees","potatoooo","para tu","la bodaaa","poulet tikka masala","daa","hana dul sae","belloo!","poopayee","tank yuuu!","me want bananaaa!","underweaaar","bee do bee do bee do","tulaliloo","ti aamoo!","tatata bala tu","baboiii","po kass","gelatooo","butt","chasy")
		latinArray = array("sit amet", "consectetur", "adipisicing", "elit", "sed", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua", "enim", "ad", "minim", "veniam", "quis", "nostrud", "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "commodo", "consequat", "duis", "aute", "irure", "dolor", "reprehenderit", "voluptate", "velit", "esse", "cillum","occaecat", "qui", "officia")

		text = self.generateParagraph(bananaArray)
		self.view.insert(edit, self.view.sel()[0].begin(), text)

		def generateParagraph(self, wordsArray):
			oneParagraph = ""
			linesNumber = 5 + (10-5) * self.random()

			oneParagraph = self.generateLine(wordsArray)

			for num in range(1,linesNumber):
				oneParagraph = oneParagraph + generateLine(wordsArray)   

			oneParagraph='<p>'+oneParagraph+'</p>';

			return oneParagraph

		def generateLine(self, wordsArray):
			oneLine = ""
			wordsNumber = 5 + (10-5) * self.random()
			wordRandomIndex = 5 + (len(wordsArray)-5) * self.random();
	
			if(firstLine):
				oneLine = "Minions ipsum"
				firstLine=false
			else:
				oneLine=wordsArray[wordRandomIndex];
			
			for num in range(0, len(wordsArray)):
				wordRandomIndex = 5 + (len(wordsArray)-5) * self.random();		
				wordRandom = wordsArray[wordRandomIndex]

				oneLine=oneLine + ' ' + wordRandom;   
	

			return oneLine

	

