# -*- coding: utf-8 -*-

import random, re
from bot.core import Answer

reflections = {
    "i": "you",
    "am": "are",
    "i'm": "you are",
    "im": "you are",
    "was": "were",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "myself": "yourself",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "yourself": "myself",
    "you": "me",
    "me": "you",
}

def reflect(token):
    t = token.lower()
    if t in reflections:
        return reflections[t]
    return token

def substitute(text, factsheet, apply_reflection):
    t = text
    if factsheet is not None and len(factsheet) > 0:
        for i in factsheet.get_facts():
            v = i.get_value()
            if apply_reflection:
                v = v.replace('!', ' ').replace('?', ' ').strip()
                v = ' '.join([reflect(j) for j in v.split(' ')])
            t = t.replace('{%s}' % i.get_label(), v)
    return t

def make_answer(templates, subfacts, context):
    random.shuffle(templates)
    for i in templates:
        try:
            t = i
            t = substitute(t, subfacts, True)
            t = substitute(t, context, False)
            if re.search(r"{[a-zA-Z0-9_\-]+}", t) is None:
                return Answer(message=t)
        except:
           pass

    return None

class SmallTalkActions():
    def __init__(self):
        pass

    def smalltalk_base(self, w, subfacts, conclusions, context):
        return(make_answer([
           
            "Tell me more about that.",
            "i cant understand you",
            "i dont uderstand you"
        ], subfacts, context))

    def smalltalk_i_cant(self, w, subfacts, conclusions, context):
        return(make_answer([
            "Sorry, can't understand you",
            "Not sure I understand",
        ], subfacts, context))

    def smalltalk_i_am(self, w, subfacts, conclusions, context):
        return(make_answer([
            "Did you come to me because you are {X}?",
            "How long have you been {X}?",
            "Why do you think you're {X}?",
            "Is it because you are {X} that you came to me?",
            "Do you believe it is normal to be {X}?",
        ], subfacts, context))

    def smalltalk_because(self, w, subfacts, conclusions, context):
        return(make_answer([
            "Is that the real reason?",
            "What other reasons come to mind?",
            "Does that reason apply to anything else?",
            "Don't any other reasons come to mind?",
        ], subfacts, context))

    def smalltalk_sorry(self, w, subfacts, conclusions, context):
        return(make_answer([
            "Please don't apologize.",
            "Apologies are not necessary.",
            "It did not bother me. Please continue.",
        ], subfacts, context))

    def smalltalk_hello(self, w, subfacts, conclusions, context):
        return(make_answer([
            "You need my help? Please state your problem.",
            " Can i help you on something?",
        ], subfacts, context))

    def smalltalk_yes(self, w, subfacts, conclusions, context):
        return(make_answer([
            "OK, but can you explaine your problem?",
            "Please tell me more about your problem.",
            "Why don't you tell me a little more about your problem.",
        ], subfacts, context))

    def smalltalk_no(self, w, subfacts, conclusions, context):
        return(make_answer([
            "sorry for not helping you. you can call 71 111 000 for more info",
        ], subfacts, context))

    def smalltalk_is_it(self, w, subfacts, conclusions, context):
        return(make_answer([
            "Do you think it is {X}?",
            "It could well be that {X}.",
        ], subfacts, context))

    def smalltalk_it_is(self, w, subfacts, conclusions, context):
        return(make_answer([
            "You seem very certain.",
        ], subfacts, context))

    def smalltalk_you_are(self, w, subfacts, conclusions, context):
        return(make_answer([
            "What support can i offer for you?",
            "How can i be helpful?",
            "do you need help?",
            "what can i do for you?",
            "how can i help you?",
        ], subfacts, context))

    def smalltalk_i_dont(self, w, subfacts, conclusions, context):
        return(make_answer([
            "Do you want to {X}?",
            "Do you wish to be able to {X}?",
        ], subfacts, context))

    def smalltalk_i_have(self, w, subfacts, conclusions, context):
        return(make_answer([
            "What is your {X}?",
            "what kind of {X}?"
        ], subfacts, context))

    def smalltalk_i_would(self, w, subfacts, conclusions, context):
        return(make_answer([
            "Could you explain why you would {X}?",
            "Why would you {X}?",
        ], subfacts, context))
        
    def smalltalk_my(self, w, subfacts, conclusions, context):
        return(make_answer([
            "I can see your {X}."
        ], subfacts, context))

    def smalltalk_perhaps(self, w, subfacts, conclusions, context):
        return(make_answer([
            "You don't seem quite certain.",
            "You aren't sure?",
            "How likely, would you estimate?",
        ], subfacts, context))

    def smalltalk_your(self, w, subfacts, conclusions, context):
        return(make_answer([
            "Why are you concerned over my {X}?",
        ], subfacts, context))

    def smalltalk_you_x_me(self, w, subfacts, conclusions, context):
        return(make_answer([
            "Why do you think I {X} ?",
            "What makes you think I {X} ?",
            "Really, I {X} ?",
        ], subfacts, context))

    def smalltalk_different(self, w, subfacts, conclusions, context):
        return(make_answer([
            "How is it different?",
            "What differences do you see?",
            "How?",
        ], subfacts, context))
