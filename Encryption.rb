require 'openssl'  
require 'base64' 

class AesEncryptDecrypt
	def self.encryption(key, msg, algorithm)  
    begin  
      cipher = OpenSSL::Cipher.new(algorithm)  
      cipher.encrypt()  
      cipher.key = key  
      crypt = cipher.update(msg) + cipher.final()  
      crypt_string = (Base64.encode64(crypt))  
      return crypt_string  
    rescue Exception => exc  
      puts ("Message for the encryption log file for message #{msg} = #{exc.message}")  
    end  
  end  
    
  def self.decryption(key, msg, algorithm)  
    begin  
      cipher = OpenSSL::Cipher.new(algorithm)  
      cipher.decrypt()  
      cipher.key = key  
      tempkey = Base64.decode64(msg)  
      crypt = cipher.update(tempkey)  
      crypt << cipher.final()  
      return crypt  
    rescue Exception => exc  
      puts ("Message for the decryption log file for message #{msg} = #{exc.message}")  
    end  
  end  
end  