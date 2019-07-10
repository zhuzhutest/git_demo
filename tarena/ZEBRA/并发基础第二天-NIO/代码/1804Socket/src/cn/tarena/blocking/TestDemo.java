package cn.tarena.blocking;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;

import org.junit.Test;

public class TestDemo {
	
	/*
	 * Listens for a connection to be made to this socket and accepts
     * it. The method blocks until a connection is made.
     * accept�˷��������������ֱ����һ���ͻ��˽��룬�����ſ�
     * 
     * this method
     * blocks until input data is available, 
     * the end of the stream is detected
     * read()����Ҳ����������������ſ��������������ݿɶ�
     * 
     * write()����Ҳ�������������һ��д������һ��������д����һ����ʱ���ͻ��������
	 */
	@Test
	public void testAccept_Read_Write() throws IOException{
		ServerSocket server=new ServerSocket(8888);
		Socket socket=server.accept();
		
		InputStream in=socket.getInputStream();
		//--����˺Ϳͻ�������֮�󣬶����ݣ����ǿͻ��˲���������
//		in.read();
//		System.out.println("hello");
		OutputStream out=socket.getOutputStream();
		for(int i=0;i<100000;i++){
			out.write("helloworld".getBytes());
			System.out.println(i);
		}
	}
	/*
	 * The connection
     * will then block until established or an error occurs
     * connectҲ����������������ſ��������������������ӻ����쳣�׳�
	 */
	@Test
	public void testConnect() throws Exception{
		Socket socket=new Socket();
		socket.connect(new InetSocketAddress("127.0.0.1",8888));
		while(true);//���ֿͻ�������һֱ����
		
	}
}
