import pandas as pd

def etl(a1,p1,p2,ti):
    e_rtn_obj = extract()
    t_rtn_obj =transform(a1, e_rtn_obj)
    l_rtn_obj = load(p1,p2,e_rtn_obj)
    return None 

def extract():
    print("What is your name")
    print("My name is", Name)
    #rtn_val = "I got this!"
    #return rtn_val

#creating a dataframe object
    details = {
        'cust_id': [1,2,3,4],
        'Name' : ['Rishu', 'Ishu', 'shanaya', 'Rudr']
    }
    df = pd.DataFrame(details)
    return df

def transform(a1,e_rtn_obj):
    #xcom_pull_obj = ti.xcom_pull(task_ids = ["Extract"])
    #print("type of xcom object is {}".format(type(xcom_pull_obj)))
    extract_rtn_obj = e_rtn_obj
    print("the value of e_rtn_obj obj is {extract_rtn_obj}")
    print("The value of ai is ", a1)
    print("Logic to transform data")
    #return 10

def load(p1,p2,e_rtn_obj):
    #xcom_pull_obj = ti.xcom_pull(task_ids = ["Extract"])
    #print("type of xcom object is {}".format(type(xcom_pull_obj)))
    #print("the value of xcom pull back obj is {}".format(xcom_pull_obj[0]))
    extract_rtn_obj = e_rtn_obj
    print("the type of e_rtn_obj is {}".format(type(extract_rtn_obj)))
    print("the value of e_rtn_obj is:")
    print(extract_rtn_obj)
    print("the value of p1 is {}".format(p1))
    print("the value of p2 is {}".format(p2))