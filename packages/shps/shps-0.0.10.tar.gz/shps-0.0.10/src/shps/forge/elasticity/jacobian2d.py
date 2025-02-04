#!/usr/bin/env nemesis
# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2023, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information. 
# =================================================================================================
# Initial attempt to compute plane strain Jacobian matrices symbolically.
# PREREQUISITES:  sympy
# ----------------------------------------------------------------------
#
# https://github.com/geodynamics/pylith/blob/main/libsrc/pylith/fekernels/jacobian2d.py
from sympy.abc import x, y
import sympy
import sympy.tensor
import sympy.tensor.array
from itertools import product
# ----------------------------------------------------------------------


ndim = 2
numComps = 2
ndimRange = range(ndim)
numCompsRange = range(numComps)

# ----------------------------------------------------------------------


def writeJacobianUniqueVals(f, jacobian):
    """Function to write unique values and assign them to variables.
    """

    # Unique entries in Jacobian, excluding 0.
#   uniqueVals = list(set(jacobian))
    uniqueVals = list(set([jacobian[i,j,k,l] 
                           for i, j, k, l in product(numCompsRange, ndimRange, numCompsRange, ndimRange)]))
    if 0 in uniqueVals:
        uniqueVals.remove(0)
    numUniqueVals = len(uniqueVals)
    uniqueValNames = [None for i in range(numUniqueVals)] # * [None]
    usedVals = []

    f.write("/* Unique components of Jacobian. */\n")
    outFmt = "const PylithReal %s = %s;\n"

    # Loop over Jacobian components in original PyLith order.
    ui = 0
    for i, j, k, l in product(numCompsRange, ndimRange, numCompsRange, ndimRange):
        ii = i + 1
        jj = j + 1
        kk = k + 1
        ll = l + 1
        if (jacobian[i, j, k, l] in uniqueVals and jacobian[i, j, k, l] not in usedVals):
            testInd = uniqueVals.index(jacobian[i, j, k, l])
            comp = "C" + repr(ii) + repr(jj) + repr(kk) + repr(ll)
            f.write(outFmt % (comp, jacobian[i, j, k, l]))
            uniqueValNames[testInd] = comp
            usedVals.append(jacobian[i, j, k, l])
            ui += 1
        if (ui == numUniqueVals):
            break

    return (uniqueVals, uniqueValNames)


def writeJacobianComments(f, jacobian):
    """Function to write correspondence between PETSc and PyLith Jacobian values.
    """

    f.write("/* j(f,g,df,dg) = C(f,df,g,dg)\n\n")
    outFmt = "%2d:  %s = %s = %s\n"

    # Loop over Jacobian components in new order.
    ui = 0
    for i, k, j, l in product(numCompsRange, numCompsRange, ndimRange, ndimRange):
        ii = i + 1
        jj = j + 1
        kk = k + 1
        ll = l + 1
        pyComp = "C" + repr(ii) + repr(jj) + repr(kk) + repr(ll)
        peComp = "j" + repr(i) + repr(k) + repr(j) + repr(l)
        f.write(outFmt % (ui, peComp, pyComp, jacobian[i, j, k, l]))
        ui += 1

    f.write("*/\n\n")

    return


def writeJacobianNonzero(f, jacobian, uniqueVals, uniqueValNames):
    """Function to write nonzero Jacobian entries using predefined value names.
    """

    f.write("/* Nonzero Jacobian entries. */\n")

    outFmt = "Jg3[%d] -=  %s; /* %s */\n"

    # Loop over Jacobian components in new order.
    ui = 0
    for i, k, j, l in product(numCompsRange, numCompsRange, ndimRange, ndimRange):
        ii = i + 1
        jj = j + 1
        kk = k + 1
        ll = l + 1
        peComp = "j" + repr(i) + repr(k) + repr(j) + repr(l)
        if (jacobian[i, j, k, l] != 0) and (jacobian[i, j, k, l] in uniqueVals):
            ind = uniqueVals.index(jacobian[i, j, k, l])
            f.write(outFmt % (ui, uniqueValNames[ind], peComp))

        ui += 1

    return


def writeJacobianInfo(fileName, jacobian):
    """Function to write info about Jacobian.
    """
    with open(fileName, 'w') as f:
        (uniqueVals, uniqueValNames) = writeJacobianUniqueVals(f, jacobian)
        writeJacobianComments(f, jacobian)
        writeJacobianNonzero(f, jacobian, uniqueVals, uniqueValNames)
    return

