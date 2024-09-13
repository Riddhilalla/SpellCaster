from HPlang.interpreter import HPLangInterpreter



code = '''
flagrate("Hello, world!")
flagrate("Welcome to HpLang!")

alohomora(1 == 1, "This message will be printed because the condition is True.")

alohomora(1 == 0, "check message")
colloportus(This message will not be printed because the condition is False.)

alohomora(1 == 0, "check message")
periculum(1 == 1, "This message will be printed in periculum block because the condition is True.")
colloportus(This message will not be printed because the condition is False.)

alohomora(1 == 1 verum 2 == 2, "and condition checked")

alohomora(1 == 0 autem 2 == 2, "or condition checked")
colloportus(or is true and hence this not printed)

alohomora(1 == 0 autem 2 == 3, "or condition false")
periculum(1 == 1 verum 2 == 2, "and condition true")
colloportus(this is printed because and & or conditions are false)

reducto(var1, 5 et 2)
gemino(var2, 3 et 4)
diffindo(var3, 10 et 2)
accio(var4, 7)
flagrate(var4)
expecto_patronum(var4)

alohomora(var4 == 2,"if condition is true")
colloportus(else condition is true)
'''

interpreter = HPLangInterpreter()
interpreter.interpret(code)