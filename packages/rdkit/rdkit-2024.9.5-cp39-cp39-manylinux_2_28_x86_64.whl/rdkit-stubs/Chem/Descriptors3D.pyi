"""
 Descriptors derived from a molecule's 3D structure

"""
from __future__ import annotations
from rdkit.Chem.Descriptors import _isCallable
from rdkit.Chem import rdMolDescriptors
__all__ = ['CalcMolDescriptors3D', 'descList', 'rdMolDescriptors']
def CalcMolDescriptors3D(mol, confId = None):
    """
    
        Compute all 3D descriptors of a molecule
        
        Arguments:
        - mol: the molecule to work with
        - confId: conformer ID to work with. If not specified the default (-1) is used
        
        Return:
        
        dict
            A dictionary with decriptor names as keys and the descriptor values as values
    
        raises a ValueError 
            If the molecule does not have conformers
        
    """
def _setupDescriptors(namespace):
    ...
descList: list  # value = [('PMI1', <function <lambda> at 0x7f17daa8b430>), ('PMI2', <function <lambda> at 0x7f17cb3e8940>), ('PMI3', <function <lambda> at 0x7f17cb3e89d0>), ('NPR1', <function <lambda> at 0x7f17cb3e8a60>), ('NPR2', <function <lambda> at 0x7f17cb3e8af0>), ('RadiusOfGyration', <function <lambda> at 0x7f17cb3e8b80>), ('InertialShapeFactor', <function <lambda> at 0x7f17cb3e8c10>), ('Eccentricity', <function <lambda> at 0x7f17cb3e8ca0>), ('Asphericity', <function <lambda> at 0x7f17cb3e8d30>), ('SpherocityIndex', <function <lambda> at 0x7f17cb3e8dc0>), ('PBF', <function <lambda> at 0x7f17cb3e8e50>)]
