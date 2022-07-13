import numpy as np
import glob
import os

class PyLebedev:
    def __init__(self):
        """
        Initialize class
        """
        # load all files
        files = glob.glob(os.path.join(os.path.dirname(__file__), 'data', '*.txt'))

        self.datasource = dict()
        for file in files:
            order = os.path.basename(file).split('_')[1].split('.')[0]
            self.datasource[order] = file
            
    def get_points_and_weights(self, order, solid_angles=False):
        """
        Return Lebedev coefficients
        """
        if ('%03i' % order) not in self.datasource.keys():
            raise Exception('Cannot find order %i in datasource. Available orders are: %s' \
                            % (order, [key for key in self.datasource.keys()]))
        else:
            data = np.loadtxt(self.datasource['%03i' % order])
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
        
    def get_num_points(self, order):
        """
        Get number of points from Lebedev order
        """
        if ('%03i' % order) not in self.datasource.keys():
            raise Exception('Cannot find order %i in datasource. Available orders are: %s' \
                            % (order, [key for key in self.datasource.keys()]))
        else:
            data = np.loadtxt(self.datasource['%03i' % order])
            return data.shape[0]