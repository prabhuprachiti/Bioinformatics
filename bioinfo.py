import operator

class Bioinfo():
	def __init__(self, seq):
		caps=seq.upper()
		self.sequence=caps
		self.seq_dict={"A":"T", "T":"A", "G":"C", "C":"G"}
		self.rev=self.getRev()

		assert self.sequence != "", "Sequence cannot be an empty string!"    	
	sequence = property(operator.attrgetter('_sequence'))
	@sequence.setter
	def sequence(self, testseq):
		for t in testseq:
			if t not in ["A","T","G","C"]:
				raise Exception("Your sequence consists of non A-T-G-C characters..please check your input")
		self._sequence=testseq
			
	def printSeq(self):
		print ("You have entered sequence:%s" %(self.sequence))

	def getRev(self):
		rev = self.sequence[::-1]
		return rev

	def getRevComp(self):
		revComp = "".join(self.seq_dict[s] for s in self.rev)
		return revComp
	
	def isPal(self):
		if self.sequence == self.rev:
			print ("The input is a palindrome")
		else:
			print ("The input is not a palindrome")

	def isSelfComplimentary(self):
		revComp = self.getRevComp()
		if revComp == self.sequence:
			print ("The input is self complementary")
		else:
			print ("The input is not self complementary")


if __name__=="__main__":
	sequence=input("Please enter your desired sequence\n")
	binf=Bioinfo(sequence)
	binf.printSeq()
	
	rev=binf.getRev()
	print ("The reverse of the string is:%s" %(rev))
	
	revComp=binf.getRevComp()
	print ("The reverse complement of the string is:%s" %(revComp))
	
	binf.isPal()
	binf.isSelfComplimentary()
