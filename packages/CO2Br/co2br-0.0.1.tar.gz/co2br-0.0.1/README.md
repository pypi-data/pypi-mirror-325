## **CO2Br**

This python module is built on the non-iterative approach to compute the phase attributes of $\mathrm{CO_2}$--brine mixtures at geological carbon--storage and sequestration conditions. It can be integeated in large scale isothermal flow and transport simulations. Given a pressure field and temperature, it computes :
```
1. Solubility - carbon-dioxide solubility in brine or pure water
2. Density - density of carbon-dioxide--brine/pure water mixture
3. Viscosity - viscosityof carbon-dioxide--brine/pure water mixture
```
All the attributes can be used to enfore Dirichlet boundary conditions (in numerical simulations) and compute end-member ($\mathrm{CO_2}$ saturated vs unsaturated) quantities.

**applicability range**

pressure and temperature range : 
```
P <= 2000 bar (200 MPa); T<=523.15 degree K (250 degree C)
```
salinity components and molality ranges: 
```
K2SO4 <= 1.5 mol/kg
MgSO4 <= 3.3 mol/kg
NaCl <= 6.0 mol/kg
KCl <= 6.0 mol/kg
MgCl2 <= 2.0 mol/kg
CaCl2 <= 5.0 mol/kg
```
**dependencies**
```
- python 2.0 or higher
- numpy
```

**installation**
It can either be download from PyPI:
```
pip install CO2Br==0.0.1
```
or directly from github:
```
pip install git+https://github.com/TectoArc/CO2Br.git
```
**documentation**
```
m = {"NaCl":1.0, 
        "KCl": 0.0, 
        "MgSO4": 0, 
        "MgCl2": 0.0}
T = 30
P = np.ones([10, 10]) * 50

mco2 = Solubility(P, T).CO2Solubility(m)
d = Density(P, T)
r_co2br, r_br, rw = d.BrineDensity(m, mco2)
s = SolutionViscosity(T, m)
mu_co2br = s.Co2BrineViscosity(rw, mco2)
```
**references**
* D. J. Bradley and K. S. Pitzer (1979). Thermodynamics of Electrolytes. 12. Dielectric Properties of Water and Debye-Hiickel Parameters to 350 $^°\mathrm{C}$ and 1 kbar. Journal of Physical Chemistry, American Chemical Society.
* S. Mao and Z. Duan (2008). The *P,V,T,x* properties of binary aqueous chloride solutions up to T = 573 K and 100 MPa, Journal of Chemical Thermodynamics, Elsevier, doi: 10.1016/j.jct.2008.03.005.
* Huber et al. (2009). New International Formulation for the Viscosity of $\mathrm{H_2O}$, Journal of Physical and Chemical Reference Data, AIP Publishing, doi: https://doi.org/10.1063/1.3088050.
* Dedong Li, Bastian J. Graupnera, Sebastian Bauera (2011). A method for calculating the liquid density for the CO2-H2O-NaCl system under CO2 storage condition, Energy Procedia, Elsevier, doi:10.1016/j.egypro.2011.02.317.
* S. Mao et al. (2017). The PVTx properties of aqueous electrolyte solutions containing $\mathrm{Li^+}$, $\mathrm{Na^+}$, $\mathrm{K^+}$, $\mathrm{Mg^{2+}}$, $\mathrm{Ca^{2+}}$, $\mathrm{Cl^−}$ and $\mathrm{SO_4^{2-}}$ under conditions of CO2 capture and sequestration, Applied Geochemistry, Elsevier, doi: http://dx.doi.org/10.1016/j.apgeochem.2017.10.002.
* H, J, Kretzschmar and W. Wagner (2019). IAPWS industrial formulation 1997 for the thermodynamic properties of water and steam, International Steam Tables: Properties of Water and Steam based on the Industrial Formulation IAPWS-IF97, Springer. 
* X. Sun et al. (2021). A simple model for the prediction of mutual solubility in CO2-brine system at geological conditions, Desalination, Elsevier, doi: https://doi.org/10.1016/j.desal.2021.114972.
* R. Sun et al. (2022). Modeling dynamic viscosities of multi-component aqueous electrolyte solutions containing $\mathrm{Li^+}$, $\mathrm{Na^+}$, $\mathrm{K^+}$, $\mathrm{Mg^{2+}}$, $\mathrm{Ca^{2+}}$, $\mathrm{Cl^−}$ and $\mathrm{SO_4^{2-}}$ and dissolved CO2 under conditions of CO2 sequestration, Applied Geochemistry, Elsevier, doi: https://doi.org/10.1016/j.apgeochem.2022.105347.
