package cn.tarena.exchanger;

import java.util.concurrent.Exchanger;

/**
 * ��������������԰���
 * ���1�İ��ţ�����һЦ
 * ���2�İ��ţ���ݲ���
 * 
 * ��������ʹ�ó����������߳������ݽ����ĳ�����ע���������̡߳�
 * @author ysq
 *
 */
public class TestDemo {
	
	public static void main(String[] args) {
		//--����������
		Exchanger<String> ex=new Exchanger<>();
		
		new Thread(new Spy1(ex)).start();
		new Thread(new Spy2(ex)).start();
	}

}

class Spy1 implements Runnable{
	
	private Exchanger<String> ex;

	public Spy1(Exchanger<String> ex) {
		this.ex=ex;
	}

	@Override
	public void run() {
		String info="����һЦ";
		try {
			//--�����ݴ����Է��߳�
			//--�˷����ķ���ֵ�ǶԷ��̴߳�����ֵ
			String spy2Info=ex.exchange(info);
			System.out.println("1�յ�2�İ���:"+spy2Info);
			
		} catch (Exception e) {
			
			e.printStackTrace();
		}
		
	}
	
}

class Spy2 implements Runnable{
	private Exchanger<String> ex;
	
	public Spy2(Exchanger<String> ex) {
		this.ex=ex;
	}

	@Override
	public void run() {
		String info="��ݲ���";
		try {
			String Spy1Info=ex.exchange(info);
			System.out.println("2�յ�1������:"+Spy1Info);
			
		} catch (Exception e) {
		
			e.printStackTrace();
		}
		
	}
	
}
