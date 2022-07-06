import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution


class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
                
    """
    def __init__(self, mu = 0, sigma = 0, p=0, n=1):

        Distribution.__init__(self, mu, sigma)
        self.p = p
        self.n = n

    def calcuate_mean(self):
        """
        Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
        """
        avg = self.p * self.n

        self.mean = avg

        return self.mean
    
    def calculate_stdev(self):
        """
        Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        sigma = math.sqrt(self.n * self.p *(1 - self.p))
        
        self.stdev = sigma

        return self.stdev
    
    def replace_stats_with_data(self):
        """
        Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """       
        self.n = len(self.data)
        self.p = sum(self.data)/ self.n

        self.calculate_mean()
        self.calculate_stdev()

        return self.p,  self.n

    def plot_bar(self):
        """
        Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """       
        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.ylabel('count')
        plt.xlabe('data')

    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """

        return (1.0 / (self.stdev * math.sqrt(2*math.pi))) * \
            math.exp(-0.5*((k - self.mean) / self.stdev) ** 2)
    
    def plot_histogram_pdf(self, n_spaces = 50):
        """
        Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot    
        """
        min_range = min(self.data)
        max_range = max(self.data)
		
		# calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces
        
        x = []
        y = []
		
		# calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

		# make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')
        
        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()
        
        return x, y

    def __add__(self, other):
        """
        Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        result = Binomial()
        result.p = self.p
        result.n = self.n + other.n

        return result

    def __repr__(self):
        """
        Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        """ 
        return 'mean: {}, standard deviation: {}'.format(self.mean, self.stdev)


