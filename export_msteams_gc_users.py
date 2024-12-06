import re
'''
this code lists out all the users from an ms teams group chat

find the group chat you want to use this for
scroll up to that group chat and you can find the expand participants button
however we only want the list of users, so we have this code to exactly do that
'''
unparsed = input()

names = re.findall(r'added ([A-Z][A-Z\s.]+) to the chat', unparsed)
for name in names:
    print(name)