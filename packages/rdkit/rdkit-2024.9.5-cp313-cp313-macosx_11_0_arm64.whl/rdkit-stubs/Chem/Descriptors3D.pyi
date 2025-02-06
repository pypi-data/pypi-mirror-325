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
descList: list  # value = [('PMI1', <function <lambda> at 0x1028c1a80>), ('PMI2', <function <lambda> at 0x1028c2160>), ('PMI3', <function <lambda> at 0x1028c2200>), ('NPR1', <function <lambda> at 0x1028c22a0>), ('NPR2', <function <lambda> at 0x1028c2340>), ('RadiusOfGyration', <function <lambda> at 0x1028c23e0>), ('InertialShapeFactor', <function <lambda> at 0x1028c2480>), ('Eccentricity', <function <lambda> at 0x1028c2520>), ('Asphericity', <function <lambda> at 0x1028c25c0>), ('SpherocityIndex', <function <lambda> at 0x1028c2660>), ('PBF', <function <lambda> at 0x1028c2700>)]
