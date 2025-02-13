from PyCmpltrtok.data.mnist.routines import *

if '__main__' == __name__:
    import itertools
    import matplotlib.pyplot as plt

    def _main():
        """
        To test the data loading procedure for MNIST.

        :return: None
        """
        x_train, y_train, x_test, y_test = load()
        sep('Data loaded')
        for type1, type2 in itertools.product(['x', 'y'], ['train', 'test']):
            var_name = f'{type1}_{type2}'
            xx = locals()[var_name]
            print(var_name, type(xx), xx.shape, xx.dtype)

        sep('Check data')
        def check(x_, y_, type2):
            print(f'Checking x_{type2} and y_{type2} ...')
            plt.figure(figsize=[16, 8])
            spn = 0
            spr = 5
            spc = 10

            def check_i(i):
                nonlocal spn
                spn += 1
                plt.subplot(spr, spc, spn)
                plt.axis('off')
                plt.title(f'{i}: {y_[i]}')
                plt.imshow(x_[i].reshape(*shape_))

            half = spr * spc // 2
            for i in range(half):
                check_i(i)

            for i in range(half):
                check_i(-(i + 1))

            print('Check and close the plotting window to continue ...')
            plt.show()

        for type2 in ['train', 'test']:
            check(locals()[f'x_{type2}'], locals()[f'y_{type2}'], type2)
        print('Over! Data loaded and checked!')

    _main()  # Main program entrance
    sep('All over')
