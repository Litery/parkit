from simulation.simulation import DoubleArray


def double_array(_list):
    array = DoubleArray(len(_list))
    for i in range(len(_list)):
        array[i] = _list[i]
    return array
