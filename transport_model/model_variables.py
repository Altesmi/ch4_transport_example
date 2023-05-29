cmp_variables = {
    'cmp_element_height':
    ['height of the tree elements', 'm', ("index", "axial_layers", "radial_layers"), 'f4'],
    'cmp_concentration':
    ['Concentration of the gas', 'mol/m^3', ("index", "axial_layers", "radial_layers", "space_layers"), 'f4'],
    'cmp_space_division':
    ['Volume fraction of air / water + cell space in an element', '1',
     ("index", "axial_layers", "radial_layers", "space_layers"), 'f4'],
    'cmp_element_radii':
    ['Radii of each element', 'm', ("index", "axial_layers", "radial_layers"), 'f4'],
    'cmp_head_area':
    ['Head (top) area of each element', 'm^2', ("index", "axial_layers", "radial_layers"), 'f4'],
    'cmp_element_volume':
    ['Volume of each element', 'm^3', ("index", "axial_layers", "radial_layers"), 'f4'],
    'cmp_element_volume_air':
    ['Air volume of each element', 'm^3', ("index", "axial_layers", "radial_layers"), 'f4'],
    'cmp_element_volume_water':
    ['Water volume of each element', 'm^3', ("index", "axial_layers", "radial_layers"), 'f4'],
    'cmp_element_volume_cell':
    ['Cell volume of each element', 'm^3', ("index", "axial_layers", "radial_layers"), 'f4'],
    'cmp_gas_radial_diffusion_coefficient':
    ['Diffusion coefficient of CH4 in each element', 'm^2/s', ("index", "axial_layers", "radial_layers"), 'f4'],
    'cmp_gas_axial_diffusion_coefficient':
    ['Diffusion coefficient of CH4 in each element', 'm^2/s', ("index", "axial_layers", "radial_layers"), 'f4'],
    'cmp_eq_rate':
    ['Equilibration rate of CH4 between water and air', '1/s', ("index"), 'f4'],
    'cmp_velocity':
    ['Sap flow velocity in the tree', 'm/s', ("index", "axial_layers", "radial_layers"), 'f4'],
    'cmp_henry_coef':
    ['Henrys law coefficient Kh = c_water/c_air', '1', ("index"), 'f4'],
    'cmp_temperature':
    ['Temperature of the element', 'K', ("index", "axial_layers", "radial_layers"), 'f4'],
    'cmp_ambient_concentration':
    ['Ambient concentration of the gas', 'mol/m^3', ("index", "axial_layers"), 'f4'],
    'cmp_moles_out':
    ['Amount of gas that has diffused out of the tree', 'mol', ("index", "axial_layers"), 'f4'],
    'cmp_simulation_time':
    ['Simulation time in the gas simulation', 's', ("index"), 'f4'],
    'cmp_gas_radial_diffusion_flux':
    ['Radial Diffusion flux of the compound in the gas phase', 'mol/s', ("index", "axial_layers", "radial_layers"), 'f4'],
    'cmp_gas_axial_diffusion_flux':
    ['Axial diffusion flux of the compound in the gas phase', 'mol/s', ("index", "axial_layers", "radial_layers"), 'f4'],
    'cmp_eq_flux':
    ['Equilibrium flux between aqueous and gas phase of an element', 'mol/s',
     ("index", "axial_layers", "radial_layers", "space_layers"), 'f4'],
     'cmp_aq_axial_advection_flux':
    ['Aqueous phase axial advection flux of the compound', 'mol/s',
     ("index", "axial_layers", "radial_layers",), 'f4'],
     'cmp_moles_in':
    ['Molar amount of the compound inside the tree', 'mol',
     ("index", "axial_layers", "radial_layers", "space_layers"), 'f4']
}
gas_three_dim_vars = [key for key,val in cmp_variables.items() if val[2] == ("index", "axial_layers",
                                                                                       "radial_layers", "space_layers")]
gas_index_dim_vars = [key for key,val in cmp_variables.items() if val[2] == ("index")]
gas_axial_dim_vars = [key for key,val in cmp_variables.items() if val[2] == ("index", "axial_layers")]
