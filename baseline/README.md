## JD Dialog Challenge


## ���ڸû���
#�û�����JD.com����JD Dialog Challenge�����������ѡ�����ṩ�Ŀ�Դ���ߴ��룬�õ���ģ��Ϊ��Seq2Seq���û��߽����ο���
#working_dir: (1).ѵ��֮���ģ�ͱ����ļ�  (2).�ʵ��ļ�
#data: (1).ԭѵ������, path��data/chat.txt  (2).������ϴ֮���ѵ�����ϣ�train.enc��train.dec��test.enc��test.dec (3).����ģ�����ݣ���������test.txt��������result.txt��path��data/test/
#seq2seq.ini: ���������ļ�
#dataProcessing.py: ������ϴ�ļ�
#���ߴ����ļ���data_utils.py��seq2seq_model.py��execute.py


## ��������
#�����ߴ��뵱ǰѵ�����Ϲ���1���seesion�Ự�����ݣ�path��data/chat.txt�������������ھ�����˾�ͷ��Ϳͻ�����ʵ���������������������������ݡ�
#train.enc��train.dec��test.enc��test.dec��Ϊģ�͵�ѵ�����ϣ����ǻ����ļ�chat.txt����������ϴ��enc�ļ�ÿ��������ͬһ�Ự�е�QAQAQ��dec�ļ�ÿ��������ͬһ�Ự�е�A��Q��ʾ�û��ش�A��ʾ�ͷ�/�����˻ش𣬾���ʵ�ֿɲο����ݴ����ļ�dataProcessing.py


## requirement
# python3.5
# tensorflow1.0.0


## Train Model
# edit seq2seq.ini file to set mode = train
python execute.py


## Test
# edit seq2seq.ini file to set mode = test
#���룺�����ļ���ʽ(QAQAQ)��path(working_dir/test/test.txt)��ע����ʽ������ʼʱ����100�����⣬�û����ļ�ֻ������50������
#���������ļ���ʽ(A)��path(working_dir/test/result.txt)
python execute.py


## Notes
#�����ߺ��������������

