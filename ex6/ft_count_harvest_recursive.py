def print_days(i, days):
    if (i < (days + 1)):
        print("Day", i)
        print_days(i + 1, days)

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    i = 1
    print_days(i, days)
    print("Harvest time!")