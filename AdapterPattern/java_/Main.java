package AdapterPattern.java_;
import AdapterPattern.java_.Computer.Computer;
import AdapterPattern.java_.Computer.CPU.*;
import AdapterPattern.java_.Computer.CPU.OldCPU.Pentium4;
import AdapterPattern.java_.Computer.GPU.*;

public class Main {
    public static void main(String[] args) {
        Computer computer = new Computer();
        CPU cpu = new Old_CPU_Adapter(new Pentium4());
        GPU gpu = new NVIDIA_GeForce_GTX_1660_SUPER();
        computer.setCpu(cpu);
        computer.setGpu2(gpu);

        computer.showInfo();        
    }
}
