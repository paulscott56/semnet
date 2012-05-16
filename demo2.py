from semnet import *

from tostr import tostr
import string

isa = GetIsA()
example = GetExampleOf()

gRelations = {'isa':isa, 'exampleOf':example }
gEntities = {}


def AskYesNo(prompt, default='Y'):
	while 1:
		ans = raw_input(prompt + ' [' + default + '] ')
		if len(ans) > 1: ans = ans[0]
		if ans == '': ans = default
		if ans == 'y' or ans == 'Y': return 1
		if ans == 'n' or ans == 'N': return 0
		print ("Please enter Y or N.")


def handleCommand(cmd, entities=gEntities, relations=gRelations):
	# respond to a command from the user
	cmd = string.lower(cmd)
	words = string.split(cmd)
	if words[0] == 'entity' or words[0] == 'e':
		entities[words[1]] = Entity(words[1])
	elif words[0] == 'relation' or words[0] == 'r':
		trans = AskYesNo("Transitive?")
		opp = string.lower(raw_input("Opposite? "))
		relations[words[1]] = Relation(words[1],trans)
		if opp:
			relations[opp] = Relation(opp,trans, \
				relations[words[1]])
	elif words[0] == 'list':
		print "Entities:", tostr(entities.keys())
		print "Relations:", tostr(relations.keys())
	else:
		agent = entities[words[0]]
		relation = relations[words[1]]
		if words[2][-1] == '?':
			object = entities[words[2][:-1]]
			handleQuestion( agent, relation, object )
		else:
			object = entities[words[2]]
			handleStatement( agent, relation, object )

def handleQuestion( agent, relation, object ):
	if relation(agent,object): print "yes"
	else: print "no"

def handleStatement( agent, relation, object ):
	if relation(agent,object):
		print "I already knew that."
	else:
		Fact( agent, relation, object )
		print "OK."




print "Ready.  Enter 'quit' (without quotes) to exit."
cmd = ''
while cmd != 'quit':
	cmd = raw_input("Command? ")
	if cmd != 'quit':
#		try:
			handleCommand(cmd)
#		except:
#			print "Error in command."
#			print "Perhaps you used an undefined term?"

