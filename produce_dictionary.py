import pandas as pd

produce_dictionary = {'Potatoes': [0.86, 12219, 10508],
                      'Okra': [2.26, 12960, 29290],
                      'Fava beans': [2.69, 11703, 31480],
                      'Watermelon': [0.66, 11485, 7580],
                      'Garlic': [1.19, 12512, 14889],
                      'Parsnips': [2.27, 11270, 25584],
                      'Asparagus': [2.49, 12848, 31991],
                      'Avocados': [3.23, 12369, 39953],
                      'Celery': [3.07, 12334, 37866],
                      'Spinach': [4.12, 11740, 48367],
                      'Cucumber': [1.07, 11994, 12834],
                      'Apricots': [3.71, 11762, 43637],
                      'Ginger': [5.13, 11915, 61126],
                      'Corn': [1.07, 11702, 12522],
                      'Grapefruit': [0.76, 11707, 8897],
                      'Eggplant': [2.32, 11843, 27477],
                      'Green cabbage': [0.8, 11611, 9289],
                      'Yellow peppers': [2.87, 12160, 34899],
                      'Grapes': [2.63, 12294, 32333],
                      'Cherries': [9.5, 12384, 117653],
                      'Apples': [1.88, 12397, 23307],
                      'Green beans': [2.52, 11483, 28938],
                      'Tomatoes': [3.16, 12016, 37969],
                      'Red onion': [0.78, 12549, 9788],
                      'Strawberries': [4.4, 11692, 51446],
                      'Papaya': [1.34, 11775, 15779],
                      'Butternut squash': [1.28, 11495, 14713],
                      'Bananas': [0.86, 12629, 10861],
                      'Lettuce': [1.88, 11891, 22355],
                      'Carrots': [1.26, 12204, 15377],
                      'Daikon': [1.4, 12146, 17004],
                      'Lime': [1.06, 11934, 12650],
                      'Green peppers': [1.89, 11981, 22645],
                      'Beets': [1.51, 12255, 18506],
                      'Coconuts': [1.18, 11840, 13972],
                      'Orange': [1.09, 11180, 12187],
                      'Lemon': [1.29, 12382, 15974],
                      'Brussels sprouts': [1.65, 11947, 19713],
                      'Kale': [5.02, 12293, 61711],
                      'Bok choy': [1.42, 11565, 16422]}

#use the dictionary to create a data frame with the produce names as rows and columns
#  named - "Cost Per Pound", "Quantity Sold" and "Total Sale"

produce = pd.DataFrame(produce_dictionary)
produce.index = ['Cost Per Pound', 'Quantity Sold', 'Total Sale']
produce = produce.T

print("--------------------------------------------------------------------------------------------------------")


print("\n1. Produce that had the highest and lowest sales in total sales (both name of produce and value)\n")

totalSale = produce["Total Sale"]
maxSale = totalSale.max()
minSale = totalSale.min()
print("Highest Sales: ", totalSale.idxmax(axis=0), " $", format(maxSale, ',.2f'), sep='')
print("Lowest Sales: ", totalSale.idxmin(axis=0), " $", format(minSale, ',.2f'), sep='')


print("\n--------------------------------------------------------------------------------------------------------")


print("\n2. Using 'loc', display the quantity and total sales for 'Orange' and 'Beets' (together)\n")

print(produce.loc[['Orange', 'Beets'], 'Quantity Sold':'Total Sale'])


print("\n--------------------------------------------------------------------------------------------------------")


print("\n3. Using 'loc', display the total sales for 'Apples' through 'Lettuce'\n")

print(produce.loc['Apples':'Lettuce', ['Total Sale']])


print("\n--------------------------------------------------------------------------------------------------------")


print("\n4. Using 'at', update the quantity sold for Apricots to 11,955 and total sales to 44,353.05\n")

print("Original Apricots Quantity Sold:", format(produce.at['Apricots','Quantity Sold'], ',.0f'))
print("Original Apricots Total Sale: $", format(produce.at['Apricots', 'Total Sale'], ',.2f'), "\n", sep='')

produce.at['Apricots','Quantity Sold']=11955
produce.at['Apricots', 'Total Sale']=44353.05

print("Updated Apricots Quantity Sold:", format(produce.at['Apricots','Quantity Sold'], ',.0f'))
print("Updated Apricots Total Sale: $", format(produce.at['Apricots', 'Total Sale'], ',.2f'), '\n', sep='')

print(produce)


print("\n--------------------------------------------------------------------------------------------------------")


print("\n5. What is the average quantity sold across all products? (print out ONLY quantity sold)\n")


quantitySold = produce["Quantity Sold"]
quantitySoldMean = quantitySold.mean()
print("Average Quantity Sold:", quantitySoldMean)


print("\n--------------------------------------------------------------------------------------------------------")


print("\n6. Create a new dataframe for only those produce that have sold between 11,500 to 12,000 (quantity)]\n")


new_produce = produce.loc[(produce["Quantity Sold"] >= 11500) & (produce["Quantity Sold"] <= 12000)]
print(new_produce)


print("\n--------------------------------------------------------------------------------------------------------")


print("\n7. What is the total sales for the products in the above new dataframe? (print out ONLY total sales)\n")

print("Total Sales of New Produce Dataframe: $", format(new_produce["Total Sale"].sum(), ',.2f'), sep='')

print("\n--------------------------------------------------------------------------------------------------------\n")

