#region: Modules.
import numpy as np
import matplotlib.pyplot as plt 
import h5py
#endregion

#region: Variables.
#endregion

#region: Functions.
#endregion

#region: Classes.
class BseSpectrumPlot:
    def __init__(
        self,
        eh_filename: str ='absorption_eh.dat',
        noeh_filename: str = 'absorption_noeh.dat',
    ):
        self.eh_filename = eh_filename
        self.noeh_filename = noeh_filename

    def save_data(self):
        abs_eh_data = np.loadtxt(self.eh_filename, dtype='f8', skiprows=4)
        abs_noeh_data = np.loadtxt(self.noeh_filename, dtype='f8', skiprows=4)

        # Save data. 
        with h5py.File('plot_absorption.h5', 'w') as f:
            f.create_dataset('abs_eh', data=abs_eh_data)
            f.create_dataset('abs_noeh', data=abs_noeh_data)

    def save_plot(self, save_filename='absorption.png', show=False):
        abs_eh_data = np.loadtxt(self.eh_filename, dtype='f8', skiprows=4)
        abs_noeh_data = np.loadtxt(self.noeh_filename, dtype='f8', skiprows=4)

        # Save data. 
        with h5py.File('plot_absorption.h5', 'w') as f:
            f.create_dataset('abs_eh', data=abs_eh_data)
            f.create_dataset('abs_noeh', data=abs_noeh_data)
        
        plt.style.use('bmh')
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.plot(abs_eh_data[:, 0], abs_eh_data[:, 1], label='eh')
        ax.plot(abs_noeh_data[:, 0], abs_noeh_data[:, 1], label='noeh')
        
        ax.set_xlabel('Energy (eV)')
        ax.set_ylabel(r'$\epsilon_2$ (arb units)')
        ax.set_title('BSE Absorption Spectrum')
        ax.legend()
        fig.savefig(save_filename)
        if show: plt.show()

#endregion
