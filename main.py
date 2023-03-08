import csv

from forming_new_file import Person


def make_new_file(all_data):
    data_list = []
    data = {}
    for i in all_data:
        if data.get(i['lastname']) is None:
            data[i['lastname']] = i
        else:
            for k, v in i.items():
                if data.get(i['lastname']).get(k) is None:
                    data.get(i['lastname'])[k] = v
    list_true = ['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']
    for i in data.values():
        data_ = []
        for j in list_true:
            for k, v in i.items():
                if k == j:
                    data_.append(v)
        data_list.append(data_)
    return data_list


def forming_data(data):
    info = {'lastname': 1, 'firstname': 3, 'surname': 5}
    name, organization, position, phone, email = Person(data).forming_new_data()
    new_data = {k: name.group(v) for k, v in info.items() if name.group(v) is not None}
    for i in organization:
        if i.group(1) is not None:
            new_data['organization'] = i.group(1)
        else:
            new_data['organization'] = i.group(2)[1:]
    if position is not None:
        for j in data:
            if position.group(0)[1:] in j:
                new_data['position'] = j
    if phone is not None:
        if phone.group(6) is not None:
            new_data['phone'] = f"+7({phone.group(2)}){phone.group(3)}-{phone.group(4)}-{phone.group(5)} " \
                                f"{phone.group(6).replace(' ', '')}"
        else:
            new_data['phone'] = f'+7({phone.group(2)}){phone.group(3)}-{phone.group(4)}-{phone.group(5)}'
    if email is not None:
        new_data['email'] = email.group(0)
    return new_data


def main():
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    new_contacts_list = make_new_file(map(lambda x: forming_data(x), contacts_list[1:]))
    new_contacts_list = [contacts_list[0]] + new_contacts_list
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_contacts_list)


if __name__ == '__main__':
    main()
