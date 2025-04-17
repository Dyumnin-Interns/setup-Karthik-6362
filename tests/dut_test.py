import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def dut_test(dut):
    a = [0,0,1,1]
    b = [0,1,0,1]
    c = [0,1,1,0]
    
    for i in range(4):
    	dut.a.value = a[i]
    	dut.b.value = b[i]
    	await Timer(1,'ns')
    	if dut.y.value != c[i]:
    		print(f"Error in interation {i}")
    	else:
    		print(f"Testcase in iter")
