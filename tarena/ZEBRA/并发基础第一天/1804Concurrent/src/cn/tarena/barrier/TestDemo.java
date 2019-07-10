package cn.tarena.barrier;

import java.util.concurrent.BrokenBarrierException;
import java.util.concurrent.CyclicBarrier;

/**
 * ������
 * ����ƥ���������̣߳�
 * Ҫ�����ȵ����е���������դ��ǰ������һ����
 * 
 * դ�����ƿ���ʵ���̵߳�ͬ��Э����ʵ�ֵķ�ʽ����ͨ��await()������ʵ��
 */
public class TestDemo {
	public static void main(String[] args) {
		//--����դ����������һ����ʼ�ļ�����
		CyclicBarrier barrier = new CyclicBarrier(2);
		new Thread(new Horse1(barrier)).start();
		new Thread(new Horse2(barrier)).start();
	}

}

class Horse1 implements Runnable{
	
	private CyclicBarrier barrier;

	public Horse1(CyclicBarrier barrier) {
		this.barrier=barrier;
	}

	@Override
	public void run() {
		System.out.println("����1����դ��ǰ");
		
		try {
			//--�˷������������,�����ſ���������դ���ĳ�ʼ������=0
			//--���⣬�˷���ÿ����һ�Σ���������-1
			barrier.await();
		} catch (Exception e) {
			
			e.printStackTrace();
		}
		System.err.println("����1��ʼ��");
		
	}
	
}

class Horse2 implements Runnable{

	private CyclicBarrier barrier;
	public Horse2(CyclicBarrier barrier) {
		this.barrier=barrier;
	}

	@Override
	public void run() {
		System.out.println("����2����������");
		
		try {
			Thread.sleep(5000);
		System.out.println("����2����դ��ǰ");
		
		barrier.await();
		
		System.out.println("����2��ʼ��");
			
		} catch (Exception e) {
			
			e.printStackTrace();
		}
		
	}
	
}
