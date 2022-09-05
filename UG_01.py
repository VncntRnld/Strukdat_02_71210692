import timeit as tm
# from matplotlib import pyplot as plt

# yang di comment buat nyoba bikin grafiknya

def fibo(n):

    a,b = 0,1

    for i in range(n):
        a,b = b, a+b
    
    return a

def fibo_rec(n):
    
    if n <= 1:
        return n

    else:
        return fibo_rec(n-1) + fibo_rec(n-2)

r = range(1,101)
# time_data = []
print("ITERATIVE")
for i in r:
    mulai = tm.default_timer()

    x = fibo(i)

    # w = "{:.15f}" .format(tm.default_timer() - mulai)

    # time_data.append(w)
    print("Input ke-{}| hasil = {} | {} detik" .format(i, x,tm.default_timer() - mulai))

print("----------------------------------------------------------------------------")

# time_data_rec = []
print("RECURSIVE")
for i in r:
    mulai = tm.default_timer()

    x = fibo_rec(i)

    # w = "{:.15f}" .format(tm.default_timer() - mulai)

    # time_data_rec.append(w)
    print("Input ke-{}| hasil = {} | {} detik" .format(i, x,tm.default_timer() - mulai))

# plt.plot(r, time_data, color="red")
# plt.plot(r, time_data_rec, color="blue")
# plt.show()