from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from Futex.models import Carteira
from Futex.models import Time
from Futex.models import Cliente
from django.db import connection
from django.contrib import messages


@login_required(login_url='/accounts/login/')
def index_carteira(request):
    # Ler os dados da Carteira
    cursor_carteira = connection.cursor()
    comando_sql = "select Time.id_time , Time.nome , Time.estado , Carteira.qtde_acoes , printf('%.2f',Time.valor) as valor , printf('%.2f', Carteira.qtde_acoes * Time.valor) as Total from Futex_Carteira Carteira, Futex_Time as Time where Carteira.id_cliente_id = " + str(request.user.id) + " and Carteira.id_time_id = Time.id_time ORDER BY Time.Nome "
    cursor_carteira.execute(comando_sql)
    linhas_carteira = cursor_carteira.fetchall()
    cursor_carteira.close

    # Ler o valor total da Carteira do Cliente
    cursor_total = connection.cursor()
    cursor_total.execute("select printf('%.2f', sum(Carteira.qtde_acoes * Time.valor)) as Total_Cliente from Futex_Carteira Carteira, Futex_Time as Time where Carteira.id_time_id = Time.id_time and id_cliente_id = " + str(request.user.id))
    linha_total_cliente = cursor_total.fetchall()
    cursor_total.close

    # Ler todos os times
    cursor_times = connection.cursor()
    cursor_times.execute("select id_time , nome , estado , printf('%.2f', valor) as valor from Futex_time ORDER BY nome")
    lista_times = cursor_times.fetchall()
    cursor_times.close

    # Ler os dados do Cliente
    cursor_cliente = connection.cursor()
    cursor_cliente.execute("select nome, email, endereco, printf('%.2f',saldo) as saldo from Futex_Cliente where id_cliente = " + str(request.user.id))
    cliente = cursor_cliente.fetchall()
    cursor_cliente.close

    # Montar o contexto que será enviado à pagina HTML
    context = {'Carteira_Cliente' : linhas_carteira , 'Total_Cliente' : linha_total_cliente , 'Times':lista_times , 'Cliente' : cliente}
    
    # Renderizar a página HTML
    return render(request, 'Carteira/index_carteira.html', context)


@login_required(login_url='/accounts/login/')
def vender_acao(request,id_time):
    # Ler os dados da ação a ser vendida
    carteira = Carteira.objects.get(id_cliente = str(request.user.id) , id_time = id_time)
    time = Time.objects.get(id_time=id_time)
    valor_operacao = carteira.qtde_acoes * time.valor

    # Vender a ação selecionada e devolver o valor para o saldo do cliente
    cursor_carteira = connection.cursor()
    cursor_carteira.execute("delete from Futex_Carteira where id_cliente_id = " + str(request.user.id) + " and id_time_id = " + str(id_time))
    cursor_carteira.close

    # Atualizar o saldo do Cliente
    sql_update = "update Futex_Cliente set saldo = saldo + " + str(valor_operacao) + " where id_cliente = " + str(request.user.id)
    cursor_carteira = connection.cursor()
    cursor_carteira.execute(sql_update)
    cursor_carteira.close
    
    # Inserir o registro de histórico de venda
    Comando_Insert = "insert into Futex_Historico_Cliente (id_cliente, id_time, valor , tipo_operacao , qtde_acoes) values ("
    Comando_Insert += str(request.user.id) + " , "
    Comando_Insert += str(id_time) + " , "
    Comando_Insert += str(time.valor) + " , "
    Comando_Insert += " 2 , " # tipo = venda
    Comando_Insert += str(carteira.qtde_acoes) + " ) "

    cursor_historico = connection.cursor()
    cursor_historico.execute(Comando_Insert)
    cursor_historico.close

    return redirect('/carteira')


