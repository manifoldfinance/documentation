#!/bin/bash
cd src/
cat GasEVO.md TestableGasEVO.md DebugHelper.md TestableGasEVOToken.md ABDKMath64x64.md | tee -a output.md /dev/null
cat GasEVO.md TestableGasEVO.md DebugHelper.md ABDKMath64x64.md >> omnibus.md
cd -
echo "Generated API Documentation"
