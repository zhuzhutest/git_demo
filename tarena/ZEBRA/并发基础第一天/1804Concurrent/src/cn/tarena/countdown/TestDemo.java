package cn.tarena.countdown;

import java.util.concurrent.CountDownLatch;

/**
 * ����Ҳ���̵߳ݼ���������ͨ���������̹߳�������ִ�С�
 * ��Ҫ��ͨ��CountDown()��await()��ʵ�֡�
 * @author ysq
 *
 */
public class TestDemo {
	
	public static void main(String[] args) throws Exception {
		
		CountDownLatch cdl=new CountDownLatch(2);
		
		new Thread(new BuyGuo(cdl)).start();
		new Thread(new BuyCai(cdl)).start();
		
		//--�˷�������������������ſ��������Ǳ�����ʼ����=0
		cdl.await();
		System.out.println("��ʼ����");
	}

}

class BuyGuo implements Runnable{
	private CountDownLatch cdl;

	public BuyGuo(CountDownLatch cdl) {
		this.cdl=cdl;
	}

	@Override
	public void run() {
		System.out.println("���������");
		//--�˷���ÿ����һ�Σ������ĳ�ʼ����-1
		
			try {
				Thread.sleep(5000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		
		cdl.countDown();
		
	}
	
}
class BuyCai implements Runnable{
	
	private CountDownLatch cdl;

	public BuyCai(CountDownLatch cdl) {
		this.cdl=cdl;
	}

	@Override
	public void run() {
		System.out.println("���������");
		cdl.countDown();
		
	}
	
}
