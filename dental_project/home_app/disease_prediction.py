from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd

l1=['toothache','sensitivity','pain_while_eating_or_drinking_sweet','pain_while_eating_or_drinking_hot','pain_while_eating_or_drinking_cold','holes','pits','brown_stain','black_stain','yellow_stain','pain_while_bite','vomiting','bleeding_while_brushing','bleeding','dry_mouth','tooth_decay','gum_ache','gum_rashes','earaches','throat_pain','headaches','bad_breath','red_gums','swallon_gums','unpleasant_taste','black_spot','brown_spot','losing_tooth','cracks_on_teeth','dehydration','indigestion','mouth_sore','jaw_pain','popping_jaw','oral_piercing','infection','cracked_teeth','broken_teeth','stain','loose_teeth','swollen_cheeks','clicking_jaw','mild_fever','missing_teeth','lumps_on_gum','red_tongue','yellow_saliva','puss','spontaneous_pain','mild_to_sharp_pain','visible_holes','pain_when_you_bite_down','molar_decay','premolar_decay','grooves','crannies','positioning_shifts','tooth_abscess','sore_gum','yellow_spot','dark_spot','grey_saliva','milky_saliva','pimple_on_tongue','reddish_tongue','fluid_from_ear','fluid_from_gum','reddish_gum','grubby_teeth','history_of_alcohol_consumption','history_of_smoking','having_bevarages_daily','having_more_caffeinated_beverages','itching','mouthskin_rash','ulcers_on_tongue','patches_in_throat','throat_pain','mood_swings','anxiety','cough','high_fever','headache','mild_fever','throat_irritation','fluid_overload','neck_pain','puffy_face','enlarged_thyroid','family_history','dark_purple_gums','gums_feeling_tender','toothbrush_that_looks_pink_after_brushing','spitting_out_blood_when_brushing','spitting_out_blood_when_flossing','pus_between_teeth_and_gum','painful_chewing','space_between_teeth_look_like_black_traingles','gums_that_pull_away_from_teeth','unfitted_teeth_when_bitting','enlarged_tongue','trouble_moving_tongue','loss_of_taste','spitting_out_blood_when_brushing','burning_sensation','texture_of_mouth_changes','black_hairy_tongue','itching','no_saliva','stain_under_teeth','bited_rough_food','change_in_drinking_water','using_chlorinated_water','consuming_lots_of_sugary_food','consuming_lots_of_starchy_food','shiny_gums','sensitivity_to_cold','sensitivity_to_hot','unpleasant_taste_in_mouth','puffy_gums','bad_odor','sleepnessness','swelled_face','bitter_taste','swollen_lymph_nodes','migraines','erupting_teeth','food_lodged_in_teeth','swollen_lymph_nodes_unde_ your_jaw','salty_fluid_in_mouth','eating_snacks_daily','cheek_swelling']

disease=['Fungal infection','Allergy','Tooth decay','Gum disease','Drug Reaction','Bad breath','Sensitive teeth','Oral cancer ','Root infection','Enamel erosion','Dry mouth','Teeth grinding','Cavity','Bacteria','Gingivitis','Oral candidiasis','Periodontitis','Probiotic','Palate','Tooth Crowding','Halitosis','Noma','Oro dental trauma','Cleft lip','Abscess','Edentulism','Impacted tooth','Misalinged teeth','Denture Stomatisis','Geographic tongue','HPV','Lichen planus','Thrush','Diabetes','Anodontia','Talon cusps','Tooth gemination','Acne','Hyperdontia','Ectodermal Dysplasia','Taurodontism'
]

l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# TESTING DATA
tr=pd.read_csv("home_app/Testing_dental.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'Tooth decay':2,'Gum disease':3,'Drug Reaction':4,'Bad breath':5,'Sensitive teeth':6,'Oral cancer':7,'Root infection':8,'Enamel erosion':9,'Dry mouth':10,'Teeth grinding':11,'Cavity':12,'Bacteria':13,'Gingivitis':14,'Oral candidiasis':15,'Periodontitis':16,'Probiotic':17,'Palate':18,'Tooth Crowding':19,'Halitosis':20,'Noma':21,'Oro dental trauma':22,'Cleft lip':23,'Abscess':24,'Edentulism':25,'Impacted tooth':26,'Misalinged teeth':27,'Denture Stomatisis':28,'Geographic tongue':29,'HPV':30,'Lichen planus':31,'Thrush':32,'Diabetes':33,'Anodontia':34,'Talon cusps':35,'Tooth gemination':36,'Acne':37,'Hyperdontia':38,'Ectodermal Dysplasia':39,'Taurodontism':40
}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)

