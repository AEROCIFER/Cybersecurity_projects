import java.io.*;
import java.net.*;
import java.util.Scanner;

public class client {
    public static void main(String[] args) throws IOException {
        // Socket cl = new Socket("172.16.10.209", 8000);
        Scanner ip_addr = new Scanner(System.in);
        System.out.println("Enter the ip address: ");
        String name = ip_addr.nextLine();
        Socket cl = new Socket(name, 5000);
        DataOutputStream out = new DataOutputStream(cl.getOutputStream());
        out.writeUTF("Hello...");
        DataInputStream data = new DataInputStream(cl.getInputStream());
        String msg = data.readUTF();
        System.out.println(msg);
    }
}
