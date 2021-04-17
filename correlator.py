_omega_list = [
    [11,2,4],
    [3, 5, 1]
]


def correlator(omega_list):
    omega_list_x = [omega[0] for omega in omega_list]
    lst_x = []
    lst_y = []
    lst_z = []
    for i in range(len(omega_list)-1):
        for j in range(len(omega_list)-1-i):
            lst_x.append(omega_list_x[i]*omega_list_x[j])
            lst_y.append(omega_list_x[i] * omega_list_x[j])
            lst_z.append(omega_list_x[i] * omega_list_x[j])

    cor_x = sum(lst_x) / len(lst_x)
    cor_y = sum(lst_y) / len(lst_y)
    cor_z = sum(lst_z) / len(lst_z)

    return cor_x, cor_y, cor_z


correlator(_omega_list)
