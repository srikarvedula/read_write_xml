import xml.etree.ElementTree as ET
import csv

with open('exams.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    header = next(csv_reader)
    # Check file as empty
    if header != None:
        # Iterate over each row after the header in the csv
        gender=[]
        race=[]
        education=[]
        lunch=[]
        test_prep=[]
        math_score=[]
        reading_score=[]
        writing_score=[]
        for row in csv_reader:
            a=row[0]
            b=row[1]
            c=row[2]
            d=row[3]
            e=row[4]
            f=int(row[5])
            g=int(row[6])
            h=int(row[7])
            gender.append(a)
            race.append(b)
            education.append(c)
            lunch.append(d)
            test_prep.append(e)
            math_score.append(f)
            reading_score.append(g)
            writing_score.append(h)

results = ET.Element("results")
key_id=list(range(1,101))
for a in range(len(gender)):
    result = ET.SubElement(results,"key_id")
    genders = ET.SubElement(result, "gender")
    races = ET.SubElement(result, "race")
    educations= ET.SubElement(result, "education")
    lunches= ET.SubElement(result, "lunch")
    test_preps = ET.SubElement(result, "test_prep")
    math_scores = ET.SubElement(result, "math_score")
    reading_scores = ET.SubElement(result, "reading_score")
    writing_scores = ET.SubElement(result, "writing_score")

    result.text=str(key_id[a])
    genders.text = gender[a]
    races.text = race[a]
    educations.text=education[a]
    lunches.text=lunch[a]
    test_preps.text = test_prep[a]
    math_scores.text = str(math_score[a])
    reading_scores.text = str(reading_score[a])
    writing_scores.text = str(writing_score[a])

mydata = ET.tostring(results, encoding='unicode')
myfile = open("exams.xml", "w")
myfile.write(mydata)