package cn.tarena.atomic;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * ԭ�������͵ײ��õ����CAS�㷨(�����㷨),�����Ա�֤�̲߳�����ȫ���⣬�������ܸܺ�
 * @author ysq
 *
 */
public class TestDemo {
	
	//--ԭ��������
	public static AtomicInteger i=new AtomicInteger(0);
	
	public static void main(String[] args) throws Exception {
		CountDownLatch cdl=new CountDownLatch(2);
		
		new Thread(new AddRunner1(cdl)).start();
		new Thread(new AddRunner2(cdl)).start();
		
		cdl.await();
		System.out.println(i);
	}
}

class AddRunner1 implements Runnable{
	private CountDownLatch cdl;

	public AddRunner1(CountDownLatch cdl) {
		this.cdl=cdl;
	}

	@Override
	public void run() {
		for(int j=0;j<100000;j++){
			TestDemo.i.incrementAndGet();
		}
		cdl.countDown();
		
	}
	
}
class AddRunner2 implements Runnable{
	private CountDownLatch cdl;

	public AddRunner2(CountDownLatch cdl) {
		this.cdl=cdl;
	}

	@Override
	public void run() {
		for(int j=0;j<100000;j++){
			TestDemo.i.incrementAndGet();
		}
		cdl.countDown();
	}
	
}
