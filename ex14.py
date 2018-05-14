from sys import argv

script, user_name, last_name = argv
prompt = '>'

print "hi %s %s, i am the %s script" % (user_name, last_name, script)
print "i'd like to ask you a few questions."
print "do you like me %s?" % user_name
likes = raw_input(prompt)
print """
alright, so you said %r about liking me
anyway, thx!
""" % likes

