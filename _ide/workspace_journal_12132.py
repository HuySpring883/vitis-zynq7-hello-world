# 2025-01-01T15:41:01.677584200
import vitis

client = vitis.create_client()
client.set_workspace(path="CET_UART_FW")

platform = client.create_platform_component(name = "CET_UART_FW",hw_design = "$COMPONENT_LOCATION/../design_1_wrapper.xsa",os = "standalone",cpu = "ps7_cortexa9_0",domain_name = "standalone_ps7_cortexa9_0")

platform = client.get_component(name="CET_UART_FW")
domain = platform.get_domain(name="standalone_ps7_cortexa9_0")

status = domain.set_config(option = "os", param = "standalone_stdin", value = "ps7_coresight_comp_0")

status = domain.set_config(option = "os", param = "standalone_stdout", value = "ps7_coresight_comp_0")

status = platform.build()

status = platform.update_desc(desc="CET_UART_FW")

comp = client.create_app_component(name="CET_UART_FW_App",platform = "$COMPONENT_LOCATION/../CET_UART_FW/export/CET_UART_FW/CET_UART_FW.xpfm",domain = "standalone_ps7_cortexa9_0")

client.delete_component(name="CET_UART_FW_App")

status = domain.set_lib(lib_name="xilffs", path="C:\Xilinx\Vitis\2024.2\data\embeddedsw\lib\sw_services\xilffs_v5_3")

comp = client.create_app_component(name="CET_UART_FW_App",platform = "$COMPONENT_LOCATION/../CET_UART_FW/export/CET_UART_FW/CET_UART_FW.xpfm",domain = "standalone_ps7_cortexa9_0")

vitis.dispose()

