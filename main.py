from utils import get_data, get_filtred_data, get_last_data, get_formatted_data


def main():
    count_last_values = 5
    filtered_empty_from = True

    data = get_data()
    data = get_filtred_data(data, filtered_empty_from)
    data = get_last_data(data, count_last_values)
    data = get_formatted_data(data)

    for row in data:
        print(row)


if __name__ == "__main__":
    main()
