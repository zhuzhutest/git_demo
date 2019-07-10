package cn.tarena.selector;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.SocketChannel;

public class ClientStart {
	
	public static void main(String[] args) throws Exception {
		SocketChannel sc=SocketChannel.open();
		sc.configureBlocking(false);
		sc.connect(new InetSocketAddress("127.0.0.1",8888));
		
		//--����������Ϊ�˱�����������Ӵ����Ŀ�ָ���쳣������
		while(!sc.isConnected()){
			sc.finishConnect();
		}
		
		ByteBuffer buffer=ByteBuffer.wrap("helloworld".getBytes());
		sc.write(buffer);
		
		ByteBuffer data=ByteBuffer.allocate(4);
		
		while(data.hasRemaining()){
			sc.read(data);
		}
	
		System.out.println("�ͻ����յ�����:"+new String(data.array()));
		
		System.out.println("success");
		while(true);//���ֿͻ����߳�һֱ����
		
	}

}
