import sublime, sublime_plugin, random

class MinionIpsum():
	
	def run(self, edit):
		bananaArray = ["pepete","aaaaaah","uuuhhh","jiji","hahaha","jeje","wiiiii","bananaaaa","bappleees","potatoooo","para tu","la bodaaa","poulet tikka masala","daa","hana dul sae","belloo!","poopayee","tank yuuu!","me want bananaaa!","underweaaar","bee do bee do bee do","tulaliloo","ti aamoo!","tatata bala tu","baboiii","po kass","gelatooo","butt","chasy"]
		latinArray = ["sit amet", "consectetur", "adipisicing", "elit", "sed", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua", "enim", "ad", "minim", "veniam", "quis", "nostrud", "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "commodo", "consequat", "duis", "aute", "irure", "dolor", "reprehenderit", "voluptate", "velit", "esse", "cillum","occaecat", "qui", "officia"]

		text = self.generateParagraph(bananaArray)
		self.view.insert(edit, self.view.sel()[0].begin(), text)

	def generateParagraph(self, wordsArray):
		oneParagraph = ""
		linesNumber = random.randrange(5,10)
		oneParagraph = self.generateLine(wordsArray)

		for num in range(1,linesNumber):
			oneParagraph = oneParagraph + self.generateLine(wordsArray)   

		oneParagraph='<p>'+oneParagraph+'</p>';

		return oneParagraph

	def generateLine(self, wordsArray):
		oneLine = ""
		wordsNumber = random.randrange(5,10)
		wordsArrayLength = len(wordsArray)
		wordRandomIndex = random.randrange(5, wordsArrayLength);
		firstLine = True

		if(firstLine):
			oneLine = "Minions ipsum"
			firstLine=False
		else:
			oneLine=wordsArray[wordRandomIndex];
		
		for num in range(0, wordsArrayLength):
			wordRandomIndex = random.randrange(num, len(wordsArray));		
			wordRandom = wordsArray[wordRandomIndex]

			oneLine=oneLine + ' ' + wordRandom;   

		return oneLine
