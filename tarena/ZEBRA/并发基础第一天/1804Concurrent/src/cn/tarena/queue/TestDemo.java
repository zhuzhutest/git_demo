package cn.tarena.queue;

import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.PriorityBlockingQueue;
import java.util.concurrent.TimeUnit;

import org.junit.Test;

/**
 * ѧϰ�������е�ʹ�á����������ڸ߲����Լ��ܶ�����ݿ�ܵײ���Ӧ�á�
 * ���е�ʹ�ó����������ݴ�����У����������������á�����������
 * ���⣬������������þ���ʵ�������ߺ�������֮��Ľ��
 * 
 * @author ysq
 *
 */
public class TestDemo {
	
	/*
	 * add���������������������쳣��ʹ�����ַ�����������У�����ͨ�����������쳣������
	 * offer�������������������׳�false��δ����Ϊtrue��
	 * put�����������������������������������ʣ���������������ſ����˷�������
	 * offer��ʱ���������������������������
	 * �����ſ���������
	 * �ٶ�����ʣ��������
	 * �ڹ���ָ���ĳ�ʱʱ��
	 */
	@Test
	public void testPut() throws Exception{
		BlockingQueue queue=new ArrayBlockingQueue<>(10);
		for(int i=0;i<10;i++){
			queue.put(i);
		}
		//queue.add(11);
		//System.out.println(queue.offer(11));
		//queue.put(11);
		queue.offer(11,3,TimeUnit.SECONDS);
		System.out.println("hello 1804");
	}
	
	/*
	 * 1.remove�����Զ���Ϊ��ʱ�������쳣 NoSuchElement
	 * ������в�Ϊ�գ���FIFO��ԭ��ȡ����Ӧ������
	 * 2.poll����������Ϊ�գ�����nullֵ��һ������poll����ֵ�Ƿ�Ϊnull
	 * ���ж϶����Ƿ���ȡ�ꡣ
	 * 3.take���������(������Ϊ��)
	 * 4.poll��ʱ����������������ſ��������ٶ����������ݿ�ȡ�ڳ�ʱʱ�䵽��
	 */
	@Test
	public void testGet() throws Exception{
		BlockingQueue queue=new ArrayBlockingQueue<>(10);
		
		//queue.remove();
		//System.out.println(queue.poll());
		//queue.take();
		queue.poll(3, TimeUnit.SECONDS);
		System.out.println("hello 1804");
	}
	
	/*
	 * ArrayBlockingQueue:�����������е��ص㣺
	 * ���н���У������ڴ���ʱָ��
	 * �ڵײ���ͨ�����ݵ����ݽṹʵ�ֵġ����Բ�ѯ�죬��ɾ����
	 * LinkedBlockingQueue:���������е��ص㣺
	 * �����޽���У�Ĭ�ϵĴ�С��Integer.MaxValue
	 * �ڵײ��������ݽṹ����ɾ�졣��Ϊ���е�ʹ��һ��������ɾ�����Ա�Array����
	 * 
	 * ��������֮�����ܹ���֤������ȫ���ײ���ͨ����������ʵ�ֵģ���������
	 */
	public void createQueue(){
		BlockingQueue q1=new ArrayBlockingQueue<>(10);
		BlockingQueue q2=new LinkedBlockingQueue<>();
	}
	/*
	 * ���ȼ����У�Ҫ���������Ԫ�ر���ʵ��Comparable�ӿڡ�
	 * ���лᰴCompareTo()�еıȽϹ���ʵ��Ԫ�ص�����
	 * Ȼ��ȡ��Ԫ��ʱ���ǰ�������˳����ȡ��
	 */
	@Test
	public void createCompareQueue() throws Exception{
		BlockingQueue<Student> queue = 
				new PriorityBlockingQueue<Student>();
		Student s1=new Student("tom",100);
		Student s2=new Student("rose",150);
		Student s3=new Student("jim",80);
		
		queue.add(s1);
		queue.add(s2);
		queue.add(s3);
		
		for(int i=0;i<3;i++){
			System.out.println(queue.take());
		}
	}
}
