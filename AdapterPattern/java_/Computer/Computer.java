package AdapterPattern.java_.Computer;
import AdapterPattern.java_.Computer.CPU.*;
import AdapterPattern.java_.Computer.GPU.*;

public class Computer {
    private CPU cpu;
    private GPU gpu1;
    private GPU gpu2;

    public Computer() {
        this.cpu = null;
        this.gpu1 = null;
        this.gpu2 = null;
    }

    public CPU getCpu() {
        return this.cpu;
    }

    public void setCpu(CPU cpu) {
        this.cpu = cpu;
    }

    public GPU getGpu1() {
        return this.gpu1;
    }

    public void setGpu1(GPU gpu) {
        gpu1 = gpu;
    }

    public GPU getGpu2() {
        return this.gpu2;
    }

    public void setGpu2(GPU gpu) {
        gpu2 = gpu;
    }

    public void showInfo(){
        System.out.println("The component of this computer");
        System.out.println(String.format("CPU   : %s", cpu.showInfo()));
        System.out.println(String.format("GPU 1 : %s", gpu1 == null ? "None" : gpu1.showInfo()));
        System.out.println(String.format("GPU 2 : %s", gpu2 == null ? "None" : gpu2.showInfo()));
    }
}
