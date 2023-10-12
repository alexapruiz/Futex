from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.db import connection
from Futex.models import Cliente


@login_required(login_url='/accounts/login/')
def dashboard(request):
    # Recuperar a quantidade de transações efetuadas
    ComandoSQL = "select count(0) as Total from Futex_historico_cliente where id_cliente = " + str(request.user.id)
    cursor_transacoes = connection.cursor()
    cursor_transacoes.execute(ComandoSQL)
    Total_Transacoes = cursor_transacoes.fetchone()
    cursor_transacoes.close

    # Recuperar o saldo do cliente
    cliente = Cliente.objects.get(id_cliente=request.user.id)

    # Calcular o valor da carteira
    ComandoSQL = "select sum(Carteira.qtde_acoes * Time.valor) as Total_Carteira "
    ComandoSQL += " from Futex_Carteira Carteira , Futex_Time Time "
    ComandoSQL += " where id_cliente_id = " + str(request.user.id)
    ComandoSQL += " and Carteira.id_time_id = Time.id_time "
    
    cursor_carteira = connection.cursor()
    cursor_carteira.execute(ComandoSQL)
    dados_carteira = cursor_carteira.fetchone()
    cursor_carteira.close

    if dados_carteira[0] is None:
        saldo_carteira = 0
    else:
        saldo_carteira = float(dados_carteira[0])

    # Calcula o resultado, descontando o valor inicial da carteira
    Saldo_Total = round(float(saldo_carteira) + float(cliente.saldo),2)
    resultado = round(Saldo_Total - 10000,2) 
    
    # Pesquisar o ranking e enviar os dados para a pagina HTML
    ComandoSQL  = " select Cliente.nome , printf('%.2f',sum(Carteira.qtde_acoes * Time.valor) + Cliente.saldo - 10000) as Carteira_Cliente , sum(Carteira.qtde_acoes * Time.valor) + Cliente.saldo - 10000 as Carteira_Cliente2 "
    ComandoSQL += " from Futex_Carteira Carteira , Futex_Time Time  , Futex_Cliente Cliente "
    ComandoSQL += " where Carteira.id_time_id = Time.id_time "
    ComandoSQL += " and Carteira.id_cliente_id = Cliente.id_cliente "
    ComandoSQL += " group by Cliente.nome "
    ComandoSQL += " order by Carteira_Cliente2 DESC "

    cursor_ranking = connection.cursor()
    cursor_ranking.execute(ComandoSQL)
    dados_ranking = cursor_ranking.fetchall()
    cursor_ranking.close
    
    context = {'usuario':request.user, 'Resultado':resultado , 'Saldo_Total':Saldo_Total , 'Total_Transacoes':Total_Transacoes[0] , 'Ranking': dados_ranking}
    return render(request, 'Futex/index.html', context)


@login_required(login_url='/accounts/login/')
def tabela_jogos(request,tipo_filtro):
    # Ler os dados dos jogos
    ComandoSQL =  " select P.id_rodada , T1.nome as Nome1 , P.placar_time_casa , P.placar_time_visitante , T2.nome as Nome2"
    ComandoSQL += " from Futex_Partida P , Futex_Time T1 , Futex_Time T2 "
    ComandoSQL += " where P.id_time_casa_id = T1.id_time "
    ComandoSQL += " and P.id_time_visitante_id = T2.id_time "
    
    # Se o usuário quiser ver apenas as partidas futuras
    if tipo_filtro == 'futuras':
        ComandoSQL += " and P.placar_time_casa is null "

    # Define a ordenação
    ComandoSQL += " order by P.id_partida "

    cursor_tabela_jogos = connection.cursor()
    cursor_tabela_jogos.execute(ComandoSQL)
    linhas_tabela_jogos = cursor_tabela_jogos.fetchall()
    cursor_tabela_jogos.close

    # Montar o contexto que será enviado à pagina HTML
    context = {'Tabela_Jogos' : linhas_tabela_jogos}
    
    # Renderizar a página HTML
    return render(request, 'Futex/tabela_jogos.html', context)


@login_required(login_url='/accounts/login/')
def perfil_usuario(request):

    cliente = Cliente.objects.get(id_cliente=request.user.id)
    context = {'cliente': cliente}
    
    # Renderizar a página HTML
    return render(request,'Futex/perfil_usuario.html', context)


@login_required(login_url='/accounts/login/')
def atualiza_usuario(request):
    nome_usuario = request.POST['nome']
    email_usuario = request.POST['email']
    endereco_usuario = request.POST['endereco']

    # Atualizar os dados do cliente com as informações da página
    comandoSQL="update Futex_Cliente set nome = '" + str(nome_usuario) + "' , email = '" + str(email_usuario) + "' , endereco = '" + str(endereco_usuario) + "' where id_cliente = " + str(request.user.id)

    cursor_cliente = connection.cursor()
    cursor_cliente.execute(comandoSQL)

    # Renderizar a página HTML
    return redirect('/perfil_usuario')