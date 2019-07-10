package cn.tarena.threadpool;

import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.RejectedExecutionHandler;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

import org.junit.Test;

public class TestDemo {

	@Test
	public void testCreate(){
		//--corePoolSize:�����߳�����
		//--���̳߳س��δ���ʱ����û���κ��̵߳ġ�����������ʱ���̻߳ᴴ�������߳�
		//--����������У����ۺ����߳��Ƿ����ã��̳߳ض��ᴴ�������̣߳�ֱ����������λ��
		
		//--maximumPoolSize:����߳���=�����߳���+��ʱ�߳���
		//--keepAliveTime����ʱ�̵߳Ĵ��ʱ��
		//--unit��ʱ�䵥λ��һ���ú��뵥λ
		//--workQueue:�ȴ����У����ڴ�Ż�δ���������
		ExecutorService service=
				new ThreadPoolExecutor(5, 
						10, 
						3000, 
						TimeUnit.MILLISECONDS, 
						new ArrayBlockingQueue<Runnable>(10),
						new RejectedExecutionHandler() {
							
							@Override
							public void rejectedExecution(Runnable r, ThreadPoolExecutor executor) {
								System.out.println("���Ժ���");
								
							}
						});
		
		//--ͨ���̳߳������߳�
		for(int i=0;i<21;i++){
			service.execute(new ClientRunner());
		}
		
		//--�ر��̳߳ء��˷�������ʱ���̳߳ز�������ⲿ�����ˡ�
		//--���ڲ����̲߳������������٣����ǵȵ��̹߳�����֮��������
		//--ʹ���̳߳صĺô����Ա����̵߳�Ƶ�����������٣���ʡcpu���ܡ�
		service.shutdown();
		
		
	}
	
	/*newCachedThreadPool:
	 *��û�к����߳�
	 *�ڶ�����ʱ�߳�
	 *�۶�����ͬ������
	 *������߳��� Integer.MaxValue
	 *�ܽ᣺�����С���еĺô���
	 *���Ժܺõ���Ӧ(��ʱ)�ͻ���������Ϊ����Ҫ�ȴ��Ŷӡ�
	 *����ע�⣺�����̳߳����ö�����������ǳ����󣬿��ܻᵼ���߳�һֱ�����������٣�����ڴ����
	 */
	public void testCreate_1(){
		ExecutorService service=Executors.newCachedThreadPool();
		
	}
	
	/*newFixedThreadPool:
	 *�ٶ��Ǻ����̣߳�û����ʱ�߳�
	 *�ڶ������޽����(LinkedBlockingQueue)
	 *�ܽ᣺С���Ӵ����
	 *�����̳߳ص����ã�������������������:���ܼ�ʱ��Ӧ�ͻ������� 
	 */
	public void testCreate_2(){
		ExecutorService service=Executors.newFixedThreadPool(10);
	}
	
}

class ClientRunner implements Runnable{

	@Override
	public void run() {
		System.out.println("����ͻ�������");
		try {
			Thread.sleep(Integer.MAX_VALUE);
		} catch (InterruptedException e) {
		
			e.printStackTrace();
		}
		
	}
	
}
