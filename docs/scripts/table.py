from pylebedev import PyLebedev

leblib = PyLebedev()

for o,n in zip(leblib.get_orders_list(), leblib.get_nrpoints_list()):
    print('* - %i' % o)
    print('  - %i' % n)