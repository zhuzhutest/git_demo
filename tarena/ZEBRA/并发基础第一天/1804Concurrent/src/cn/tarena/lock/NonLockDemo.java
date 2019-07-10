package cn.tarena.lock;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class NonLockDemo {
	
	public static String name="����";
	public static String gender="��";
	
	public static void main(String[] args) {
		//--����������
		//--�ײ�֧�����������ƣ��ٹ�ƽ������ �ڷǹ�ƽ������
		//--���������fasle �Ƿǹ�ƽ�����ԣ�Ĭ���Ǵ˻���
		//--true�ǹ�ƽ������
		//--ͬ�������Ĭ�Ͼ�һ�ַǹ�ƽ��
		//--ע�⣺ʹ����������һ��Ҫע�����ͷŵ����⡣
		//--��Ҫ��finally{lock.unlock},�����������
		//--�ٷ����飬���ʹ�÷ǹ�ƽ����ʹ��ͬ�������
		Lock lock=new ReentrantLock(false);
		new Thread(new WriteRunner(lock)).start();
		new Thread(new ReadRunner(lock)).start();
	}

}

class WriteRunner implements Runnable{
	private Lock lock;

	public WriteRunner(Lock lock) {
		this.lock=lock;
	}

	@Override
	public void run() {
		while(true){
//			synchronized(NonLockDemo.class){
//				if(NonLockDemo.name=="����"){
//					NonLockDemo.name="��÷÷";
//					NonLockDemo.gender="Ů";
//				}else{
//					NonLockDemo.name="����";
//					NonLockDemo.gender="��";
//				}	
//			}
			//--����
			lock.lock();
			if(NonLockDemo.name=="����"){
				NonLockDemo.name="��÷÷";
				NonLockDemo.gender="Ů";
			}else{
				NonLockDemo.name="����";
				NonLockDemo.gender="��";
			}	
			//--�ͷ���
			lock.unlock();
			
		}
		
	}
	
}
class ReadRunner implements Runnable{
	private Lock lock;
	public ReadRunner(Lock lock) {
		this.lock=lock;
	}

	@Override
	public void run() {
		while(true){
//			synchronized(NonLockDemo.class){
//				System.out.println(NonLockDemo.name+":"+NonLockDemo.gender);	
//			}
			lock.lock();
			System.out.println(NonLockDemo.name+":"+NonLockDemo.gender);	
			lock.unlock();
		}
		
	}
	
}
