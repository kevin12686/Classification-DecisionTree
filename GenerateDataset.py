import random
import csv


class Attr:
    def __init__(self, name, values):
        self.name = name
        self.values = list(values.keys())
        self.weight = list(values.values())

    def random(self):
        return random.choices(self.values, self.weight, k=1)[0]


class DataGenerator:
    def __init__(self):
        self.attrs = list()
        self.rule = dict()

    def add_attr(self, attr_):
        self.attrs.append(attr_)

    def set_right_rule(self, rule):
        self.rule = rule

    def generate(self, size_, output=None):
        dataset_ = list()
        for i in range(size_):
            temp = dict()
            for a in self.attrs:
                temp[a.name] = a.random()
            if self.rule:
                predict = "True"
                for name, val in self.rule.items():
                    if temp[name] != val:
                        predict = "False"
                        break
                temp["Predict Class"] = predict
            dataset_.append(temp)
        if output:
            attr_name = [i.name for i in self.attrs]
            with open(output, "w", newline="") as f:
                label = attr_name
                if self.rule:
                    label += ["Predict Class"]
                writer = csv.DictWriter(f, fieldnames=label)
                writer.writeheader()
                for i in range(len(dataset_)):
                    temp = dict(**dataset_[i])
                    writer.writerow(temp)
        return dataset_


if __name__ == '__main__':
    size = 300
    attrs = [
        Attr("License", {"True": 3, "False": 1}),
        Attr("Drunk", {"True": 1, "False": 3}),
        Attr("Glasses", {"True": 1, "False": 1}),
        Attr("Clothes Color", {"Red": 1, "Blue": 1, "Green": 1, "Yellow": 1, "Purple": 1, "White": 1, "Black": 1}),
        Attr("Weight", {"Thin": 1, "Normal": 1, "Fat": 1}),
        Attr("Eat Beef", {"True": 1, "False": 1}),
        Attr("Vegetarianism", {"True": 1, "False": 1}),
        Attr("Gender", {"Male": 1, "Female": 1, "Others": 1}),
        Attr("Unemployed", {"True": 1, "False": 1}),
        Attr("Hair", {"No": 1, "Short": 1, "Long": 1}),
        Attr("Watch", {"True": 1, "False": 1}),
        Attr("Hat", {"True": 1, "False": 1}),
        Attr("Member of Costco", {"True": 1, "False": 1}),
        Attr("Member of Ikea", {"True": 1, "False": 1}),
        Attr("Member of Carrefour", {"True": 1, "False": 1}),
        Attr("Use Gmail", {"True": 1, "False": 1}),
        Attr("Foreigner", {"True": 1, "False": 1}),
        Attr("Use Apple", {"True": 1, "False": 1}),
        Attr("Tired", {"True": 1, "False": 3}),
        Attr("Health", {"True": 3, "False": 1}),
    ]

    gen = DataGenerator()
    for attr in attrs:
        gen.add_attr(attr)
    gen.set_right_rule({"License": "True", "Drunk": "False", "Tired": "False", "Health": "True"})
    dataset = gen.generate(500, output="dataset.csv")
