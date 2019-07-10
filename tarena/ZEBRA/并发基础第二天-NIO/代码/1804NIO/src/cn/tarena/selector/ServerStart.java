package cn.tarena.selector;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.nio.ByteBuffer;
import java.nio.channels.SelectionKey;
import java.nio.channels.Selector;
import java.nio.channels.ServerSocketChannel;
import java.nio.channels.SocketChannel;
import java.util.Iterator;
import java.util.Set;

public class ServerStart {

	public static void main(String[] args) throws Exception {
		ServerSocketChannel ssc=ServerSocketChannel.open();
		ssc.configureBlocking(false);
		ssc.bind(new InetSocketAddress(8888));
		//--��ȡ��·����ѡ����
		Selector selector=Selector.open();
		//--�ڷ����ͨ���ϰ󶨼������������������¼�
		ssc.register(selector,SelectionKey.OP_ACCEPT);
		while(true){
			//--�˷�����һ�����������������ſ������������¼�����
			selector.select();
			//--��������ߵ��⣬˵�������ſ���˵�����¼�����������Ҫ�����¼�
			Set<SelectionKey> set=selector.selectedKeys();
			//--��ȡ����(�¼�����)�ĵ�����
			Iterator<SelectionKey> it=set.iterator();
			
			while(it.hasNext()){
				//--��ȡһ���¼�
				SelectionKey sk= it.next();
				//--��ʾ�пͻ��˽����¼�
				if(sk.isAcceptable()){
					ServerSocketChannel server=
							(ServerSocketChannel) sk.channel();
					//--�����Ͷ�Ӧ�ͻ���ͨ�ŵ�ͨ��
					SocketChannel sc=server.accept();
					//--���÷�����ģʽ
					sc.configureBlocking(false);
					//-- OP_READ  0000 0001
					//-- OP_WRITE 0000 0100
					//            0000 0101
					System.out.println("����ͻ���,�����̺߳�:"+Thread.currentThread().getId());
					sc.register(selector,SelectionKey.OP_READ|SelectionKey.OP_WRITE);
					
				}
				//--��ʾ�ͻ��������ݷ�������ˣ����Ƿ����Ҫ������
				if(sk.isReadable()){
					SocketChannel sc=(SocketChannel) sk.channel();
					
					ByteBuffer buffer=ByteBuffer.allocate(10);
					sc.read(buffer);
					System.out.println("�յ��ͻ�������:"+new String(buffer.array())+"�̱߳��:"+Thread.currentThread().getId());
					
				}
				//--��ʾ�ͻ���׼���ý������ݣ����Ƿ���Ҫд������
				if(sk.isWritable()){
					SocketChannel sc=(SocketChannel) sk.channel();
					ByteBuffer buffer=ByteBuffer.wrap("1234".getBytes());
					//--��Ϊwrite��read�Ƿ���������
					//--����Ϊ��ȷ������д������������Ҫ����hasRemaining()
					while(buffer.hasRemaining()){
						sc.write(buffer);
					}
					
				}
				//--�¼���������Ƴ����¼��������ظ�����
				it.remove();
			}
			
		}
	}
}
