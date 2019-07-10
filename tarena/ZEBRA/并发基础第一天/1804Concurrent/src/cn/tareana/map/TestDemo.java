package cn.tareana.map;

import java.util.concurrent.ConcurrentHashMap;

import org.junit.Test;

/**
 * ѧϰ����Map�Ĵ�����ʹ�á�
 * HashMap �̲߳����ǰ�ȫ�������ܸ�
 * HashTable �̲߳�����ȫ�������ܵ�
 * @author ysq
 *
 */
public class TestDemo {
	
	/*
	 * ConcurrentHashMap������ֶ������ƣ��ײ����16��(segment)
	 * �����ϲ�������Ҫ��Hash��16����
	 * ÿ��Segment���Կ�����һ��HashTable����ĳ���̲߳���ĳ��k,vʱ��
	 * ֻ������k,v���ڵ�Segment��������������Segment��
	 * ���⣬ConcurrentHashMap�Ĵ�ȡ������HashMapһ�£�
	 * ���Ҹ������ӵĸ����HashMapһ�¡�
	 * ���⣬�ײ������ṹҲ��HashMapһ�¡�
	 * ע�⣺������������jdk1.8�汾֮ǰ��ConcurrentHashMap
	 * jdk1.8֮�󣬢��õ�CAS��compare and swap)�����㷨 �ڵײ�������滻�ɺ����
	 */
	@Test
	public void create(){
		ConcurrentHashMap<Integer, Integer> map=
				new ConcurrentHashMap<>();
		for(int i=0;i<1000;i++){
			map.put(i, i);
		}
		System.out.println();
	}
}
