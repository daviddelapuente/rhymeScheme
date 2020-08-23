from rhymeScheme import *

def runTests0():
    print("begin test 0")
    assert(rhyme_score("","")==0)
    assert(rhyme_score(None,None)==0)
    assert(rhyme_score(None,"cat")==0)
    assert(rhyme_score("cat",None)==0)
    assert(rhyme_score("","cat")==0)
    assert(rhyme_score("cat","")==0)
    print("test0 succesfull")

def runTests1():
    print("begin test 1")
    assert(rhyme_score("cat","cat")==0)
    assert(rhyme_score("cat","scat")==0)
    assert(rhyme_score("scat","cat")==0)
    assert(rhyme_score("pare","compare")==0)
    assert(rhyme_score("cat","hat")>0)
    assert(rhyme_score("hat","cat")>0)
    print("test1 succesfull")

def runTests2():
    print("begin test 2")

    print(rhyme_score("commit","submit"))
    print(word_similarity("commit","submit"))

    print(rhyme_score("commit","submits"))
    print(word_similarity("commit","submits"))

    print(rhyme_score("cat","hat"))
    print(word_similarity("cat","hat"))

    print(rhyme_score("three","me"))
    print(word_similarity("three","me"))

    print(rhyme_score("misery","polite"))
    print(word_similarity("misery","polite"))

    print(rhyme_score("misery","mystery"))
    print(word_similarity("misery","mystery"))
    
    print("end test 2")

def runTests3():
    #this test uses a function that is optimized
    print("begin test 3")
    print(rhyme_scoreOPT("commit","submit"))
    print(rhyme_scoreOPT("commit","submits"))
    print(rhyme_scoreOPT("cat","hat"))
    print(rhyme_scoreOPT("three","me"))
    print(rhyme_scoreOPT("misery","polite"))
    print(rhyme_scoreOPT("misery","mystery"))
    print("end test 3")

def borderCasesTest():
    #this will fail because, hat is sufix of chat. but is not a phone sufix, and that is not implemented yet
    assert(rhyme_score("chat","hat")>0)

def runTests():
    runTests0()
    runTests1()
    runTests2()
    runTests3()
runTests()