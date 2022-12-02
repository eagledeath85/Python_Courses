def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:...{0}, {1}".format(p1, p2))
    print("var-positional (*args)...{0}".format(args))
    print("keyword:.................{0}".format(k))
    print("var-keyword:.............{0}".format(kwargs))


func(1, 2, 3, 4, 5, k=6, k1=7, k2=8)