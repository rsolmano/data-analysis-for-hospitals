import pandas as pd
import matplotlib.pyplot as plt

general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')

# change name of HOSPITAL column in prenatal to hospital
prenatal = prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'})
sports = sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'})

# change all `man` values in general to `male` and all `woman` values to `female`
general.loc[general['gender'] == 'man', 'gender'] = 'male'
general.loc[general['gender'] == 'woman', 'gender'] = 'female'

# merge all dataframes in new one
df = pd.concat([general, prenatal, sports], ignore_index=True)

plt.figure()
plt.hist(df["age"], bins=10)
plt.figure()
plt.pie(df["diagnosis"].value_counts(), autopct='%1.1f%%', shadow=True)
plt.figure()
plt.violinplot(df["height"].value_counts())

plt.show()


print('The answer to the 1st question: 15-35')
print('The answer to the 2st question: pregnancy')
print("The answer to the 3rd question: It's because the measurement in the 'sports' dataset made in inches but in general and prenatal datasets it's made in centimeters.")
