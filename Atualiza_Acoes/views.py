from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.db import connection


def BuscaValoresParametros():
    # Busca e retorna o valor do time
    cursor_parametro = connection.cursor()
    comandoSQL = "select VITORIA_CASA , VITORIA_FORA , EMPATE_CASA , EMPATE_FORA , DERROTA_CASA , DERROTA_FORA from Futex_Parametros"
    cursor_parametro.execute(comandoSQL)
    parametros = cursor_parametro.fetchone()
        
    return float(parametros[0]) , float(parametros[1]) , float(parametros[2]) , float(parametros[3]) , float(parametros[4]) , float(parametros[5])


def BuscaValorAcaoTime(id_time):
    # Busca e retorna o valor do time
    cursor_time = connection.cursor()
    comandoSQL = "select printf('%.2f', valor) as valor from Futex_time where id_time = " + str(id_time)
    cursor_time.execute(comandoSQL)
    dados_time = cursor_time.fetchone()
    
    return float(dados_time[0])


def AtualizaAcao(id_time , valor):
    # Atualiza o valor do time
    cursor_time = connection.cursor()
    comandoSQL = "update Futex_Time set valor = " + str(valor) + " where id_time = " + str(id_time)
    cursor_time.execute(comandoSQL)
    
    return True


@login_required(login_url='/accounts/login/')
def index_atualiza_acoes(request):
    # Ler todos os times
    comandoSQL="select id_time , nome , estado , printf('%.2f', valor) as valor , valor as valor_real from Futex_time ORDER BY valor_real DESC"

    cursor_times = connection.cursor()
    cursor_times.execute(comandoSQL)
    lista_times = cursor_times.fetchall()

    # Montar o contexto que será enviado à pagina HTML
    context = {'Times':lista_times}

    # Renderizar a página HTML
    return render(request, 'Atualiza_Acoes/index_atualiza_acoes.html', context)


@login_required(login_url='/accounts/login/')
def atualiza_acoes(request):

    # Retornar o valor das ações de todos os times para R$ 10.00
    cursor_valor_inicial = connection.cursor()
    comandoSQL = "update Futex_Time set valor = 10"
    cursor_valor_inicial.execute(comandoSQL)

    # Ler todas as partidas cadastradas
    comandoSQL = "select id_time_casa_id , id_time_visitante_id , placar_time_casa , placar_time_visitante from Futex_Partida where placar_time_casa is not null and placar_time_visitante is not null order by id_partida , id_time_casa_id , id_time_visitante_id"
    cursor_partidas = connection.cursor()
    cursor_partidas.execute(comandoSQL)
    lista_partidas = cursor_partidas.fetchone()

    # Busca os valores dos parametros
    FATOR_VITORIA_CASA , FATOR_VITORIA_FORA , FATOR_EMPATE_CASA , FATOR_EMPATE_FORA , FATOR_DERROTA_CASA , FATOR_DERROTA_FORA = BuscaValoresParametros()

    # Para cada partida encontrada, atualizar o valor da ação dos times envolvidos
    while lista_partidas:
        id_time_casa = lista_partidas[0]
        id_time_visitante = lista_partidas[1]
        placar_time_casa = lista_partidas[2]
        placar_time_visitante = lista_partidas[3]
        valor_acao = 0
        if (placar_time_casa > placar_time_visitante):
            # O time da casa ganhou -> Verificar o placar
            dif_gols = placar_time_casa - placar_time_visitante
            valor_acao = BuscaValorAcaoTime(id_time_casa)
            valor_acao = valor_acao * (1 + (FATOR_VITORIA_CASA * dif_gols))
            AtualizaAcao(id_time_casa , valor_acao)
            
            valor_acao = BuscaValorAcaoTime(id_time_visitante)
            valor_acao = valor_acao * (1 - (FATOR_DERROTA_FORA * dif_gols))
            AtualizaAcao(id_time_visitante , valor_acao)
        elif (placar_time_casa == placar_time_visitante):
            # Empate
            # Atualizar valor do time da casa
            valor_acao = BuscaValorAcaoTime(id_time_casa)
            valor_acao = valor_acao * (1 + (FATOR_EMPATE_CASA))
            AtualizaAcao(id_time_casa , valor_acao)

            # Atualizar valor do time visitante
            valor_acao = BuscaValorAcaoTime(id_time_visitante)
            valor_acao = valor_acao * (1 + (FATOR_EMPATE_FORA))
            AtualizaAcao(id_time_visitante , valor_acao)
        else:
            # O time visitante ganhou
            dif_gols = placar_time_visitante - placar_time_casa
            valor_acao = BuscaValorAcaoTime(id_time_visitante)
            valor_acao = valor_acao * (1 + (FATOR_VITORIA_FORA * dif_gols))
            AtualizaAcao(id_time_visitante , valor_acao)
            
            valor_acao = BuscaValorAcaoTime(id_time_casa)
            valor_acao = valor_acao * (1 - (FATOR_DERROTA_CASA * dif_gols))
            AtualizaAcao(id_time_casa , valor_acao)

        lista_partidas = cursor_partidas.fetchone()

    cursor_partidas.close

    # Ler todos os times
    comandoSQL = "select id_time , nome , estado , printf('%.2f', valor) as valor from Futex_time ORDER BY nome"
    cursor_times = connection.cursor()
    cursor_times.execute(comandoSQL)
    lista_times = cursor_times.fetchall()
    cursor_times.close

    # Montar o contexto que será enviado à pagina HTML
    context = {'Times':lista_times}

    # Renderizar a página HTML
    return redirect('/atualiza_acoes')


@login_required(login_url='/accounts/login/')
def regras(request):

    # Ler todos os times
    comandoSQL="select VITORIA_CASA * 100 AS VITORIA_CASA , VITORIA_FORA * 100 AS VITORIA_FORA , EMPATE_CASA * 100 AS EMPATE_CASA , EMPATE_FORA * 100 AS EMPATE_FORA , DERROTA_CASA * 100 AS DERROTA_CASA , DERROTA_FORA * 100 AS DERROTA_FORA from Futex_Parametros"

    cursor_parametros = connection.cursor()
    cursor_parametros.execute(comandoSQL)
    lista_parametros = cursor_parametros.fetchall()

    # Montar o contexto que será enviado à pagina HTML
    context = {'Parametros':lista_parametros}


    # Renderizar a página HTML
    return render(request,'Atualiza_Acoes/regras.html', context)