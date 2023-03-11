def variacao (arg, *vartup):
    print('primeiro argumento: ', arg)
    for intem in vartup:
        print ('o outro argumento: ', intem)
        return;
variacao (10)
variacao("pao de queiio", 'cafe')
variacao('beincando', 'com argumento', 'segundo mais ainda')
variacao(1)
variacao(2)
variacao(3)
variacao(4)
variacao(5)
variacao(6)
