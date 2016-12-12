from __future__ import division
__author__ = 'jamiebrew'



# information about a unique string within a corpus
class Ngram(object):

	def __init__(self, string, count=1, reach = 0):
		self.string = string
		self.count = count
		self.after = [{} for _ in range(reach)]
		self.before = [{} for _ in range(reach)]
	
	def add_before(self, token, reach, count):
		if token in self.before[reach-1]:
			target_dict[token] += count
		else:
			target_dict[token] = count
			
	def add_after(self, token, reach, count):	
		if token in self.after[reach-1]:
			target_dict[token] += count
		else:
			target_dict[token] = count
	
	
	
	def __str__(self):
		return self.string+"\ncount: "+str(self.count)

	def __repr__(self):
		return self.string

	def __len__(self):
		return len(self.string)

	def __eq__(self, other):
		return self.__dict__ == other.__dict__


"""
		if reach > 0:
			print 'adding "%s" after "%s" with reach %s' % (token, self.string, reach)
			target_dict = self.after[abs(reach)-1]
		elif reach < 0:
			print 'adding "%s" after "%s" with reach %s' % (token, self.string, reach)
			target_dict = self.before[abs(reach)-1]
		"""	