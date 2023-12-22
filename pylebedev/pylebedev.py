import numpy as np
import glob
import os
from numpy import array as ndarray

class PyLebedev:
    def __init__(self):
        """
        Construct the Lebedev coefficient library
        """        
        # load all files
        files = glob.glob(os.path.join(os.path.dirname(__file__), 'data', '*.txt'))

        # store file locations
        self.__datasource = dict()
        for file in files:
            order = os.path.basename(file).split('_')[1].split('.')[0]
            self.__datasource[order] = file
            
    def get_points_and_weights(self, order:int, solid_angles:bool=False) -> (ndarray, ndarray):
        """
        Get the Lebedev coefficients

        Parameters
        ----------
        order : int
            Order of the method
        solid_angles : bool, optional
            Whether to give the result using solid angles or by Cartesian coordinates on the unit sphere, by default False

        Returns
        -------
        (ndarray,ndarray)
            Sampling point positions and weights

        Raises
        ------
        Exception
            When invalid order is requested
        """        
        if ('%03i' % order) not in self.__datasource.keys():
            raise Exception('Cannot find order %i in datasource. Available orders are: %s' \
                            % (order, [key for key in self.__datasource.keys()]))
        else:
            data = np.loadtxt(self.__datasource['%03i' % order])
            angles = data[:,0:2]
            weights = data[:,2]
            
            # convert angles to radians
            theta = np.radians(angles[:,0])
            phi = np.radians(angles[:,1])

            if solid_angles:
                return np.array(np.vstack([theta, phi])).transpose(), weights

            # produce unit sphere vectors
            x = np.cos(theta) * np.sin(phi)
            y = np.sin(theta) * np.sin(phi)
            z = np.cos(phi)

            return np.array(np.vstack([x,y,z])).transpose(), weights
        
    def get_num_points(self, order:int) -> list[int]:
        """
        Get the number of points for a specific Lebedev order

        Parameters
        ----------
        order : int
            Order of the quadrature

        Returns
        -------
        list[int]
            Number of points

        Raises
        ------
        Exception
            WHen the order is not available.
        """        
        if ('%03i' % order) not in self.__datasource.keys():
            raise Exception('Cannot find order %i in datasource. Available orders are: %s' \
                            % (order, [key for key in self.__datasource.keys()]))
        else:
            data = np.loadtxt(self.__datasource['%03i' % order])
            return data.shape[0]
        
    def get_orders_list(self) -> list[int]:
        """
        Get a list of orders

        Returns
        -------
        list[int]
            Sorted list of orders
        """        
        res = [int(i) for i in self.__datasource.keys()]
        res.sort()
        return res
    
    def get_nrpoints_list(self) -> list[int]:
        """
        Get a list of sampling points per order

        Returns
        -------
        list[int]
            Sorted list of sampling points per order
        """        
        res = [int(self.get_num_points(o)) for o in self.get_orders_list()]
        res.sort()
        return res