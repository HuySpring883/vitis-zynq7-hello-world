# 2025-01-01T16:20:53.727578700
import vitis

client = vitis.create_client()
client.set_workspace(path="CET_UART_FW")

client.delete_component(name="CET_UART_FW_App")

comp = client.create_app_component(name="CET_UART_FW_App",platform = "$COMPONENT_LOCATION/../CET_UART_FW/export/CET_UART_FW/CET_UART_FW.xpfm",domain = "standalone_ps7_cortexa9_0",template = "hello_world")

platform = client.get_component(name="CET_UART_FW")
status = platform.build()

comp = client.get_component(name="CET_UART_FW_App")
comp.build()

vitis.dispose()

vitis.dispose()

