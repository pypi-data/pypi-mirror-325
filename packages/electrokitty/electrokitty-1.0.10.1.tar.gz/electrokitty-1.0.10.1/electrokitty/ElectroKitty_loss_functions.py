# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:37:58 2024

@author: ozbejv
"""

import numpy as np
import sys
import scipy.signal as scisi
from cpp_ekitty_simulator import cpp_ekitty_simulator

class electrokitty_loss():
    """
    Class that calculates loss function value, given the data and the mechanism
    """
    def __init__(self, kin, species_information, cell_const, isotherm, I_data,
                 fit_Cdl=False, fit_Ru=False, fit_gamamax=False,
                 fit_A=False, fit_iso=False):
        
        self.kin=kin
        self.species_information=species_information
        self.cell_const=cell_const
        self.isotherm=isotherm
        self.ysim=None
        self.I_data=I_data
        self.N_hars=5
        self.base_freq=0
        self.w=0.1*self.base_freq*np.ones(self.N_hars+1)
        self.I_har_exp=None
        self.t=None

        self.Diffusion_const = None
        self.spectators = None
        self.Spatial_info = None
        self.mechanism_list = None
        self.t = None
        self.E_generated = None
        
        self.guess, self.tells, self.gammaposition = self.create_parameter_guess(kin, species_information, 
                                                                                 cell_const, isotherm,
                                                                                 fit_Cdl=fit_Cdl, fit_Ru=fit_Ru, 
                                                                                 fit_gamamax=fit_gamamax,
                                                                                 fit_A=fit_A, fit_iso=fit_iso)
        
    def give_guess(self):
        """
        Gives the list of parameters that it is trying to optimise
        """
        return self.guess
    
    def set_constants(self, Diffusion_const, spectators, Spatial_info, mechanism_list, t, E):
        self.Diffusion_const = Diffusion_const
        self.spectators = spectators
        self.Spatial_info = Spatial_info
        self.mechanism_list = mechanism_list
        self.t = t
        self.E_generated = E
        
    def give_tells_gp(self):
        """
        Gives the tells list and gammaposition
        
        both are parameters that dictate the simulator how to use the guess
        """
        return self.tells, self.gammaposition
    
    def update_ysim(self, ysim):
        """
        Function that updates the function that is used when generating the simulated response
        """
        self.ysim=ysim
        
    def create_ACV_problem(self, freq, N_hars, I_har_exp, t,w):
        """
        Creating the minimisation problem for ACV
        
        needs base frequency, number of harmonics, a list containing harmonics from experimental data,
        time and a list to separate simulated harmonics
        """
        self.base_freq=freq
        self.N_hars=N_hars
        self.I_har_exp=I_har_exp
        self.t=t
        self.w=w
    
    def RMSE(self, guess):
        """
        Calculates and returns the RRMSE value given the guess for the simulator 
        """

        simulator = cpp_ekitty_simulator()
        kin, cp, si, iso = self.unpack_fit_params(guess, self.tells, self.gammaposition)
        simulator.set_parameters(
                              cp, self.Diffusion_const, iso, self.spectators, self.Spatial_info, si, kin, 
                              self.mechanism_list[0], self.mechanism_list[1], 
                              self.mechanism_list[2], self.mechanism_list[3], self.mechanism_list[4]
                              )

        simulator.set_simulation_programm(self.t, self.E_generated)
        i_sim = simulator.simulate()

        return np.sqrt(np.sum((i_sim-self.I_data)**2)/np.sum(self.I_data**2)/len(self.I_data))
    
    def RMSE_har(self, guess):
        """
        Calculates the harmonic average RRMSE given the guess
        """
        simulator = cpp_ekitty_simulator()
        kin, cp, si, iso = self.unpack_fit_params(guess, self.tells, self.gammaposition)
        simulator.set_parameters(
                              cp, self.Diffusion_const, iso, self.spectators, self.Spatial_info, si, kin, 
                              self.mechanism_list[0], self.mechanism_list[1], 
                              self.mechanism_list[2], self.mechanism_list[3], self.mechanism_list[4]
                              )

        simulator.set_simulation_programm(self.t, self.E_generated)
        i_sim = simulator.simulate()
        s, f, i_har_sim=self.FFT_analysis(self.base_freq, self.N_hars, self.w, i_sim, self.t)
        
        L=0
        for i in range(len(i_har_sim)):
            L+=1/(self.N_hars+1)*np.sqrt(np.sum((i_har_sim[i]-self.I_har_exp[i])**2)/np.sum(self.I_har_exp[i]**2)/len(self.I_har_exp[i]))
        return L
    
    def FFT_analysis(self, f,N,w, current, t):
        """
        Same as in the base class
        """
        
        def rectangular(f,w0,w):
            return np.where(abs(f-w0)<=w,1,0)
        
        I_harmonics=[]
        dt=np.average(np.diff(t))
        freq=np.fft.fftfreq(t.shape[-1],d=dt)
        sp=np.fft.fft(current)
        for i in range(N+1):
        #     #kopiram FFT
            if i==0:
                filter_sp=sp.copy()
                window=rectangular(freq,i*f,w[i])
                filter_sp=window*filter_sp
                Inew=np.fft.ifft(filter_sp).real
                I_harmonics.append(Inew)
            else:
                filter_sp=sp.copy()
                window=rectangular(freq,i*f,w[i])+rectangular(freq,-i*f,w[i])
                filter_sp=window*filter_sp
                Inew=np.real(np.fft.ifft(filter_sp))
                Inew=np.fft.ifft(filter_sp).real
                anal_signal=np.abs(scisi.hilbert(Inew))
                I_harmonics.append(anal_signal)
        return sp,freq,I_harmonics
        
    def create_parameter_guess(self, kin, species_information, cell_const, isotherm,
                   fit_Cdl=False, fit_Ru=False, fit_gamamax=False,
                    fit_A=False, fit_iso=False):
        """
        Function that generates the tells list and gammamax
        
        Parameters:
            - kin: kinetic constants to be fitted
            - species_information: initial conditions
            - cell_const: cell constants
            - isotherm: isotherm constants
            
            - fit_: used to create tells
        
        tells: list containing intigers that tell the simulator whetehr to update a certain parameter
        the first element is the number of sets of kinetic parameters, other values are used to correctly distrubute the guess in the simulator
        gammamax: the position in the species_information of the maximum surface concentration that is fitted
        
        """
        tells=[]
        initial_guess=[]
        
        tells.append(len(kin))
        if fit_gamamax:
            gamma_position=species_information[0].index(max(species_information[0]))
        else:
            gamma_position = 0
        n=0
        for step in kin:
            n=n+len(step)
            tells.append(n)
            
            initial_guess+=step
            
        if fit_Ru:
            
            tells.append(n)
            initial_guess.append(cell_const[1])
            n+=1
        else:
            tells.append(0)

        if fit_Cdl:
            
            tells.append(n)
            initial_guess.append(cell_const[2])
            n+=1
        else:
            tells.append(0)
           
        if fit_A:
            
            tells.append(n)
            initial_guess.append(cell_const[3])
            n+=1
        else:
            tells.append(0)
        
        if fit_gamamax:
            
            tells.append(n)
            initial_guess.append(max(species_information[0]))
            n+=1
        else:
            tells.append(0)
        
        if fit_iso:
            
            tells.append(n)
            initial_guess+=isotherm

        else:
            tells.append(0)
        
        return np.array(initial_guess), tells, gamma_position
    
    def unpack_fit_params(self, guess, tells, gamma_position):
        """
        Function takes the guess, tells and gammma_position to reconstruct the lists for the simulator
        """
        guess=guess.tolist()
        kinetics=[]
        cell_params=[self.cell_const[0]]
        spec_info=self.species_information
        
        index1=0

        for i in range(tells[0]):
            
            index2=tells[i+1]
            kinetics.append(guess[index1:index2])
            index1=index2

        if tells[tells[0]+1] != 0:
            cell_params.append(guess[tells[tells[0]+1]]) #Ru
        else:
            cell_params.append(self.cell_const[1])
        
        if tells[tells[0]+2] != 0:
            cell_params.append(guess[tells[tells[0]+2]]) #Cdl
        else:
            cell_params.append(self.cell_const[2])
        
        if tells[tells[0]+3] != 0:
            cell_params.append(guess[tells[tells[0]+3]]) #A
        else:
            cell_params.append(self.cell_const[3])
        
        if tells[tells[0]+4] != 0:
            spec_info[0][gamma_position] = guess[tells[tells[0]+4]] #gammamax
        else:
           pass
           
        if tells[tells[0]+5]!=0:
            isotherm=guess[tells[tells[0]+5]:] #isotherm
        else:
            isotherm=self.isotherm
        
        return kinetics, cell_params, spec_info, isotherm
    
    def create_lower_upper_bounds(self, guess, tells, potential):
        """
        Function creates based on the guess (arameters to be fitted) the lower and upper bounds,
        for either CMA-ES or MCMC. Both algorithms follow the same rules
        
        The default is:
            - alpha: 0,1
            - k0: 0, 100*k0 or 10
            - E0: -0.5+min(E), 0.5+max(E)
            
            - kf, kb: 0,100*k
            
            - Cdl: 0,100*Cdl
            - Ru: 0,100*Ru
            - A: 0,100*A
            - gammamax: 0,100*gammamax
            - isotherm: -100*iso,100*iso or -0.1,0.1 
        """
        guess=guess.tolist()
        lower_bound=[]
        upper_bound=[]
        
        index1=0
        pot_min, pot_max = min(potential)-0.5, max(potential)+0.5
        for i in range(tells[0]):
            index2=tells[i+1]
            if index2 - index1 == 3:
                upper_bound.append(1)
                lower_bound.append(0)
                lower_bound.append(0)
                if guess[index1+1]!=0:
                    upper_bound.append(guess[index1+1]*100)
                else: 
                    upper_bound.append(10)
                
                upper_bound.append(pot_max)
                lower_bound.append(pot_min)
            
            if index2 - index1 == 2:
                lower_bound.append(0)
                lower_bound.append(0)
                
                if guess[index1]!=0:
                    upper_bound.append(guess[index1]*100)
                else: 
                    upper_bound.append(10)
                
                if guess[index1+1]!=0:
                    upper_bound.append(guess[index1+1]*100)
                else: 
                    upper_bound.append(10)
                    
            if index2 - index1 == 1:
                lower_bound.append(0)
                if guess[index1]!=0:
                    upper_bound.append(guess[index1]*100)
                else: 
                    upper_bound.append(10)
            
            index1=index2
        
        if tells[tells[0]+1] != 0: #Ru
            lower_bound.append(0)
            if guess[tells[tells[0]+1]] != 0:
                upper_bound.append(100*guess[tells[tells[0]+1]])
            else:
                upper_bound.append(100)
        
        if tells[tells[0]+2] != 0: #Cdl
            lower_bound.append(0)
            if guess[tells[tells[0]+1]] != 0:
                upper_bound.append(100*guess[tells[tells[0]+2]])
            else:
                upper_bound.append(10**-3)
        
        if tells[tells[0]+3] != 0: #A
            lower_bound.append(0)
            if guess[tells[tells[0]+3]] != 0:
                upper_bound.append(100*guess[tells[tells[0]+3]])
            else:
                upper_bound.append(10**-1) 
        
        if tells[tells[0]+4] != 0: #gammamax
            lower_bound.append(0)
            if guess[tells[tells[0]+4]] != 0:
                upper_bound.append(1000*guess[tells[tells[0]+4]])
            else:
                upper_bound.append(10**-4)
           
        if tells[tells[0]+5]!=0: #isotherm
            check=guess[tells[tells[0]+5]:]
            for param in check:
                lower_bound.append(-25)
                upper_bound.append(10)
        
        lower_bound.append(0)
        upper_bound.append(1)
        
        return lower_bound, upper_bound 
    
    def create_axis_labels(self,tells, a_spec):
        """
        Function takes the tells and species names to return parameter labels for the chain
        """
        
        labels = []
        index1 = 0
        for i in range(tells[0]):
                
            index2=tells[i+1]
            dist = abs(index2-index1)
            if dist == 3:
                labels.append(r"$\alpha"+"_{"+str(i+1)+"}$")
                labels.append(r"$k_{0,"+str(i+1)+"}$")
                labels.append(r"$E^{0'}_{"+str(i+1)+"}$")
            elif dist == 2:
                labels.append(r"$k_{f"+str(i+1)+"}$")
                labels.append(r"$k_{b"+str(i+1)+"}$")
            elif dist == 1:
                labels.append(r"$k_{"+str(i+1)+"}$")
            index1=index2

        if tells[tells[0]+1] != 0:
            labels.append(r"$R_{u}$") #Ru
        else:
            pass
        
        if tells[tells[0]+2] != 0:
            labels.append(r"$C_{dl}$") #Cdl
        else:
            pass
        
        if tells[tells[0]+3] != 0:
            labels.append(r"$A$") #A
        else:
            pass
        
        if tells[tells[0]+4] != 0:
            labels.append(r"$\Gamma_{max}$") #gammamax
        else:
           pass
           
        if tells[tells[0]+5]!=0:
            for spec_name in a_spec: #isotherm
                labels.append(r"$g_{"+spec_name+"}$")
        else:
            pass
        labels.append(r"$\sigma$")
        return labels
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        