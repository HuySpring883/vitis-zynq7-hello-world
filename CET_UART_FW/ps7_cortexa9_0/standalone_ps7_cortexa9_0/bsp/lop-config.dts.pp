# 0 "C:\\Users\\fall4\\Documents\\Cora-Z7_07S\\Vitis\\CET_UART_FW\\CET_UART_FW\\ps7_cortexa9_0\\standalone_ps7_cortexa9_0\\bsp\\lop-config.dts"
# 0 "<built-in>"
# 0 "<command-line>"
# 1 "C:\\Users\\fall4\\Documents\\Cora-Z7_07S\\Vitis\\CET_UART_FW\\CET_UART_FW\\ps7_cortexa9_0\\standalone_ps7_cortexa9_0\\bsp\\lop-config.dts"

/dts-v1/;
/ {
        compatible = "system-device-tree-v1,lop";
        lops {
                lop_0 {
                        compatible = "system-device-tree-v1,lop,load";
                        load = "assists/baremetal_validate_comp_xlnx.py";
                };

                lop_1 {
                    compatible = "system-device-tree-v1,lop,assist-v1";
                    node = "/";
                    outdir = "C:/Users/fall4/Documents/Cora-Z7_07S/Vitis/CET_UART_FW/CET_UART_FW/ps7_cortexa9_0/standalone_ps7_cortexa9_0/bsp";
                    id = "module,baremetal_validate_comp_xlnx";
                    options = "ps7_cortexa9_0 C:/Xilinx/Vitis/2024.2/data/embeddedsw/lib/sw_services/xilffs_v5_3/src C:/Users/fall4/Documents/Cora-Z7_07S/Vitis/CET_UART_FW/_ide/.wsdata/.repo.yaml";
                };

        };
    };