# TRAINING DATA
df=pd.read_csv("home_app/Training_dental.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'Tooth decay':2,'Gum disease':3,'Drug Reaction':4,'Bad breath':5,'Sensitive teeth':6,'Oral cancer':7,'Root infection':8,'Enamel erosion':9,'Dry mouth':10,'Teeth grinding':11,'Cavity':12,'Bacteria':13,'Gingivitis':14,'Oral candidiasis':15,'Periodontitis':16,'Probiotic':17,'Palate':18,'Tooth Crowding':19,'Halitosis':20,'Noma':21,'Oro dental trauma':22,'Cleft lip':23,'Abscess':24,'Edentulism':25,'Impacted tooth':26,'Misalinged teeth':27,'Denture Stomatisis':28,'Geographic tongue':29,'HPV':30,'Lichen planus':31,'Thrush':32,'Diabetes':33,'Anodontia':34,'Talon cusps':35,'Tooth gemination':36,'Acne':37,'Hyperdontia':38,'Ectodermal Dysplasia':39,'Taurodontism':40
}},inplace=True)

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)




def message():
    if (Symptom1.get() == "None" and  Symptom2.get() == "None" and Symptom3.get() == "None" and Symptom4.get() == "None" and Symptom5.get() == "None"):
        messagebox.showinfo("OPPS!!", "ENTER  SYMPTOMS PLEASE")
    else :
        NaiveBayes()

def NaiveBayes():
    from sklearn.naive_bayes import MultinomialNB

    gnb = MultinomialNB()
    # gnb = gnb.fit(X, np.ravel(y))

    gnb.fit(X, np.asarray(y, dtype=int).ravel())
    gnb = gnb.fit(X, pd.Series(np.ravel(y)))
    # gnb=gnb.fit(X,np.ravel(y))
    from sklearn.metrics import accuracy_score
    y_pred = gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(disease[predicted] == disease[a]):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "No Disease")

root = Tk()
root.title(" Disease Prediction From Symptoms")
root.configure()

Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)

w2 = Label(root, justify=LEFT, text=" Disease Prediction From Symptoms ")
w2.config(font=("Elephant", 30))
w2.grid(row=1, column=0, columnspan=2, padx=100)

NameLb1 = Label(root, text="")
NameLb1.config(font=("Elephant", 20))
NameLb1.grid(row=5, column=1, pady=10,  sticky=W)

S1Lb = Label(root,  text="Symptom 1")
S1Lb.config(font=("Elephant", 15))
S1Lb.grid(row=7, column=1, pady=10 , sticky=W)

S2Lb = Label(root,  text="Symptom 2")
S2Lb.config(font=("Elephant", 15))
S2Lb.grid(row=8, column=1, pady=10, sticky=W)

S3Lb = Label(root,  text="Symptom 3")
S3Lb.config(font=("Elephant", 15))
S3Lb.grid(row=9, column=1, pady=10, sticky=W)

S4Lb = Label(root,  text="Symptom 4")
S4Lb.config(font=("Elephant", 15))
S4Lb.grid(row=10, column=1, pady=10, sticky=W)

S5Lb = Label(root,  text="Symptom 5")
S5Lb.config(font=("Elephant", 15))
S5Lb.grid(row=11, column=1, pady=10, sticky=W)

lr = Button(root, text="Predict",height=2, width=20, command=message)
lr.config(font=("Elephant", 15))
lr.grid(row=15, column=1,pady=20)

OPTIONS = sorted(l1)

S1En = OptionMenu(root, Symptom1,*OPTIONS)
S1En.grid(row=7, column=2)

S2En = OptionMenu(root, Symptom2,*OPTIONS)
S2En.grid(row=8, column=2)

S3En = OptionMenu(root, Symptom3,*OPTIONS)
S3En.grid(row=9, column=2)

S4En = OptionMenu(root, Symptom4,*OPTIONS)
S4En.grid(row=10, column=2)

S5En = OptionMenu(root, Symptom5,*OPTIONS)
S5En.grid(row=11, column=2)

NameLb = Label(root, text="")
NameLb.config(font=("Elephant", 20))
NameLb.grid(row=13, column=1, pady=10,  sticky=W)

NameLb = Label(root, text="")
NameLb.config(font=("Elephant", 15))
NameLb.grid(row=18, column=1, pady=10,  sticky=W)

t3 = Text(root, height=2, width=30)
t3.config(font=("Elephant", 20))
t3.grid(row=20, column=1 , padx=10)

root.mainloop()
