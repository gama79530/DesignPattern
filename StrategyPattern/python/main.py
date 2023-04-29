import Computer
# import Computer.CPU
# import Computer.GPU

computer = Computer.Computer()
cpu = Computer.CPU.AMD_Ryzen7_3700X()
gpu2 = Computer.GPU.NVIDIA_GeForce_GTX_1660_SUPER()
computer.cpu = cpu
computer.gpu2 = gpu2

computer.showInfo()