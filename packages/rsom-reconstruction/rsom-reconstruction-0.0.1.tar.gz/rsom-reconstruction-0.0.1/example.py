from rsom_reconstruction import SensitivityField, saft_matfile_adapter, recon2rgb, write_to_matfile
import matplotlib.pyplot as plt
from time import time

def main():

    # path to .mat file containing the recorded data
    data_path = '...'

    start = time()

    sensitivity = SensitivityField()
    recon = saft_matfile_adapter(data_path, sensitivity, verbose=True)

    print('Elapsed time:', time() - start)

    write_to_matfile(data_path, recon) # automatically adds '_LF' and '_HF' to the path

    recon = recon2rgb(recon).get()
    plt.imshow(recon.max(1))
    plt.show()


if __name__ == '__main__':
    main()