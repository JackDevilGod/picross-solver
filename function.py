def create_board(size: str) -> [[str]]:
    """
    creates the picross board
    :param size: the size in x X y format
    :return:
    """
    list_size: [str] = size.split("X" or "x")
    horizontal_size: int = int(list_size[0])
    vertical_size: int = int(list_size[1])

    return [["[ ]" for _ in range(horizontal_size)] for _ in range(vertical_size)]


def main():
    return


if __name__ == "__main__":
    main()
