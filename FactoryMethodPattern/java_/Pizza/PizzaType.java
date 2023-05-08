package FactoryMethodPattern.java_.Pizza;

public enum PizzaType {
    CHEESE_PIZZA("cheese flavor pizza"), 
    PEPPERONI_PIZZA("pepperoni flavor pizza"), 
    VEGGIE_PIZZA("veggie flavor pizza");

    private String info;
    private PizzaType(String info){
        this.info = info;
    }

    public String getInfo(){
        return info;
    }
}
