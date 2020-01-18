 # --*-- coding:utf-8 --*--

def run():
    counter = 0
    with open('borges.txt', 'r') as f:
       for line in f:
           counter += line.count('Carlos')
    
    print('Beatriz se encuentra {} en el texto'.format(counter))
           

if __name__ == '__main__':
    run()