def main():
    # Constants.
    zero  = sympy.sympify(0)
    one   = sympy.sympify(1)
    two   = sympy.sympify(2)
    three = sympy.sympify(3)

    # Define basis and displacement vector.
    #u1, u2 = sympy.symbols('u1 u2', type="Function")
    u1 = sympy.Function('u1')
    u2 = sympy.Function('u2')
    X = [x, y]
    U = [u1(x, y), u2(x, y)]

    # Deformation gradient, transpose, and strain tensor.
    defGrad = sympy.tensor.array.derive_by_array(U, X)
    defGradTranspose = sympy.tensor.array.Array(defGrad.tomatrix().transpose())
    strain = (defGrad + defGradTranspose)/two

    # Define volumetric strain and deviatoric strain.
    volStrain = sympy.tensor.array.tensorcontraction(strain, (0, 1))
    volStrainArr = sympy.tensor.array.tensorproduct(volStrain, sympy.eye(ndim))
    devStrain = strain - volStrainArr/three

    # Define displacements and strains for previous time step.
    #un1, un2 = sympy.symbols('un1 un2', type="Function")
    un1 = sympy.Function('un1')
    un2 = sympy.Function('un2')
    Un = [un1(x, y), un2(x, y)]
    defGradN = sympy.tensor.array.derive_by_array(Un, X)
    defGradNTranspose = sympy.tensor.array.Array(defGradN.tomatrix().transpose())
    strainN = (defGradN + defGradNTranspose)/two
    meanStrainN = sympy.tensor.array.tensorcontraction(strainN, (0, 1))/three
    meanStrainNArr = sympy.tensor.array.tensorproduct(meanStrainN, sympy.eye(ndim))
    devStrainN = strainN - meanStrainNArr

    # Put in dummy tensor for things that don't depend on U.
    aa, ab, ba, bb = sympy.symbols('aa ab ba bb')
    dummyTensor = sympy.tensor.array.Array([[aa, ab],
                                            [ba, bb]])

    # ----------------------------------------------------------------------
    # Elastic isotropic stress.
    fileName = 'elasticity-elas_iso2d.txt'
    (lambdaModulus, shearModulus,
     bulkModulus) = sympy.symbols('lambdaModulus shearModulus bulkModulus')
    stress = lambdaModulus * volStrainArr + two * shearModulus * strain
    meanStress = sympy.tensor.array.tensorcontraction(stress, (0, 1))/three
    meanStressArr = sympy.tensor.array.tensorproduct(meanStress, sympy.eye(ndim))
    devStress = stress - meanStressArr
    jacobian1 = sympy.tensor.array.derive_by_array(stress, defGrad)
    jacobian2 = sympy.tensor.array.derive_by_array(stress, defGradTranspose)
    jacobian = (jacobian1 + jacobian2)/two
    print(jacobian)
    writeJacobianInfo(fileName, jacobian)

    # ----------------------------------------------------------------------
    # Maxwell viscoelastic.
    fileName = 'elasticity-max_iso2d.txt'
    shearModulus, deltaT, tauM = sympy.symbols('shearModulus deltaT tauM')
    expFac = sympy.exp(-deltaT/tauM)
    dq = sympy.symbols('dq')
    delHArr = dq * (devStrain - devStrainN)
    # Dummy tensor represents viscous strain from previous time step.
    hMArr = expFac * dummyTensor + delHArr
    meanStress = bulkModulus * volStrainArr
    devStress = two * shearModulus * hMArr
    stress = meanStress + devStress
    jacobian1 = sympy.tensor.array.derive_by_array(stress, defGrad)
    jacobian2 = sympy.tensor.array.derive_by_array(stress, defGradTranspose)
    jacobian = (jacobian1 + jacobian2)/two
    writeJacobianInfo(fileName, jacobian)

    # ----------------------------------------------------------------------
    # Generalized Maxwell viscoelastic.
    fileName = 'elasticity-genmax_iso2d.txt'
    (shearModulus, deltaT, tauM1, tauM2, tauM3,
     shearModulusRatio_1, shearModulusRatio_2,
     shearModulusRatio_3) = sympy.symbols(
        'shearModulus deltaT tauM1 tauM2 tauM3 shearModulusRatio_1 shearModulusRatio_2 shearModulusRatio_3')
    shearModulusRatio_0 = sympy.symbols('shearModulusRatio_0')
    expFac1 = sympy.exp(-deltaT/tauM1)
    expFac2 = sympy.exp(-deltaT/tauM2)
    expFac3 = sympy.exp(-deltaT/tauM3)
    dq_1, dq_2, dq_3 = sympy.symbols('dq_1 dq_2 dq_3')
    delHArr1 = dq_1 * (devStrain - devStrainN)
    delHArr2 = dq_2 * (devStrain - devStrainN)
    delHArr3 = dq_3 * (devStrain - devStrainN)
    # Dummy tensors represent viscous strain from previous time step.
    hMArr1 = expFac1 * dummyTensor + delHArr1
    hMArr2 = expFac2 * dummyTensor + delHArr2
    hMArr3 = expFac3 * dummyTensor + delHArr3
    meanStress = bulkModulus * volStrainArr
    devStress = two * shearModulus * (shearModulusRatio_0 * devStrain +
                                      shearModulusRatio_1 * hMArr1 +
                                      shearModulusRatio_2 * hMArr2 +
                                      shearModulusRatio_3 * hMArr3)
    stress = meanStress + devStress
    jacobian1 = sympy.tensor.array.derive_by_array(stress, defGrad)
    jacobian2 = sympy.tensor.array.derive_by_array(stress, defGradTranspose)
    jacobian = (jacobian1 + jacobian2)/two
    writeJacobianInfo(fileName, jacobian)


if __name__ == "__main__":
    main()
