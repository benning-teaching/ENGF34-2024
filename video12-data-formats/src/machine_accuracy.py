import sys

def compute_machine_accuracy():
    epsilon = 1
    while 1 + epsilon > 1:
        epsilon /= 2
    return 2.0*epsilon

if __name__ == "__main__":
    print(f"Machine accuracy eps = {compute_machine_accuracy()}")
    print(f"Machine accuracy with sys.float_info = {sys.float_info.epsilon}")