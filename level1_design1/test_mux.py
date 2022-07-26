# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    sel=24
    inp0=3
    inp30=0

    #input driving
    dut.sel.value = sel
    dut.inp0.value = inp0
    dut.inp30.value = inp30

    await Timer(2,units='ns')
    assert dut.out.value == inp0, "MUX correct"
    cocotb.log.info('##### CTB: Develop your test here ########')
