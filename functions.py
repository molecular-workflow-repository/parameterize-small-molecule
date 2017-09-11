__DOCKERIMAGE__ = 'docker.io/autodesk/mst:mdt_ambertools-0.0.1b6'

import moldesign as mdt

def parameterize_small_molecule(mol, ligandcode, ff, charges):
    """
    Create force field parameters for the chosen ligand
    """
    if mol.num_residues != 0:
        return {'success': False,
                'error': "Can only parameterize single-residue molecules"}

    if ligandcode:
        mol.residues[0].resname = ligandcode

    params = mdt.interfaces.ambertools.parameterize(mol,
                                                    ff=ff,
                                                    charges=charges)
    return params.amber_params.frcmod, params.amber_params.lib
