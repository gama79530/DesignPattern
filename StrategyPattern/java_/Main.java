package StrategyPattern.java_;
import StrategyPattern.java_.Computer.Computer;
import StrategyPattern.java_.Computer.CPU.*;
import StrategyPattern.java_.Computer.GPU.*;

public class Main {
    public static void main(String[] args) {
        Computer computer = new Computer();
        CPU cpu = new AMD_Ryzen7_3700X();
        GPU gpu2 = new NVIDIA_GeForce_GTX_1660_SUPER();
        computer.setCpu(cpu);
        computer.setGpu2(gpu2);

        computer.showInfo();        
    }
}
