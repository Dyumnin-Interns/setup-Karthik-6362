SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/../hdl/dut.v

xor: 
	$(MAKE) sim TOPLEVEL=dut MODULE=dut_test
include $(shell cocotb-config --makefiles)/Makefile.sim
