import molflow.definitions as mf


wf = mf.WorkflowDefinition("parameterize_small_molecule")
__workflow__ = wf

# Functions
parameterize = mf.Function(sourcefile='./functions.py',
                           funcname='parameterize_small_molecule')


# Inputs
mol = wf.add_input('ligand', type='mdt', description='Molecule to parameterize.')
ligand_code = wf.add_input('ligand_code',
                           '3-letter ligand code',
                           default='UNL',
                           type='str')
forcefield = wf.add_input('forcefield',
                          'Forcefield type',
                          default='gaff2',
                          type='str')
partial_charges = wf.add_input('partial_charges',
                               'Partial charge calculation method',
                               default='am1-bcc',
                               type='str')

# DAG
frcmod, libfile = parameterize(mol, ligand_code, forcefield, partial_charges)


# Outputs
wf.set_output(frcmod, 'mol.frcmod', type='File')
wf.set_output(libfile, 'mol.lib', type='File')
