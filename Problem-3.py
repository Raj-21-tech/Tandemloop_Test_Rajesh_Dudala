if __name__ == "__main__":
    a = int(input("Enter a: "))
    series = []
    for i in range(1, a * 2):
        if len(series) < a and i % 2 == 1:
            series.append(i)
    if a % 2 == 0:
        series = series[:-1]  # Remove last element if 'a' is even
    print(", ".join(map(str, series)))