@login_required(login_url='/accounts/login/')
def comprar_acao(request, id_time):
    if request.method == 'GET':
        # Ler os dados da Carteira
        cursor_carteira = connection.cursor()
        cursor_carteira.execute("select Time.id_time , Time.nome , Time.estado, Carteira.qtde_acoes , Time.valor , printf('%.2f', Carteira.qtde_acoes * Time.valor) as Total from Futex_Carteira Carteira, Futex_Time as Time where Carteira.id_cliente_id = " + str(request.user.id) + " and Carteira.id_time_id = Time.id_time ORDER BY Time.nome")
        linhas_carteira = cursor_carteira.fetchall()
        cursor_carteira.close

        # Ler o valor total da Carteira do Cliente
        cursor_total = connection.cursor()
        cursor_total.execute("select printf('%.2f', sum(Carteira.qtde_acoes * Time.valor)) as Total_Cliente from Futex_Carteira Carteira, Futex_Time as Time where Carteira.id_time_id = Time.id_time and id_cliente_id = " + str(request.user.id))
        linha_total_cliente = cursor_total.fetchall()
        cursor_total.close

        # Ler os dados do Cliente
        cursor_cliente = connection.cursor()
        cursor_cliente.execute("select nome, email, endereco, printf('%.2f',saldo) as saldo from Futex_Cliente where id_cliente = " + str(request.user.id))
        cliente = cursor_cliente.fetchall()
        cursor_cliente.close

        # Ler os dados do time
        cursor_times = connection.cursor()
        cursor_times.execute("select id_time , nome , estado , printf('%.2f', valor) from Futex_time where id_time = " + str(id_time))
        time = cursor_times.fetchall()
        cursor_times.close

        # Montar o contexto que será enviado à pagina HTML
        context = {'Carteira_Cliente' : linhas_carteira , 'Total_Cliente' : linha_total_cliente , 'Time':time , 'Cliente' : cliente}
    
        # Renderizar a página HTML
        return render(request, 'Carteira/comprar_acao.html', context)
    else:
        # Efetuar a compra das ações
        # Verificar se o cliente já possui ações deste time
        carteira = Carteira.objects.filter(id_cliente=request.user.id , id_time_id = id_time)
        time = Time.objects.get(id_time=id_time)
        valor_operacao = int(request.POST['qtde_acoes']) * time.valor

        # Verificar se o cliente tem saldo para comprar as ações
        cursor_cliente = connection.cursor()
        cursor_cliente.execute("select saldo from Futex_Cliente where id_cliente = " + str(request.user.id))
        cliente = cursor_cliente.fetchone()
        saldo = cliente[0]
        cursor_cliente.close

        if ( valor_operacao > saldo ):
            # Saldo Insuficiente
            messages.info(request, 'Saldo Insuficiente')
            return redirect('.')

        if carteira:
            # Atualizar a qtde de ações
            cursor_carteira = connection.cursor()
            sql_insert = "update Futex_Carteira set qtde_acoes = qtde_acoes + " + request.POST['qtde_acoes'] + " where id_cliente_id = " + str(request.user.id) + " and id_time_id = " + str(id_time)
            cursor_carteira.execute(sql_insert)
            cursor_carteira.close
        else:
            # Inserir registro com a qtde de ações compradas
            cursor_carteira = connection.cursor()
            sql_insert = "insert into Futex_Carteira (id_cliente_id,id_time_id,qtde_acoes) values (" + str(request.user.id) + " , " + str(id_time) + " , " + str(request.POST['qtde_acoes']) + " )"
            cursor_carteira.execute(sql_insert)
            cursor_carteira.close

        # Atualizar o saldo do Cliente
        sql_update = "update Futex_Cliente set saldo = saldo - " + str(valor_operacao) + " where id_cliente = " + str(request.user.id)
        cursor_carteira = connection.cursor()
        cursor_carteira.execute(sql_update)
        cursor_carteira.close

        # Inserir o registro de histórico de compra
        Comando_Insert = "insert into Futex_Historico_Cliente (id_cliente, id_time, valor , tipo_operacao , qtde_acoes) values ("
        Comando_Insert += str(request.user.id) + " , "
        Comando_Insert += str(id_time) + " , "
        Comando_Insert += str(time.valor) + " , "
        Comando_Insert += " 1 , " # tipo = compra
        Comando_Insert += str(request.POST['qtde_acoes']) + " ) "

        cursor_historico = connection.cursor()
        cursor_historico.execute(Comando_Insert)
        cursor_historico.close

        return redirect('/carteira')