SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/../hdl/dut.v
VERILOG_SOURCES += $(PWD)/../wrapper_xor/xor_test.v

xor: 
	$(MAKE) sim TOPLEVEL=xor_test MODULE=dut_test
include $(shell cocotb-config --makefiles)/Makefile.sim
