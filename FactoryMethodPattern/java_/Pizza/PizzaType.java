package FactoryMethodPattern.java_.Pizza;

public enum PizzaType {
    CheesePizza("cheese flavor pizza"), 
    PepperoniPizza("pepperoni flavor pizza"), 
    VeggiePizza("veggie flavor pizza");

    private String info;
    private PizzaType(String info){
        this.info = info;
    }

    public String getInfo(){
        return info;
    }
}
