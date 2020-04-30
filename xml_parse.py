from create_xml import *
from xml.dom import minidom
import pymysql as sql
import configparser

config = configparser.ConfigParser()
config.read('db.ini')
host = config['mysql']['host']
user = config['mysql']['user']
passwd = config['mysql']['passwd']
db = config['mysql']['db']
conn=sql.connect(host=host,port=3306,user=user,password=passwd, db=db)
cursor=conn.cursor()

xmldoc = minidom.parse('exams.xml')
result_elements = xmldoc.getElementsByTagName("results")


gender_list=[]
race_list=[]
education_list=[]
lunch_list=[]
test_prep_list=[]
math_score_list=[]
reading_score_list=[]
writing_score_list=[]
for re in result_elements:
    key_elements = re.getElementsByTagName("key_id")
    for k in key_elements:
        gender_element = k.getElementsByTagName("gender")
        for gen in gender_element:
            a=gen.childNodes[0].nodeValue
            gender_list.append(a)
        race_element=k.getElementsByTagName("race")
        for rac in race_element:
            b=rac.childNodes[0].nodeValue
            race_list.append(b)
        edu_element = k.getElementsByTagName("education")
        for edu in edu_element:
            c = edu.childNodes[0].nodeValue
            education_list.append(c)
        lunch_element = k.getElementsByTagName("lunch")
        for lun in lunch_element:
            d = lun.childNodes[0].nodeValue
            lunch_list.append(d)
        test_prep_element = k.getElementsByTagName("test_prep")
        for tes in test_prep_element:
            e = tes.childNodes[0].nodeValue
            test_prep_list.append(e)
        math_score_element = k.getElementsByTagName("math_score")
        for mat in math_score_element:
            f = mat.childNodes[0].nodeValue
            int_f=int(f)
            math_score_list.append(int_f)
        reading_score_element = k.getElementsByTagName("reading_score")
        for read in reading_score_element:
            g = read.childNodes[0].nodeValue
            int_g = int(g)
            reading_score_list.append(int_g)
        writing_score_element = k.getElementsByTagName("writing_score")
        for write in writing_score_element:
            h = write.childNodes[0].nodeValue
            int_h = int(h)
            writing_score_list.append(int_h)


query = "INSERT INTO exam_table(key_id, gender, race, education, lunch, test_prep, math_score, reading_score, writing_score) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
sqltuples = [(ke,ge,r,ed,lu,te,ma,rea,wri) for ke,ge,r,ed,lu,te,ma,rea,wri in zip(key_id,gender_list,race_list,education_list,lunch_list,test_prep_list,math_score_list,reading_score_list,writing_score_list)]
cursor.executemany(query,sqltuples)
conn.commit()
cursor.close()
print("XML data added to MySQL database successfully!")