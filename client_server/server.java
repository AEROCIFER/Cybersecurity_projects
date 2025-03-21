import java.io.*;
import java.net.*;

public class server {

    public static void main(String q[]) throws IOException{
        System.out.println("Starting Server...");
        ServerSocket ss = new ServerSocket(8000);

        System.out.println("Server listening on port 8888...");

        Socket cs = ss.accept();
        System.out.println("Connection Established ...");

        DataInputStream data = new DataInputStream(cs.getInputStream());
        String msg = data.readUTF();
        System.out.println(msg);
        DataOutputStream out = new DataOutputStream(cs.getOutputStream());
        out.writeUTF("Hello...");

    }
}