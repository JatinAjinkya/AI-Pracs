#data set => already taken for prediction
dataset = {
"Ans":          ["Yes", "No", "Yes", "Yes", "No", "Yes", "No", "Yes", "No", "No", "No", "Yes"],
"Alternate":    ["Yes", "Yes", "No", "Yes", "Yes", "No", "No", "No", "No", "Yes", "No", "Yes"],
"Bar":          ["No", "No", "Yes", "No", "No", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes"],
"Fri/Sat":      ["No", "No", "No", "Yes", "Yes", "No", "No", "No", "Yes", "Yes", "No", "Yes"],
"Hungry":       ["Yes", "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes"],
"Patrons":      ["Some", "Full", "Some", "Full", "Full", "Some", "None", "Some", "Full", "Full", "None", "Full"],
"Price":        ["High", "Low", "Low", "Low", "High", "Medium", "Low", "Medium", "Low", "High", "Low", "Low"],
"Raining":      ["No", "No", "No", "Yes", "No","Yes", "Yes", "Yes", "Yes", "No", "No", "No"],
"Reservation":  ["Yes", "No", "No", "No", "Yes", "Yes", "No", "Yes", "No", "Yes", "No", "No"],
"Type":         ["French", "Thai", "Burger", "Thai", "French", "Italian", "Burger", "Thai", "Burger", "Italian", "Thai", "Burger"],
"WaitEstimate": ["0-10", "30-60", "0-10", "10-30", ">60","0-10", "0-10", "0-10", ">60", "10-30", "0-10", "30-60"]
}

#input data to test or predict
test_case = {
"Alternate":    "Yes",
"Bar":          "No",
"Fri/Sat":      "No",
"Hungry":       "Yes",
"Patrons":      "Full",
"Price":        "Low",
"Raining":      "No",
"Reservation":  "No",
"Type":         "Thai",
"WaitEstimate": "10-30"
}

def build_probs(ds, test_case):
    ans = ds["Ans"] #output attribute (ans)
    length = len(ans) #total length of output (ans)
    ans_set = set(ans) # unique (individual) classes yes and no
    count_ans = {k: ans.count(k) for k in ans_set} #count of yes and no classes of output attribute (ans) (frequency table)
    calc_prob = {k: count_ans[k] / length for k in ans_set} #P(yes|X), P(no|X)
    for ft in ds:
        if ft != "Ans":  #for all the input attributes except for output attr (ans)
            counts = {attr: {k: 0 for k in ans_set} for attr in set(ds[ft])} #for all input attribute prediction value, type => french= count(no) and count(yes
##            for i in range(length):
##                counts[ds[ft][i]][ans[i]] += 1 #taking a count of input attribute prediction
            for k in ans_set:
                calc_prob[k] *= counts[test_case[ft]][k] / count_ans[k] # calculating probability of input attributes -->Prob yes and no (likelihood table)
    print(test_case, ":\n", max(calc_prob, key=calc_prob.get)) #maximum value is considered as a prediction

build_probs(dataset, test_case)

