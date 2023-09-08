import sys
import pymysql
import time
import os
import banco

def conecta():
    try:
        global con
        con = banco.con
        
    except pymysql.Error as e:
        print(f"Erro ao conectar: {e}")
        sys.exit

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
                    print ("\nAdicionado com Sucesso")
                except pymysql.Error as e:
                    print(f"\nErro ao Adicionar: {e}")
            else:
                print(f"\nSite {site} já está cadastrado")
        except pymysql.Error as e:
            print(f"\nErro ao Adicionar: {e}")
            sys.exit   
        next() 

def show_site():
    conecta()
    with con.cursor() as c:
        try:
            sql = "SELECT * FROM usuario;"
            c.execute(sql)
            res=c.fetchall()
            for i in res:
                print(f"Site: {i['site']}\tUsuario: {i['login']}\tSenha: {i['password']}")
        except pymysql.Error as e:
            print(f"Erro ao Selecionar: {e}")
            sys.exit
        next()

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
                    print ("\nAlterado com Sucesso")
                except pymysql.Error as e:
                    print(f"Erro ao Selecionar: {e}")
            else:
                print(f"\nSite {site} não cadastrado")
        except pymysql.Error as e:
            print(f"\nErro ao Selecionar: {e}")
            sys.exit
        next()

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
                    print ("\nRemovido com Sucesso")
                except pymysql.Error as e:
                    print(f"Erro ao Remover: {e}")
            else:
                print(f"\nSite {site} não cadastrado")
        except pymysql.Error as e:
            print(f"\nErro ao Remover: {e}")
            sys.exit   
        next() 

def next():
    next=input("\nDeseja continuar? Y/n ")
    if next == "Y" or next == "y" or next == "s" or next == "S":
        clear()
    elif next == "n" or next == "N":
        print("Até logo")
        clear()
        sys.exit()
    else:
        print("Inválido, até logo")
        clear()
        sys.exit()      

def clear():
    time.sleep(1)
    os.system("clear")

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
            print("\nAté Logo")
            clear()
            sys.exit()
        else:
            print("\nInvalido")
            clear()

