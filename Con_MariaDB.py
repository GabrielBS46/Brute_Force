import sys
import pymysql
import time
import os
import colorama
import banco # Conexão com o banco

# import pymysql
# con = pymysql.connect(
#     host='IP',
#     user='usuario',
#     database='Banco',
#     password='Senha',
#     cursorclass=pymysql.cursors.DictCursor)

### Colors
color = colorama.Fore
green = color.GREEN
red = color.RED
blue = color.BLUE
reset = color.RESET


### Comunicando com MariaDB, importando conf da biblioteca banco
def conecta():
    try:
        global con
        con = banco.con
        
    except pymysql.Error as e:
        print(f"{red}Erro ao conectar: {e} {reset}")
        sys.exit

### Opção1, cadastro de um novo site
def cad_site():
    site=input("Informe o site para cadastro: ")
    login=input("Informe o login/username: ")
    password=input("Informe a senha/password: ")
    conecta()
    with con.cursor() as c:
        try:
            sql="SELECT site FROM usuario WHERE site = '"+ site +"';"
            c.execute(sql)
            res=c.fetchall()
            if (len(res)) == 0:
                sql="INSERT INTO usuario (site,login,password) VALUES('"+site+"','"+login+"','"+password+"');"
                try:
                    c.execute(sql)
                    con.commit()
                    print (f"{green}\nAdicionado com Sucesso{reset}")
                except pymysql.Error as e:
                    print(f"{red}\nErro ao Adicionar: {e} {reset}")
            else:
                print(f"{red}\nSite {site} já está cadastrado{reset}")
        except pymysql.Error as e:
            print(f"{red}\nErro ao Adicionar: {e}{reset}")
            sys.exit   
        next() 

### Opção2, mostrando sites cadastrado no banco
def show_site():
    conecta()
    with con.cursor() as c:
        try:
            sql = "SELECT * FROM usuario;"
            c.execute(sql)
            res=c.fetchall()
            for i in res:
                print(f"{green}Site: {i['site']}\tUsuario: {i['login']}\tSenha: {i['password']}{reset}")
        except pymysql.Error as e:
            print(f"{red}Erro ao Selecionar: {e}{reset}")
            sys.exit
        next()

### Opção3, alterando a senha de algum site
def alter_site():
    site=input("Qual site ira alterar senha: ")
    conecta()
    with con.cursor() as c:
        try:
            sql="SELECT site FROM usuario WHERE site = '"+ site +"';"
            c.execute(sql)
            res=c.fetchall()
            if (len(res)) == 1:
                senha=input("Digite a nova senha: ")
                sql="UPDATE usuario SET password = '"+ senha +"' WHERE site = '"+ site +"';"
                try:
                    c.execute(sql)
                    con.commit()
                    print (f"{green}\nAlterado com Sucesso{reset}")
                except pymysql.Error as e:
                    print(f"{green}Erro ao Selecionar: {e}{reset}")
            else:
                print(f"{red}\nSite {site} não cadastrado{reset}")
        except pymysql.Error as e:
            print(f"{red}\nErro ao Selecionar: {e}{reset}")
            sys.exit
        next()

### Opção4, removendo site do banco
def rem_site():
    site=input("Qual site ira alterar senha: ")
    conecta()
    with con.cursor() as c:
        try:
            sql="SELECT site FROM usuario WHERE site = '"+ site +"';"
            c.execute(sql)
            res=c.fetchall()
            if (len(res)) == 1:
                sql="DELETE FROM usuario WHERE site = '" + site + "';"
                try:
                    c.execute(sql)
                    con.commit()
                    print (f"{green}\nRemovido com Sucesso{reset}")
                except pymysql.Error as e:
                    print(f"{red}Erro ao Remover: {e}{reset}")
            else:
                print(f"{red}\nSite {site} não cadastrado{reset}")
        except pymysql.Error as e:
            print(f"{red}\nErro ao Remover: {e}{reset}")
            sys.exit   
        next() 

### Verificando se deseja continuar com novas buscas
def next():
    next=input("\nDeseja continuar? Y/n ")
    if next == "Y" or next == "y" or next == "s" or next == "S":
        clear()
    elif next == "n" or next == "N":
        print(f"{green}Até logo{reset}")
        clear()
        sys.exit()
    else:
        print(f"{red}Inválido, até logo{reset}")
        clear()
        sys.exit()      

### Limpeza de tela
def clear():
    time.sleep(1)
    os.system("clear")

### Inicio do programa
if __name__ == '__main__':
    os.system('clear')
    while True:
        print(""" 
            1) Inserir nova senha
            2) Verificar senhas salvas
            3) Alterar senha
            4) Deletar senha
            5) Sair
        """)
        choice=int(input("Escolha sua opção: "))
        print("\n")
        if choice == 1:
            cad_site()
        elif choice == 2:
            show_site()
        elif choice == 3:   
            alter_site()
        elif choice == 4:
            rem_site()
        elif choice == 5:
            print(f"{green}\nAté Logo{reset}")
            clear()
            sys.exit()
        else:
            print(f"{red}\nInvalido{reset}")
            clear()

