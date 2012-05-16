from semnet import *

from tostr import tostr
import string

# get the global "is-a" relationship
isa = GetIsA()

# inverse of "is-a" is "exampleOf"
example = GetExampleOf()

# declare some entities we want to store knowledge about
thing = Entity("thing")
animal = Entity("animal")
bird = Entity("bird")
fish = Entity("fish")
minnow = Entity("minnow")
trout = Entity("trout")
ape = Entity("ape")

# declare some facts: what's what?
Fact(animal, isa, thing)
Fact(ape, isa, animal)
Fact(bird, isa, animal)
Fact(fish, isa, animal)
Fact(trout, isa, fish)
Fact(minnow, isa, fish)

# print out some of the things we know (directly or by induction)
print "trout is:", tostr( trout.objects(isa) )
print "animal is:", tostr( animal.objects(isa) )
print
print "fish:", tostr( fish.objects(example) )
print "fish:", tostr( fish.agents(isa) )
print "animals:", tostr( animal.agents(isa) )
print

# declare size relationships
biggerThan = Relation("bigger than", 1)
smallerThan = Relation("smaller than", 1, biggerThan)

# declare a couple facts
Fact( minnow, smallerThan, trout )
Fact( trout, smallerThan, ape )

# look at all the things we know now!
print "ape is a fish?", isa(ape,fish)
print "minnow is a fish?", isa(minnow,fish)
print "minnow is an animal?", isa(minnow,animal)
print
print "ape bigger than minnow?", biggerThan(ape,minnow)
print "minnow bigger than trout?", biggerThan(minnow,trout)
print "minnow is smaller than:", tostr( minnow.objects(smallerThan) )
print "ape is bigger than:", tostr( ape.objects(biggerThan) )

# declare entities for actions (these are nouns too, you know)
act = Entity("act")
swim = Entity("swim")
walk = Entity("walk")
Fact( swim, isa, act )
Fact( walk, isa, act )

# declare an "ableTo" relation, so we can say who can do what
ableTo = Relation("ableTo", 0)
whatCan = Relation("whatCan", 0, ableTo)

# note that fish can swim and apes can walk
Fact( fish, ableTo, swim )
Fact( walk, whatCan, ape )

# see what we can say about swimming ability
print
print "fish can swim?", ableTo( fish, swim )
print "minnow can swim?", ableTo( minnow, swim )
print "bird can swim?", ableTo( bird, swim )
print "what can swim?", tostr( swim.getObjects(whatCan) )
print "what can act?", tostr( act.getObjects(whatCan) )

# declare a "has" relationship (and its inverse)
has = Relation("has", 0)
whatHas = Relation("whatHas", 0, has)

scales = Entity("scales")
hair = Entity("hair")
Fact( fish, has, scales )
Fact( ape, has, hair )

print
print "minnow has hair?", has( minnow, hair )
print "minnow has scales?", has( minnow, scales )
print "ape has hair?", has( ape, hair )
print "ape has scales?", has( ape, scales )
print "what has scales?", tostr( scales.getAgents(has) )
