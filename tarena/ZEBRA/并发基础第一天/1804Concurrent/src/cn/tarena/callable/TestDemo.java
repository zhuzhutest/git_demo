package cn.tarena.callable;
/**
 * Callable��jdk1.5֮���ṩ�µ��̻߳��ƣ���Runnable�ı仯��
 * �٣�call()�ķ���ֵ���Ϳ����Զ���
 * �ڣ�call()�ķ���ֵ���Խӵ�
 * �ۣ�call()�������쳣
 * �ܣ�Callable�߳���ֻ��ͨ���̳߳�����������ͨ�� new Thread().start()����
 */
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class TestDemo {

	public static void main(String[] args) throws Exception {
		ExecutorService service=Executors.newCachedThreadPool();
		Future<String> future=service.submit(new C1());
		//--��ȡ��Ӧ�߳�call()�ķ���ֵ
		String result=future.get();
		System.out.println(result);
		service.shutdown();
	}
}

class C1 implements Callable<String>{

	@Override
	public String call() throws Exception {
		System.out.println("�߳�����");
		return "success";
	}
	
}
