def multiziperator(*args):
    return (one_element
            for one_index in zip(*args)
            for one_element in one_index)


if __name__ == '__main__':
    pass
