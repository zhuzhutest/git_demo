package cn.tarena.filechannel;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;

import org.junit.Test;

public class TestDemo {
	
	@Test
	public void write() throws Exception{
		//--��ȡ�ļ�ͨ��������ĳ�����������ļ��������������������)
		FileChannel fc=
			new FileOutputStream(new File("1.txt")).getChannel();
		
		ByteBuffer buffer=ByteBuffer.wrap("helloworld".getBytes());
		fc.write(buffer);
		
		fc.close();
	}
	@Test
	public void read() throws Exception{
		FileChannel fc=new FileInputStream(new File("1.txt")).getChannel();
		ByteBuffer buffer=ByteBuffer.allocate(10);
		//--�ļ�ͨ������ͨ��λ�����Ĳ�������
		//--�ļ�ͨ���ײ����ʹ��zero copy �㿽������
		fc.position(4);
		fc.read(buffer);
		System.out.println(new String(buffer.array()));
		fc.close();
	}
}
