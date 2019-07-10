package cn.tarena.channel;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.channels.ServerSocketChannel;
import java.nio.channels.SocketChannel;

import org.junit.Test;

public class TestDemo {
	
	@Test
	public void server_create_accept() throws Exception{
		//--��ȡ�����ͨ��������Ҫ�������ǰ󶨷���ip�ͷ���˿�
		ServerSocketChannel server=ServerSocketChannel.open();
		server.bind(new InetSocketAddress(8888));
		//--��ɷ�����ģʽ��Ĭ��������ģʽ
		server.configureBlocking(false);
		
		//--��ȡ�Ͷ�Ӧ�ͻ���ͨ�ŵ�ͨ��
		SocketChannel sc=server.accept();
		System.out.println("hello");
	}
	@Test
	public void client_create_connect() throws Exception{
		//--��ȡ�ͻ���ͨ��
		SocketChannel sc=SocketChannel.open();
		sc.configureBlocking(false);
		sc.connect(new InetSocketAddress("127.0.0.1",8888));
		System.out.println("hello");
	}
}
