package cn.tarena.selector;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.nio.ByteBuffer;
import java.nio.channels.SelectionKey;
import java.nio.channels.Selector;
import java.nio.channels.SocketChannel;
import java.util.Iterator;
import java.util.Set;

public class ClientSelectorStart {
	
	public static void main(String[] args) throws Exception {
		SocketChannel sc=SocketChannel.open();
		sc.configureBlocking(false);
		sc.connect(new InetSocketAddress("127.0.0.1",8888));
		Selector selector=Selector.open();
		//--�ͻ���ע��ѡ�����������������¼�
		sc.register(selector, SelectionKey.OP_CONNECT);
		
		while(true){
			selector.select();
			Set<SelectionKey> set= selector.selectedKeys();
			Iterator<SelectionKey> it=set.iterator();
			
			while(it.hasNext()){
				SelectionKey sk= it.next();
				//--��ʾ�ͻ��˳ɹ����ӷ����
				if(sk.isConnectable()){
					SocketChannel client=(SocketChannel) sk.channel();
					client.register(selector,SelectionKey.OP_READ|SelectionKey.OP_WRITE);
					
				}
				//--����˷����ݹ��������ǿͻ��˶�����
				if(sk.isReadable()){
					SocketChannel client=(SocketChannel) sk.channel();
					ByteBuffer data=ByteBuffer.allocate(10);
					while(data.hasRemaining()){
						client.read(data);
					}
				}
				//--��ʾ���ǿͻ���Ҫ���������ݣ����ҷ������׼����
				if(sk.isWritable()){
					
				}
				it.remove();
			}
	
		}
	}

}
