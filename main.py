def is_negativ(l):
    '''
    se returneaza o noua lista cu toate nr negative nenule din lista data
    :param l: lista de numere intregi
    :return: lista noua formata doar din numere negative nenule
    '''
    new_l=[]
    for x in l:
        if x<0:
            new_l.append(x)
    return new_l
def test_is_negativ():
    assert is_negativ([1,-1,2,-2,-3])==[-1, -2, -3]
    assert is_negativ([1,1,2,2,3])==[]
    assert is_negativ([-1,-2,-3])==[-1,-2,-3]
test_is_negativ()

def min_numar_cu_cifra_data(l,val):
    '''
    se cauta cel mai mic nr din lista care sa aiba ultima cifra egala cu val
    :param l: lista cu numere intregi
    :param val: cifra
    :return: cel mai mic numar din lista care indeplineste conditia
    '''
    min=99999999
    ok=0
    for x in l:
        if abs(x)%10==val:
                if min>x:
                    min=x
                    ok=1

    if ok==1 :
        return min
    return None

def test_min_numar_cu_cifra_data():
    assert min_numar_cu_cifra_data([1,-1,2,22,-3],2)== 2
    assert min_numar_cu_cifra_data([1,1,2,2,3],5)== None
    assert min_numar_cu_cifra_data([-1,-2,-32],2)==-32
test_min_numar_cu_cifra_data()


def verif_is_prim(nr):
    if nr < 2:
        return False
    elif nr == 2:
        return True
    elif nr % 2 == 0:
        return False
    else:
        for i in range(3, nr // 2 + 1, 2):
            if nr % i == 0:
                return False
        return True


def verif_super_prim(nr):
    string=str(nr)
    temp=len(string)-1
    while temp:
        if verif_is_prim(nr//(10**temp)) is False:
            return False
        temp-=1
    return True

def get_superprim(l):
    '''
    se returneaza o lista cu toate nr superprime din lista
    :param l: lista de numere intregi
    :return: lista cu toate numerele superprime
    '''
    new_l=[]
    for x in l:
        if x>0:
            if verif_super_prim(x) is True:
                new_l.append(x)
    return new_l

def test_get_superprim():
    assert get_superprim([173,239])==[239]
test_get_superprim()


def get_cmmdc_v2(x, y):
  # codul vostru aici
  r=x%y
  while r!=0:
      x=y
      y=r
      r=x%y
  return y

def get_invers(nr):
    n=0
    nr=abs(nr)
    while nr:
        n=n*10+nr%10
        nr=nr//10
    return -n

def get_lista_noua(l):
    '''
    se returneaza o lista noua in care numerele pozitive și nenule au fost înlocuite cu CMMDC-ul lor și numerele negative au cifrele în ordine inversă
    :param l: lista de numere intregi
    :return: lista noua care indeplineste cerinta de mai sus
    '''
    new_l=[]
    a=0
    b=0
    cmmdc=0
    for x in l:
        if x>0:
            if a==0:
                a=x
        elif x>0:
            if b==0:
                b=x
                cmmdc=get_cmmdc_v2(a,b)
        elif x>0:
            cmmdc = get_cmmdc_v2(cmmdc, x)


    for x in l:
        if x<0:
          new_l.append(get_invers(x))
        else:
            new_l.append(cmmdc)

    return new_l

def test_get_lista_noua():
    assert get_lista_noua([-76,12,24,-13,144])==[-67, 12, 12, -31, 12]
#test_get_lista_noua()

def read_list():
    # citim numerele asa: 3,56,7,1,3,43,5,54
    given = input('Dati numerele separate prin virgula: ')
    str_list = given.split(',')
    l = []
    for str_num in str_list:
        l.append(int(str_num))
    return l

def print_meniu():
    print("1. Citire lista")
    print("a. Afisare lista")
    print("2. Afișarea tuturor numerelor negative nenule din listă")
    print("3. Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.")
    print("4. Afișarea tuturor numerelor din listă care sunt superprime.")
    print("5. Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu CMMDC-ul lor și numerele negative au cifrele în ordine inversă.")
    print("x. Iesire")

def main():
    l=[]
    while True:
        print_meniu()
        option = input('Alegeti o optiune: ')
        if option == '1':
            l = read_list()
        elif option == '2':
            print("Lista noua este:\n")
            print(is_negativ(l))
        elif option == '3':
            val=int(input("Introduceti cifra: "))
            nr=min_numar_cu_cifra_data(l,val)
            if nr is not None:
                print("Numarul gasit este:",nr )
            else: print("Nu s-a gasit niciun nr")
        elif option == '4':
            print("Noua lista este:")
            print(get_superprim(l))
        elif option == '5':
            print("Noua lista este:")
            print(get_lista_noua(l))
        elif option == "a":
            print(l)
        elif option == 'x':
            break
        else:
            print('Optiune invalida, reincearca!')

if __name__ == '__main__':
  main()
