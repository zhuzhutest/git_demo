package cn.tarena.buffer;

import java.nio.ByteBuffer;

import org.junit.Test;

/**
 * ֪ʶ�㣺
 * 1.��������NIOͨ��ʱ�����ݵ����塣
 * 2.�����У����õĻ�������ByteBuffer(�ֽڻ�����)
 * 3.�����������ԣ�capacity(����),�����˴洢���������ޡ�һ��д�������ܸ���
 * 4.�����������ԣ�limit(����),���Ƶĳ�ʼλ��=capacity
 * 5.�����������ԣ�position(λ��),��ʼλ����0
 * 6.ByteBufferĬ���õ����ࣺHeapByteBuffer(�����ֽڻ�����),��������
 * �Ļ���������JVM�Ķ��д����ģ����˻���������������(GC)��JVM�����
 * 7.MappedByteBuffer(�����ֽڻ�����),����ʹ�ò���ϵͳ���ڴ棬ʹ�ó���
 * ����������ֽڻ�����ʱ��ע�⣺���ʹ�ö��⣬�������ڵĹ�����Ҫ�Լ���ʵ��
 * 8.positionλ�ã�ÿ����һ���ֽڣ��ͻ�����ƶ�һλ
 * 9.get()��������ݵ�ǰposition��λ��ȡֵ,
 * ���⣬get()ÿ����һ�Σ�λ��Ҳ���ƶ�һλ
 * 
 * @author ysq
 *
 */
public class TestDemo {
	
	@Test
	public void create(){
		ByteBuffer buffer=ByteBuffer.allocate(10);
		System.out.println("");
	}
	
	@Test
	public void put(){
		ByteBuffer buffer=ByteBuffer.allocate(10);
		byte b1=1;
		byte b2=2;
		
		buffer.put(b1);
		buffer.put(b2);
		buffer.put("hello".getBytes());
		System.out.println("");
	}
	
	@Test
	public void get(){
		ByteBuffer buffer=ByteBuffer.allocate(10);
		byte b1=1;
		byte b2=2;
		byte b3=3;
		buffer.put(b1);
		buffer.put(b2);
		buffer.put(b3);
		
		//--��limit�õ���ǰ��position
		buffer.limit(buffer.position());
		
		//--��position�õ���ʼλ��
		buffer.position(0);
		System.out.println(buffer.get());
		System.out.println(buffer.get());
		System.out.println(buffer.get());
		System.out.println(buffer.get());
		
	}
	@Test
	public void flip(){
		ByteBuffer buffer=ByteBuffer.allocate(10);
		byte b1=1;
		byte b2=2;
		byte b3=3;
		buffer.put(b1);
		buffer.put(b2);
		buffer.put(b3);
		//--flip ��ת���������л����������Ķ�ģʽ
		//--�ȼ���buffer.limit(buffer.position())+buffer.position(0);
		buffer.flip();
		System.out.println(buffer.get());
		System.out.println(buffer.get());
		System.out.println(buffer.get());
		System.out.println(buffer.get());
	}
	
	@Test
	public void wrap(){
		//--����ݴ�����ֽ������С������Ӧ�Ĵ�С����������д������
		//--���⣬д�����ݺ��Զ�����flip()
		ByteBuffer buffer=ByteBuffer.wrap("helloworld".getBytes());
		System.out.println("");
	}
	@Test
	public void clear(){
		ByteBuffer buffer=ByteBuffer.allocate(10);
		byte b1=1;
		byte b2=2;
		byte b3=3;
		buffer.put(b1);
		buffer.put(b2);
		buffer.put(b3);
		//--clear��������������������������ݣ�ֻ�ǽ�position��Ϊ0
		buffer.clear();
		byte b4=4;
		byte b5=5;
		//--clear֮����д���ݣ�Ϊ�˱��������ʷ���ݣ�һ�������˵���flip
		buffer.put(b4);
		buffer.put(b5);
		buffer.flip();
		
	}
	
	@Test
	public void hasRemaining(){
		ByteBuffer buffer=ByteBuffer.wrap("helloworld".getBytes());
		
		//--hasRemaining()�������ж� limit��position֮���Ƿ���Ԫ�ؿɶ�
		//--����оͷ���true,���û�У��ͷ���false,����ѭ��
		while(buffer.hasRemaining()){
			System.out.println(buffer.get());
		}
	}
}
