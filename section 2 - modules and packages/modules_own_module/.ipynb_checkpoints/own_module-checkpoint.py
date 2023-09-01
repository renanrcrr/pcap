if __name__ == '__main__':
    print('File executed directly')
    print(__name__)
else:
    print('File executed as a module')
    print(__name__)