import Computer

if __name__ == '__main__':
    computer = Computer.Computer()
    cpu = Computer.AMD_Ryzen7_3700X()
    gpu = Computer.NVIDIA_GeForce_GTX_1660_SUPER()
    computer.cpu = cpu
    computer.gpu2 = gpu
    
    computer.showInfo()