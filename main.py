# This is a sample Python script.

# https://dx-analytics.com/02_dx_models.html

#The model classes represent the fundamental building blocks to model a financial market. They are used to represent the fundamental risk factors driving uncertainty (e.g. a stock, an equity index an interest rate). The following models are available:
#geometric_brownian_motion: Black-Scholes-Merton (1973) geometric Brownian motion
#jump_diffusion: Merton (1976) jump diffusion
#stochastic_volatility: Heston (1993) stochastic volatility model

#stoch_vol_jump_diffusion: Bates (1996) stochastic volatility jump diffusion

#sabr_stochastic_volatility: Hagan et al. (2002) stochastic volatility model
#mean_reverting_diffusion: Vasicek (1977) short rate model
#square_root_diffusion: Cox-Ingersoll-Ross (1985) square-root diffusion
#square_root_jump_diffusion: square-root jump diffusion (experimental)
#square_root_jump_diffusion_plus: square-root jump diffusion plus term structure (experimental)
import dt as dt
import np as np
from dx import *
from pylab import plt
plt.style.use('seaborn')
np.set_printoptions(precision=3)

#Throughout this section we fix a constant_short_rate discounting object.
r = constant_short_rate('r', 0.01)

#To instantiate any kind of model class, you need a market_environment object conataining a minimum set of data (depending on the specific model class).
me = market_environment(name='me', pricing_date=dt.datetime(2015, 1, 1))

#For the geometric Browniam motion class, the minimum set is as follows with regard to the constant parameter values.
# Here, we simply make assumptions,
# in practice the single values would, for example be retrieved from a data service provider like Thomson Reuters or Bloomberg.
# The frequency parameter is according to the pandas frequency conventions (cf. http://pandas.pydata.org/pandas-docs/stable/timeseries.html).

me.add_constant('initial_value', 36.)
me.add_constant('volatility', 0.2)
me.add_constant('final_date', dt.datetime(2015, 12, 31))
  # time horizon for the simulation
me.add_constant('currency', 'EUR')
me.add_constant('frequency', 'M')
  # monthly frequency; paramter accorind to pandas convention
me.add_constant('paths', 1000)
  # number of paths for simulation