def fibonacci():
    n = input("Enter the number of terms you require ")
    terms = int(n)

    n_0 = 0
    n_1 = 1
    n_2 = n_1 + n_0
    fibo = [n_0, n_1, n_2]
    
    for i in range(3,terms):
        n_3 = fibo[-1] + fibo[-2]
        fibo.append(n_3)