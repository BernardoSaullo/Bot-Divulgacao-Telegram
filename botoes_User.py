from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import mysql.connector



def conectar_ao_banco():
    # Função de conexão com o banco de dados MySQL
    try:
        return mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",  # Substitua pela sua senha correta
            database="ItsInvictus"  # Substitua pelo seu nome de banco de dados
        )
    except mysql.connector.Error as err:
        print(f"Erro ao acessar o banco de dados: {err}")
        return None

def botoesMenuUser():
    # Criação do teclado
    markup = InlineKeyboardMarkup()

    # Conectar ao banco de dados
    conexao = conectar_ao_banco()
    if not conexao:
        print("Erro ao acessar o banco de dados.")
        return markup

    cursor = conexao.cursor(dictionary=True)

    # Consultar a mensagem do suporte
    cursor.execute("SELECT Mensagem_aroba_suporte FROM mensagens LIMIT 1")
    mensagem_suporte = cursor.fetchone()

    # Consultar a URL das informações
    cursor.execute("SELECT Mensagem_aroba_informacoes FROM mensagens LIMIT 1")
    mensagem_info = cursor.fetchone()

    # Verificar se a consulta de suporte retornou um valor
    if mensagem_suporte:
        suporte_url = mensagem_suporte['Mensagem_aroba_suporte']
    else:
        suporte_url = "https://t.me/SuporteBravusListBot"  # Fallback para um valor padrão, caso não encontre

    # Verificar se a consulta de informações retornou um valor
    if mensagem_info:
        info_url = mensagem_info['Mensagem_aroba_informacoes']
    else:
        info_url = "https://t.me/BravusList"  # Fallback para um valor padrão, caso não encontre

    # Fechar o cursor e a conexão
    cursor.close()
    conexao.close()

    # Adiciona os botões ao teclado
    markup.row(
        InlineKeyboardButton("👤| 𝗠𝗲𝘂 𝗣𝗲𝗿𝗳𝗶𝗹", callback_data="menu_meu_perfil"),
        InlineKeyboardButton("👨🏻‍💻| 𝗦𝘂𝗽𝗼𝗿𝘁𝗲", url=suporte_url)
    )

    markup.row(
        InlineKeyboardButton("🗂| 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝗰̧𝗼̃𝗲", url=info_url),
        InlineKeyboardButton("📕| 𝗥𝗲𝗴𝗿𝗮𝘀", callback_data="menu_regras")
    )

    markup.add(
        InlineKeyboardButton('⚙| 𝗔𝗱𝗶𝗰𝗶𝗼𝗻𝗮𝗿 𝗴𝗿𝘂𝗽𝗼/𝗰𝗮𝗻𝗮𝗹', callback_data="menu_add")
    )

    return markup




def botaoRegras():
    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton("🏠 Início", callback_data='menu_inicio')
    )
    return markup

def botaoMeuPerfil():
    markup = InlineKeyboardMarkup()
    # Adicionar lógica de botões aqui, caso haja
    markup.add(
        InlineKeyboardButton("🏠 Início", callback_data='menu_inicio')
    )
    return markup


def botoesAdicaoCanalouGrupo():
    markup = InlineKeyboardMarkup()

    markup.row(
        InlineKeyboardButton("Adicionar Grupo 👥", url='http://t.me/BravusListBot?startgroup&admin=delete_messages+invite_users+pin_messages'),
        InlineKeyboardButton("Adicionar Canal 📢", url='http://t.me/BravusListBot?startchannel&admin=post_messages+edit_messages+delete_messages+invite_users+pin_messages+manager_chat')
    )

    # Adicionando o botão "🏠 Início"
    markup.add(
        InlineKeyboardButton("🏠 Início", callback_data='menu_inicio')
    )

    return markup
