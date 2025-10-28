## This code originates from the CompOSE website. It is used to convert an EOS of our choice from CompOSE's table format, to HDF5 format, compatible with IllinoisGRMHD.
It is written in Fortran. Once the code has compiled, you will be given several prompts regarding formatting of the EOS variables. Please see the ```Instructions``` file provided by my mentor, Pedro Espino, for a complete overview of how the COMPOSE code was used to reformat our EOS data to HDF5 format, as well as some descriptions of variables, their units, and significance.

Here is an example of the COMPOSE code in use:

          Please select the interpolation order (1, 2, or 3) 
          for the temperature T
          >> 3

          Please select the interpolation order (1, 2, or 3) 
          for the baryon density n_b
          >> 3
        
          Please select the interpolation order (1, 2, or 3) 
          for the hadronic charge fraction Y_q
          >> 3
        
          Please select if you want to calculate the EoS of matter in beta-equilibrium.
          1: yes, else: no
          >> 0
        
          Please select if you want the calculate the EoS for given entropy per baryon.
          1: yes, else: no
          >> 0
        
          Please select the tabulation scheme for the parameters from
          0: explicit listing of parameter values
          1: loop form of parameter values
          >> 1
        
          Please enter the minimum and maximum values for the temperature T
          >> 0.1 199

          Please enter the number of grid points
          >> 34

          Please select the scaling of the grid points from
          0: linear
          else: logarithmic
          >> 1
        
          Please enter the minimum and maximum values for the baryon density n_b
          >> 7.59e-11 15.1

          Please enter the number of grid points
          >> 114

          Please select the scaling of the grid points from
          0: linear
          else: logarithmic
          >> 1
        
          Please enter the minimum and maximum values for the hadronic charge fraction Y_q
          >> 0.01 0.562

          Please enter the number of grid points
          >> 71

          Please select the scaling of the grid points from
          0: linear
          else: logarithmic
          >> 0
