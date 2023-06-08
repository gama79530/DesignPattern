package ProxyPattern.java_.Server;

import java.rmi.*;
import java.rmi.registry.*;
import java.util.*;

public class Service {
    private String host;
    private int port;
    private Registry registry;

    public Service(String host, int port) throws RemoteException {
        this.host = host;
        this.port = port;
        registry = LocateRegistry.createRegistry(port);
    }

    public String getHost(){
        return this.host;
    }

    public int getPort() {
        return this.port;
    }

    public void bind(String name, Remote skeleton) throws Exception{
        String rmiReference = String.format("rmi://%s:%d/%s", host, port, name);
        try{
            registry.lookup(name);
            registry.rebind(rmiReference, skeleton);
        }catch(NotBoundException e){
            registry.bind(name, skeleton);
        }
    }

    @Override
    public String toString() {
        try {
            return "Registry List: " + Arrays.toString(registry.list());
        } catch (Exception e) {
            return e.toString();
        }
    }
    
    public static void main(String[] args) throws Exception{
        Account account = new Account();
        Skeletons skeleton = new Skeletons(account);

        String host = "127.0.0.1";
        int port = 1099;
        Service service = new Service(host, port);
        
        String name = "accountProxy";
        service.bind(name, skeleton);
        
        System.out.println("Service Start");
        System.out.println("======================================================");           
    }
}
