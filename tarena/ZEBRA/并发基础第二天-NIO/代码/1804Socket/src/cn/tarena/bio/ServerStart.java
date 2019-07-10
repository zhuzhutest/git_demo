package cn.tarena.bio;

import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class ServerStart {

	public static void main(String[] args) throws Exception {
		ServerSocket server=new ServerSocket(8888);
		
		while(true){
			Socket socket=server.accept();
			new Thread(new ClientRunner(socket)).start();
		}
	}
}
class ClientRunner implements Runnable{
	private Socket socket;
	
	public ClientRunner(Socket socket) {
		this.socket=socket;
	}

	@Override
	public void run() {
		try {
			InputStream in=socket.getInputStream();
			byte[] data=new byte[10];
			in.read(data);
			System.out.println("������յ�����:"+new String(data)+"�̱߳��:"+Thread.currentThread().getId());
			
		} catch (IOException e) {
			
			e.printStackTrace();
		}
		
	}
	
}
