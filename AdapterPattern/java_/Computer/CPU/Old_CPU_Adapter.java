package AdapterPattern.java_.Computer.CPU;

import AdapterPattern.java_.Computer.CPU.OldCPU.Old_CPU;

public class Old_CPU_Adapter implements CPU{
    private Old_CPU old_CPU;

    public Old_CPU_Adapter(Old_CPU old_CPU) {
        this.old_CPU = old_CPU;
    }

    @Override
    public String showInfo() {
        return old_CPU.getName();
    }
    
}
