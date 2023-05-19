import Computer
import Old_CPU

if __name__ == '__main__':
    computer = Computer.Computer()
    cpu = Computer.Old_CPU_Adapter(Old_CPU.Pentium4())
    gpu = Computer.NVIDIA_GeForce_GTX_1660_SUPER()
    computer.cpu = cpu
    computer.gpu2 = gpu
    
    computer.showInfo()