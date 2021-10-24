
from operator import itemgetter
 
class det:
    """Деталь"""
    def __init__(self, id, fio, price, dep_id):
        self.id = id
        self.fio = fio
        self.sal = price
        self.dep_id = dep_id
 
class mark:
    """Поставщик"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class DetMark:

    def __init__(self, dep_id, emp_id):
        self.dep_id = dep_id
        self.emp_id = emp_id
 
# Отделы
mark = [
    mark(1, 'Mitsubishi Motors'),
    mark(2, 'Honda Motors'),
    mark(3, 'Ford Motors'),
 
    mark(11, 'Toyota Motors'),
    mark(22, 'Tesla Company'),
    mark(33, 'VAG'),
]
 
# Детали
det = [
    det(1, 'Crankshaft', 18200, 1),
    det(2, 'Piston', 7350, 2),
    det(3, 'Gear set', 45000, 1),
    det(4, 'Water Pump', 12000, 3),
    det(5, 'Ignition coil', 1200, 3),
]
 
dets_marks = [
    DetMark(1,1),
    DetMark(2,2),
    DetMark(3,3),
    DetMark(3,4),
    DetMark(3,5),
 
    DetMark(11,1),
    DetMark(22,2),
    DetMark(33,3),
    DetMark(33,4),
    DetMark(33,5),
]
 
def main():
    """Основная функция"""
 
    # Соединение данных один-ко-многим 
    one_to_many = [(d.fio, d.sal, m.name) 
        for m in mark 
        for d in det 
        if d.dep_id==m.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, ed.dep_id, ed.emp_id) 
        for d in mark 
        for ed in dets_marks 
        if d.id==ed.dep_id]
    
    many_to_many = [(e.fio, e.sal, dep_name) 
        for dep_name, dep_id, emp_id in many_to_many_temp
        for e in det if e.id==emp_id]
 
    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)
    
    print('\nЗадание А2')
    res_12_unsorted = []

    for m in mark:

        m_dets = list(filter(lambda i: i[2]==m.name, one_to_many))
  
        if len(m_dets) > 0:
            # Зарплаты сотрудников отдела
            m_prices = [sal for _,sal,_ in m_dets]
            # Суммарная зарплата сотрудников отдела
            d_prices_sum = sum(m_prices)
            res_12_unsorted.append((m.name, d_prices_sum))
 
    # Сортировка по суммарной стоимости
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)
 
    print('\nЗадание А3')
    res_13 = {}
    # Перебираем все отделы
    for m in mark:
        if 'Motors' in m.name:
            m_dets = list(filter(lambda i: i[2]==m.name, many_to_many))
            m_dets_names = [x for x,_,_ in m_dets]

            res_13[m.name] = m_dets_names
 
    print(res_13)
 
if __name__ == '__main__':
    main()

